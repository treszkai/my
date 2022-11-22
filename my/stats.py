import scipy.stats as st


def compare_ratios(a: float | tuple[int, int], b: float | tuple[int, int]):
    """The probability that probability `a` is lower than `b`

    One of `a` and `b` should be a float (a fixed probability), the other a
    tuple of ints, representing (number of successes, total number of events),
    assuming a uniform prior.
    """
    match a, b:
        case (float(), float()):
            return 0.5 if a == b else float(a < b)
        case (float(), (int(), int())):
            b_success, b_total = b
            return st.beta.sf(a, b_success + 1, b_total - b_success + 1)
        case ((int(), int()), float()):
            return 1 - compare_ratios(b, a)
        case ((int(), int()), (int(), int())):
            # TODO
            raise NotImplementedError('comparing two tuples is not implemented yet')
        case _:
            raise TypeError(
                'Every argument of compare_ratios must be either a float or a pair of integers.'
            )
