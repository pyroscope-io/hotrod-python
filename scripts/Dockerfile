FROM python:3

RUN pip install requests


WORKDIR /

COPY mock_requests.py mock_requests.py

ENTRYPOINT [ "python", "/mock_requests.py" ]
