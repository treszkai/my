# My Python utilities

The standard `pickle` module of Python expects a file object as an argument, not a filename. Let's make life convenient `\o/` 

For now, `my` package contains:
 - `my.dump(obj, filename)`, to Pickle dump an object to a file, specified by a filename
 - `my.load(filename)`, to Pickle load an object from a file, specified by a filename

```python
import my

shrugs = r'¯\_(ツ)_/¯'
my.dump(shrugs, 'shrugs.pickle')
x = my.load('shrugs.pickle')
assert x == shrugs
```
