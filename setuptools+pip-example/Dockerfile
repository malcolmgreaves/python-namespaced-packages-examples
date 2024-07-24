FROM python:3.10.13-slim

## Installing dependencies and tools
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        python3-setuptools python3-dev build-essential \
        wget vim tree && \
    rm -rf /var/lib/apt/lists/*

# copy project code & build configurations
WORKDIR /build/
COPY src/ LICENSE pyproject.toml README.md ./

# build & install all packages => pack_g depends on all of myorg's namespaced packages
WORKDIR /build/src/pack-g
RUN pip install .
WORKDIR /build
