import scipy.stats as st


def compare_ratios(a: float | tuple[int, int], b: float | tuple[int, int]):
    """The probability that probability `a` is lower than `b`

    One of `a` and `b` should be a float (a fixed probability), the other a
    tuple of ints, representing (number of successes, total number of events),
    assuming a uniform prior.
    """
    if isinstance(a, float) and isinstance(b, tuple):
        return st.beta.cdf(a, b[0] + 1, b[1] - b[0] + 1)
    elif isinstance(b, float) and isinstance(a, tuple):
        return 1 - compare_ratios(b, a)
    else:
        # TODO
        raise NotImplementedError
