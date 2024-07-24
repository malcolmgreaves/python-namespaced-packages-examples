# setuptools+pip-example

To build the docker image, run:
```bash
docker buildx build -f Dockerfile -t python_namespaced_packages_examples_setuptools_pip_example:$(git rev-parse HEAD) .
```
