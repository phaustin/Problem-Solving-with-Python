# Problem-Solving-with-Python-37-Edition

This is a fork of the [git repo](https://github.com/ProfessorKazarinoff/Problem-Solving-with-Python-37-Edition.git) for the book: Problem Solving with Python 3.7 Edition by Peter D. Kazarinoff, PhD

If you like this book, please consider purchasing a hard copy version on Amazon: [https://www.amazon.com/dp/1693405415](https://www.amazon.com/dp/1693405415)

The formatted version: https://phaustin.github.io/Problem-Solving-with-Python-37-Edition/

To actually run the notebooks 

1) Install [docker](https://docs.docker.com/get-docker/)

2) checkout the repo on the `with_html` branch to get the rendered book

```
git clone https://github.com/phaustin/Problem-Solving-with-Python-37-Edition.git
cd Problem-Solving-with-Python-37-Edition
git checkout with_html
docker pull phaustin/webserver:aug10
docker pull phaustin/user_notebook:aug11
docker-compose up
```

2) open firefox or chrome and in one tab open:

       localhost:8500

3) Now take a look at your local version of [section 6.1.5](https://phaustin.github.io/Problem-Solving-with-Python-37-Edition/05-NumPy-and-Arrays/05_05-Array-Indexing.html). If you right-click on the rocketship and launch Jupyterhub in a new tab, you will be prompted for a password. Type "friend" (without the quotes) to start a live notebook for that page.


4) To stop and remove all processes, containers and images:

```
bash bringdown.sh
docker rmi $(docker images -q)
``
