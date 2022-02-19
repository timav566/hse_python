import numbers

import numpy as np


class ArrayLike(np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, value):
        self.value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        inputs = tuple(x.value if isinstance(x, ArrayLike) else x
                       for x in inputs)

        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, ArrayLike) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)


class StrMixin:

    def __str__(self):
        res = "This is an ArrayLike object:\n"
        res += str(self.value)
        return res

class FileWriteMixin:

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.__str__())

class GetAndSetMixin:

    def __set__(self, instance, value):
        self.value = value

    def __get__(self):
        return self.value

class SuperArrayLike(ArrayLike, StrMixin, FileWriteMixin, GetAndSetMixin):
    pass


np.random.seed(0)
a = SuperArrayLike(np.random.randint(0, 10, (10, 10)))
b = SuperArrayLike(np.random.randint(0, 10, (10, 10)))

with open("./artifacts/medium/matrix+.txt", 'w') as f:
    f.write((a + b).__str__())

with open("./artifacts/medium/matrix1.txt", 'w') as f:
    f.write((a * b).__str__())

with open("./artifacts/medium/matrix@.txt", 'w') as f:
    f.write((a @ b).__str__())
