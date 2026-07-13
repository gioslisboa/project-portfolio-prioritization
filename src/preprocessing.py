
"""
Preprocessing utilities for project portfolio prioritization.
"""

import pandas as pd
import sys
from pathlib import Path

project_root = Path().resolve().parent

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

def build_decision_matrix(
    df: pd.DataFrame,
    criteria: dict,
) -> pd.DataFrame:
    """
    Build the decision matrix from the selected criteria.

    Parameters
    ----------
    df : pandas.DataFrame
        Original dataset.

    criteria : dict
        Dictionary where the keys are the selected criteria and the values
        indicate whether the criterion should be minimized ("min")
        or maximized ("max").

    Returns
    -------
    pandas.DataFrame
        Decision matrix.
    """

    return df[list(criteria.keys())].copy()