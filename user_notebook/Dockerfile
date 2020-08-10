# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/base-notebook
FROM $BASE_CONTAINER

LABEL maintainer="paustin@eoas.ubc.ca"

USER $NB_UID

WORKDIR $HOME

# Copy over build files. Unfortunately we can't use $NB_UID/$NB_GID
# in the `--chown` statement, so we need to hardcode these values.
COPY --chown=1000:100 environment_linux.txt requirements_linux.txt postBuild $HOME/

# # Install Python 3 packages
RUN conda install --quiet --yes \
    --file environment_linux.txt \
    && \
    conda clean --all -f -y \
    && \
    pip install -r requirements_linux.txt --upgrade

# Copy local files as late as possible to avoid cache busting
COPY jupyter_notebook_config.py /etc/jupyter/

RUN echo "Checking for 'postBuild'..." \
    && export PATH=${NB_PYTHON_PREFIX}/bin:${PATH} \
    && chmod +x postBuild \
    && echo "running postBuild" \
    && ./postBuild \
    && rm -rf /tmp/* \
    && rm -rf ${HOME}/.cache ${HOME}/.npm ${HOME}/.yarn \
    && rm -rf ${NB_PYTHON_PREFIX}/share/jupyter/lab/staging \
    && find ${CONDA_DIR} -follow -type f -name '*.a' -delete \
    && find ${CONDA_DIR} -follow -type f -name '*.pyc' -delete \
    && find ${CONDA_DIR} -follow -type f -name '*.js.map' -delete 
