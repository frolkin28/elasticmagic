try:
    from collections.abc import Iterable, Mapping  # noqa:F401
except ImportError:
    from collections import Iterable, Mapping  # noqa:F401


text_type = str
string_types = (str,)
binary_type = str
int_types = (int,)


def force_unicode(value):
    """
    Forces a bytestring to become a Unicode string.
    """
    if isinstance(value, bytes):
        value = value.decode('utf-8', errors='replace')
    elif not isinstance(value, str):
        value = str(value)

    return value


def with_metaclass(meta, *bases):
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)

    return metaclass('temporary_class', None, {})
