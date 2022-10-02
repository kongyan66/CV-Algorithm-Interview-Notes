from xml.etree.ElementTree import ProcessingInstruction


def a():
    a = 289
    b = 289
    print(a is b)
    print(id(a))
    print(id(b))

a()