# Problem-Solving-with-Python-37-Edition

Fork of the [git repo](https://github.com/ProfessorKazarinoff/Problem-Solving-with-Python-37-Edition.git) for the book: Problem Solving with Python 3.7 Edition by Peter D. Kazarinoff, PhD

A print copy of the book is available on Amazon: [https://www.amazon.com/dp/1693405415](https://www.amazon.com/dp/1693405415)


This fork is an experimental repo to see how easy it is to serve a jupyter book as a docker image.  To run:

1) install docker and docker-compose (with the wls2 backend if you are on windows)
2) open a unix shell
3) clone this repository  (do this from unix, not windows)

        git clone https://github.com/phaustin/Problem-Solving-with-Python-37-Edition.git

4) change to the book folder and switch to branch `jb`

        cd Problem-Solving-with-Python-37-Edition
        git checkout -b jb origin/jb


5) at the prompt, type:

        docker-compose up

6) if this succeeds, you should see two containers running when you do:

        docker ps

7) The container `phaustin/base_pangeo` is running a jupyter notebook server on port 9500
   and the container `phaustin/webserver_intropy` is running an apache webserver on port 8500


8) Log into the container to build the book:

        docker exec -it base_pangeo bash

   you should see a prompt that looks like:

        jovyan@4466eaec6c1f:~$

   which means that you're now user jovyan in the container.  To build the book:

        jb build notebooks

   and you should see new files appear in the `notebooks/_build/html` folder

   type `Ctrl-d` to quit the container


9) To see the text of the jupyter-book, point your web browser at `localhost:8500`

10) To access the notebooks, point your web browser at `localhost:9500` and enter the password: `friend` at in the password box on that page.

11) to remove all volumes and containers do:

       bash bringdown.sh

12) to remove all images do:

       docker rmi $(docker images -q)

