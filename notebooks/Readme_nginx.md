# nginx javascript issue

* The project:

  I want to build a docker image that runs 5 different services on localhost

  1. a webserver to serve a jupyter-book
  2. a dask cluster scheduler
  3. a dask cluster worker
  4. a jupyterlab server
  5. a jupyter notebook server

I've got all of these containers building and running sucessfully, but I've hit an issue with the nginx web server.

* The problem:
  
  - here's what I want to see: [kite apache version](https://clouds.eos.ubc.ca/~phil/docs/problem_solving/04-Data-Types-and-Variables/04.05-Dictionaries-and-Tuples.html) -- notice the copy icon in the rhs of the code box.
  - here's what I see on localhost:  [nginx localhost](local_host_trouble.png)
   
  - i.e. -- something's wrong with the javascript/css for the copybutton, which I think is loaded here:


        html/04-Data-Types-and-Variables/04.05-Dictionaries-and-Tuples.html
        14:    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css" />
        25:    <script src="../_static/copybutton.js"></script>
        331:            &copy; Copyright 2020.<br/>


  - Does this have something to do with ssl/https?  The javascript is actually working (code is copied to clipboard on click).  It also looks fine when you just open the html files with chrome.  The nginx.conf I'm using is:  [nginx.conf](https://github.com/phaustin/Problem-Solving-with-Python-37-Edition/blob/with_html/notebooks/docker_webserver/nginx.conf) and here is the [docker-compose.yml](https://github.com/phaustin/Problem-Solving-with-Python-37-Edition/blob/with_html/notebooks/docker-compose.yml)

* to reproduce:

  1. `git clone https://github.com/phaustin/Problem-Solving-with-Python-37-Edition.git`
  2. then build and run the image:

          cd Problem-Solving-with-Python-37-Edition/notebooks
          git checkout with_html
          docker-compose up
          
      the book should be up on localhost:9800

* I have no problem switching to another webserver if that fixes this.


