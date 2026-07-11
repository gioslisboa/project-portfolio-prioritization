def build_decision_matrix(df, criteria):
    """
    Build the decision matrix used by the AHP-Gaussian model.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    criteria : dict
        Dictionary where keys are criteria names.

    Returns
    -------
    pandas.DataFrame
        Decision matrix.
    """

    return df[list(criteria.keys())].copy()