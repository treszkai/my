"""
Tired of repeating the argparse chore? My.argparse to the rescue!

Previously, you had to write:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    args = parser.parse_args()
    print(args.foo)

Now you can get away with:
    from my import argparse

    argparse.add_argument('--foo')
    args = argparse.parse_args()
    print(args.foo)

Or, if you're feeling reckless:
    from my.argparse import add_argument, args

    add_argument('--foo')
    print(args.foo)

Isn't it beautiful?
...
No! Because now you're manipulating a state which shouldn't exist
by most standards. Even though parser.parse_args() implicitly
plucks the command-line arguments from sys.argv, this simplified
interface hides the mutable state *in the module*, and it's already
bad enough when instance states are mutated without mercy.
Furthermore, when relying on automatic parsing upon attribute access
(as in the latter version), you can't nicely catch the errors of
incorrectly specified arguments.
"""

import argparse
from functools import partial

parser = argparse.ArgumentParser()
add_argument = partial(parser.add_argument)
parse_args = parser.parse_args


class DelayedNamespace(argparse.Namespace):
    @property
    def is_initialized(self):
        return bool(vars(self))

    def parse_args(self):
        args = parser.parse_args()
        for name, value in vars(args).items():
            setattr(self, name, value)

    def __getattr__(self, item):
        if not self.is_initialized:
            self.parse_args()
        return super().__getattribute__(item)

    def __contains__(self, item):
        if not self.is_initialized:
            self.parse_args()

        return super().__contains__(item)

    def __repr__(self):
        if not vars(self):
            return f"{self.__class__.__qualname__}()"
        else:
            return super().__repr__()


args = DelayedNamespace()
