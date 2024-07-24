from myorg.pack_b.mymodule import hello_world


def test_package():
    assert hello_world() == "Hello world from package B!"
