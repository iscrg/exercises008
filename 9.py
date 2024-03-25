import json
import yaml
import xml.etree.ElementTree as ET
import functools


def to_xml(data, root_element="root"):
    def build_element(key, value):
        element = ET.Element(str(key))
        if isinstance(value, (list, tuple)):
            for item in value:
                element.append(build_element("item", item))
        elif isinstance(value, dict):
            for key, value in value.items():
                element.append(build_element(key, value))
        else:
            element.text = str(value)
        return element

    root = build_element(root_element, data)
    return ET.tostring(root, encoding='unicode')


def to_format(datatype):
    def real_decorator(func):
        if datatype is None or datatype == 'json':
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                result = func(*args, **kwargs)
                jsoned = json.dumps(result)
                return jsoned
            return wrapped

        if datatype == 'xml':
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                result = func(*args, **kwargs)
                return to_xml(result)
            return wrapped

        if datatype == 'yaml':
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                result = func(*args, **kwargs)
                yamled = yaml.dump(result, default_flow_style=False)
                return yamled
            return wrapped

    return real_decorator



@to_format(None)
def lst():
    #res = 'qwerty12345'
    #res = [1, 2, 3, 4]
    res = {'a': 1, 'b': 2, 'c':3}
    return res


print(lst())
