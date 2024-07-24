# setuptools+pip-example

To build the docker image, run:
```bash
docker buildx build -f Dockerfile -t python_namespaced_packages_examples_setuptools_pip_example:$(git rev-parse HEAD) .
```

Once built, you can run tests in the image under the `src/pack-g` namespaced package, which includes all other packages.

Open a `bash` interpreter in the built image:
```bash
docker run --rm -it --entrypoint /bin/bash python_namespaced_packages_examples_setuptools_pip_example:$(git rev-parse HEAD)
```

Then, run the tests:
```shell
pushd src/pack-g && pytest -v .
```
