import os

import my


def test_pickling():
    shrugs = r'¯\_(ツ)_/¯'
    filename = 'shrugs.pickle'

    try:
        os.remove(filename)
    except OSError:
        pass

    my.dump(shrugs, filename)
    x = my.load(filename)
    assert x == shrugs

    os.remove(filename)

def test_load_or_do():
    obj = []
    elem = 0

    def func():
        obj.append(elem)
        return obj

    filename = 'obj.pickle'

    try:
        os.remove(filename)
    except OSError:
        pass

    obj2 = my.load_or_do(filename, func)
    assert obj == [elem], 'func was not called'
    assert obj2 is obj, 'obj was not returned properly'

    obj3 = my.load_or_do(filename, func)
    assert obj3 == [elem], 'obj was not saved or loaded properly'
    assert obj3 is not obj
 
    os.remove(filename)
