FROM phaustin/base-image:sep05

USER ${NB_USER}

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

RUN mkdir -p /srv/conda_channel
COPY conda_channel/recipe/ /srv/conda_channel/
RUN echo "building conda channel" \
   && conda install conda-build conda-verify \
   && cd /srv/conda_channel \
   && conda build --output-folder=. . \
   && conda index .

WORKDIR ${HOME}





