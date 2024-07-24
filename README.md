# python-namespaced-packages-examples
Examples of Python projects using PEP-420 namespace packages.


All examples implement the same namespaced package structure.
Each example only differs in the build tools that are used.
Each build tool is a PEP 517+518 compliant build backend.

## Namespaced Project Stucture

The entire namespaced package structure is:

- `pack_a` is an orphan
- `pack_b` depends only on `myorg.pack_a`
- `pack_c` depends only on `myorg.pack_b`
- `pack_d` is an orphan
- `pack_e` depends on `pack_a`
- `pack_f` depends on `pack_d` and `pack_e`
- `pack_g` depends on all other packages (`pack_{a,b,c,d,e,f}`)

## Implementations with Different Python Build Tools

### `setuptools` + `pip`
See the example project under the [`setuptools+pip-example/`](./setuptools+pip-example) directory.

### `poetry`
See the example project under the [`poetry-example/`](./poetry-example) directory.
