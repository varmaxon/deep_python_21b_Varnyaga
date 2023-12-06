"""Module with MetaClass"""


class CustomMeta(type):
    """MetaClass for renaming attributes"""

    def __new__(mcs, name, bases, dct):
        corrected_dict = {}
        for i, val in dct.items():
            if i.startswith('__') and i.endswith('__'):
                corrected_dict[i] = val
            else:
                corrected_dict['custom_' + i] = val

        corrected_dict["__setattr__"] = mcs.__new_setattr__

        cls = super().__new__(mcs, name, bases, corrected_dict)
        return cls

    def __new_setattr__(cls, key, value):
        """rename attributes in class's __init__ (for object fields)"""

        object.__setattr__(cls,
                           "custom_" + key if (not key.startswith('__')) and (not key.endswith('__')) else key,
                           value)
