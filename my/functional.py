from typing import Callable, Optional, TypeVar

T = TypeVar('T')
U = TypeVar('U')


def filterNotNone(seq):
    return (x for x in seq if x is not None)


def maybe(f: Callable[[Optional[T]], U]) -> Callable[[Optional[T]], Optional[U]]:
    """Haskell’s fmap function for the Maybe type class

    fmap :: (a -> b) -> Maybe a -> Maybe b

    - if x is None, then f is not called, and fmap(f)(x) is None;
    - if f(x) raises an Exception, fmap(f)(x) returns None.
    """
    def wrapped(x):
        if x is None:
            return None
        try:
            return f(x)
        except Exception:
            return None

    return wrapped
