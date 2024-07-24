FROM python:3.10.13-slim

## Installing dependencies and tools
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        python3-setuptools python3-dev build-essential \
        wget vim tree && \
    rm -rf /var/lib/apt/lists/*

# all project-related files live here
WORKDIR /build/

# install testing tools
COPY requirements-test.txt ./
RUN pip install -r requirements-test.txt

# copy project code & build configurations
COPY src/ LICENSE pyproject.toml README.md ./

# build & install all packages => pack_g depends on all of myorg's namespaced packages
WORKDIR /build/src/pack-g
RUN pip install .

WORKDIR /build
