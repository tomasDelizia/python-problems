import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.arrays.binary_search import binary_search

__all__ = ["binary_search"]
