from unittest import TestCase
from unittest.util import safe_repr

from unittest.mock import Mock


class TestMyMock(TestCase):
    def assertMethodTrue(self, obj, method, msg=None):
        if not eval(f"obj{method}"):
            msg = self._formatMessage(
                msg,
                f"obj{method} is not true, where obj is %s" % safe_repr(obj)
            )
            raise self.failureException(msg)

    def test_assert_method_true(self):
        m = Mock()
        m.foo = Mock()
        m.foo.bar = Mock(return_value=True)
        m.foo.baz = Mock(return_value=False)

        self.assertTrue(m.foo.bar())
        self.assertFalse(m.foo.baz())

        self.assertMethodTrue(m, ".foo.baz()")

        with self.assertRaises(AssertionError):
            self.assertMethodTrue(m, ".foo.baz()")
