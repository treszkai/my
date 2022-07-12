import pandas as pd

# Everything useful happens at import time, __all__ is empty.
__all__ = []

@pd.api.extensions.register_dataframe_accessor("Q")
class QueryAccessor:
    """Shorthand for the DataFrame.query method

    Usage:
        >>> import pandas as pd
        >>> import my
        >>> df = pd.DataFrame([[0,1],[2,3]], columns=['A','B'])
        >>> df.Q['A > 1']
           A  B
        1  2  3
    """
    def __init__(self, pandas_obj):
        self.df = pandas_obj

    def __getitem__(self, query):
        return self.df.query(query)

