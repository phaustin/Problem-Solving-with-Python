# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="paustin@eoas.ubc.ca"

USER $NB_UID

WORKDIR $HOME

ADD requirements.txt $HOME

# Install Python 3 packages
RUN conda install --quiet --yes \
    'pip' \
    'xarray' \
    'zarr' \
    && \
    conda clean --all -f -y \
    && \
    pip install -r requirements.txt

USER $NB_UID

