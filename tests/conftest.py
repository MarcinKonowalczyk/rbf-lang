from pathlib import Path
import sys


__project_root__ = Path(__file__).resolve().parents[1]
sys.path.append(str(__project_root__))
