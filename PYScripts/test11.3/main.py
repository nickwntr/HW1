
import inspect


def introspect(obj):
    info = {
        'type' : None,
        'attributes' : [],
        'methods' : [],
        'module' : None
    }
    info['type'] = type(obj).__name__
    for key,value in inspect.getmembers(obj):
        if  '__main__' in str(value) and '__module__' in key:
            info['module'] = value
            continue
        if inspect.isroutine(value):
            info['methods'].append(key)
            continue
        else: info['attributes'].append(key)
    return info


print(introspect("22"))
testList=[1,5,1,87,3]
print(introspect(22))
print(introspect(testList))
print(introspect(introspect))

