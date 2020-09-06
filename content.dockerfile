FROM busybox

RUN mkdir -p /srv/problem_solving_content
COPY ./notebooks/ /srv/problem_solving_content

CMD tail -f /dev/null


