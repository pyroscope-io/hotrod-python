FROM 489437247049.dkr.ecr.us-east-1.amazonaws.com/pyroscope:dev as pyroscope

FROM python:3

COPY . /app/src
WORKDIR /app/src
RUN pip install -r requirements.txt
COPY --from=pyroscope /usr/bin/pyroscope /usr/bin/pyroscope
ENTRYPOINT ["/usr/bin/pyroscope", "exec", "uwsgi", "--ini"]
