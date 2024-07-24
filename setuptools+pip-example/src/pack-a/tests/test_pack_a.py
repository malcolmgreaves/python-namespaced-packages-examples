from myorg.pack_a.mymodule import hello_world


def test_package():
    assert hello_world() == "Hello world from package A!"
