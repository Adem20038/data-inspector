from pathlib import Path
import sys

# ==================================================
# PROJECT ROOT
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ==================================================
# PYTHON PATH CONFIGURATION
# ==================================================

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))