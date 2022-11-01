# My Python utilities

The standard `pickle` module of Python expects a file object as an argument, not a filename. Let’s make life convenient and [spare myself 10 seconds a hundred times a year](https://xkcd.com/1205/) `\o/` 

`my` package contains:
 - `my.dump(obj, filename)`, to Pickle dump an object to a file, specified by a filename
 - `my.load(filename)`, to Pickle load an object from a file, specified by a filename
 - `my.load_or_do(filename, func)`, to Pickle load an object from a file if the file exists,
   or pickle the return value of `func()` under `filename` otherwise.
 - `my.maybe(func)`, which applies `func()` on non-`None` values, and returns `None` othewise.

This package requires Python 3.10 or later.

## Building the package

The `my.gil` module was written in C, therefore needs to be _built_ with:

```shell
python setup.py build
```

Then copy the resulting `build/*/gil.*.so` file to the `my/` package.

## Demos

My Pickle dump and load:
```python
import my

shrugs = r'¯\_(ツ)_/¯'
my.dump(shrugs, 'shrugs.pickle')
x = my.load('shrugs.pickle')
assert x == shrugs
```

My Pickle load or do:
```python
func_called = 0
def calc_big():
    global func_called
    func_called += 1
    return sum(range(10))

n = my.load_or_do('number.pickle', calc_big)
assert func_called == 1

m = my.load_or_do('number.pickle', calc_big)
assert func_called == 1
assert n == m
```

My maybe:
```python
from my import maybe

s = '12'
n = maybe(int)(s)      # 12
sq = maybe(square)(n)  # 144

s = 'foo'
n = maybe(int)(s)      # None (ValueError suppressed)
sq = maybe(square)(n)  # None
```

My `math`:

```python
from my import math

math.sin(math.pi / 4) == math.dsin(45)   # True
math.r(90) == math.pi / 2                # True
```

My `rot13`:

```python
from my import rot13

rot13('abzABZ 123') == 'nomNOM 123'
```

My `acquire_gil` (only available on certain platforms):

```python
from my import acquire_gil

acquire_gil(2)  # Acquires the GIL and holds it for 2 seconds
```

My `jupyter` widgets:

```python
from my import jupyter

# in a Jupyter cell
l = jupyter.Leafer(range(10,20,3)); l()

# in another cell
[l.data[i] for i in l.marked_idxs]
```

My `pandas` `DataFrame` accessor `Q` (just a shorthand for `query`):

```python
>>> import pandas as pd
>>> import my
>>> df = pd.DataFrame([[0,1],[2,3]], columns=['A','B'])
>>> a = 2
>>> df.Q['A == @a']
    A  B
 1  2  3
```

