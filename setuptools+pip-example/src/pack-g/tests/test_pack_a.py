from myorg.pack_a.mymodule import a_hello_world


def test_package():
    assert a_hello_world() == "Hello world from package A!"
