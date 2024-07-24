# setuptools+pip-example

To build the docker image, run:
```bash
docker buildx build -f Dockerfile -t 'python-namespaced-packages-examples/setuptools+pip-example:$(git rev-parse HEAD)' .
```
