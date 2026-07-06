from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Missing GOOGLE_API_KEY in .env file")

MODEL_NAME = os.getenv("GEMINI_MODEL")

if not MODEL_NAME:
    raise ValueError("Missing GEMINI_MODEL in .env file")

client = genai.Client(api_key=api_key)


# ==================================================
# GENERIC AI REQUEST
# ==================================================

def ask_ai(prompt):
    """
    Send a prompt to Gemini and return the generated response.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"AI Error: {e}"


# ==================================================
# DEBUG REPORT
# ==================================================

def generate_debug_report(error_message, code_snippet):
    """
    Explain a Python error and suggest a correction.
    """

    prompt = f"""
    You are a senior Python Data Engineer.
    
    A developer is debugging a Python data pipeline.
    
    Code:
    
    {code_snippet}
    
    Error:
    
    {error_message}
    
    Please provide:
    
    1. A clear explanation of the error.
    2. The root cause.
    3. A corrected version of the code.
    4. Best practices to avoid this issue.
    
    Keep your answer concise and practical.
    """

    return ask_ai(prompt)


# ==================================================
# DATA QUALITY REPORT
# ==================================================

def generate_quality_report(metrics, data):
    """
    Generate a deeper AI-driven data quality report using:
    - computed metrics
    - raw dataset sample (for pattern detection)
    """

    # Convert dataset safely (avoid dumping huge dataframes)
    data_sample = None

    try:
        # if pandas DataFrame
        data_sample = data.head(50).to_string()

    except Exception:
        try:
            # if dict or list
            data_sample = str(data)[:5000]
        except Exception:
            data_sample = "Data could not be serialized."

    prompt = f"""
    You are a senior Data Quality & Data Engineering expert.
    
    You are analyzing a dataset from an educational information system.
    
    Your task is NOT to repeat metrics.
    
    You must go deeper than surface-level descriptions.
    
    ---
    
    ## CONTEXT: COMPUTED METRICS
    {metrics}
    
    ---
    
    ## RAW DATA SAMPLE (FIRST ROWS)
    {data_sample}
    
    ---
    
    ## YOUR TASK
    
    Write a professional analytical report that:
    
    ### 1. Avoids repetition
    Do NOT restate metric values directly.
    
    ### 2. Finds hidden patterns
    Try to detect:
    - inconsistencies between fields
    - structural issues in schema usage
    - potential data modeling problems
    - anomalies visible from sample data
    
    ### 3. Provides interpretation
    Explain WHY these metrics might be happening.
    
    ### 4. Goes beyond numbers
    Make insights that are NOT directly visible in metrics output.
    
    ### 5. Produces an expert-level report:
    
    ## Executive Summary
    (interpretation, not numbers)
    
    ## Data Structure Observations
    (schema-level insights)
    
    ## Coverage Interpretation
    (why coverage behaves this way)
    
    ## Noise Analysis (root causes)
    (not just percentages)
    
    ## Integrity Issues (data modeling problems)
    
    ## Duplicate Patterns (where they originate)
    
    ## Hidden Risks
    (important)
    
    ## Recommendations
    (actionable engineering improvements)
    
    ---
    
    Be concise but insightful.
    Act like a senior data engineer reviewing a production system.
    """

    return ask_ai(prompt)