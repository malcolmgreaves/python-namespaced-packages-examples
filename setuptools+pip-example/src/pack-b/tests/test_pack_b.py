from myorg import pack_a
from myorg.pack_b import hello_world


def test_package():
    assert hello_world() == "Hello world from package B!"
    assert pack_a.hello_world() == "Hello world from package A!"
