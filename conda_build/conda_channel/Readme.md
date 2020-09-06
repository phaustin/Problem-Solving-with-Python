# building a conda package

This container build the recipe in conda_channel/recipe/meta.yaml, which provides the base
jupyter packages for the user notebook

The Dockerfile copies the recipe to /srv/conda_channel and builds the package there.

To start the container to see the build channel

```
docker-compose run -d --name conda conda_build tail -f
docker exec -it conda bash
```

To see the recipe:

```
cat /srv/conda_channel/meta.yaml
```


To get the built package out of the container and uplaod to anaconda:


```
cd /Users/phil/repos/Problem-Solving-with-Python-37-Edition/conda_build
docker cp conda:/srv/conda_channel built_channel
anaconda upload --force /Users/phil/repos/Problem-Solving-with-Python-37-Edition/conda_build/built_channel/noarch/base-notebook-2020.09.05-0.tar.bz2 
```

To use this package to constuct an environment:

```
name: notebook
channels:
  - eoas_ubc
  - conda-forge
  - defaults
dependencies:
  - base-notebook=2020.09.05
  ```

i.e. if that is in environment.yml, then

```
conda-lock -f environment.yml -p linux-64
```

will produce the correct conda-linux-64.lock file




