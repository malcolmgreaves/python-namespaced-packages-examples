FROM python:3.10.13-slim

## Installing dependencies and tools
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        python3-setuptools python3-dev build-essential \
        wget vim tree && \
    rm -rf /var/lib/apt/lists/*

# install dependencies first
WORKDIR /build

# Workaround for gitlab CI's limitation in overriding WORKDIR and not allowing builds to specify the mount point:
# https://docs.gitlab.com/ee/ci/docker/using_docker_images.html#where-scripts-are-executed
ENV WORKDIR "/install/infra-bionemo/"
WORKDIR "${WORKDIR}"

RUN pip install -r requirements-dev.txt
RUN pip install -r requirements-test.txt
RUN pip install -r requirements.txt

# install project code
COPY . /install/infra-bionemo
# NOTE: --no-deps because the dependeices come from requirements.txt, which are already installed in a previous layer
RUN pip install --no-deps -e .
