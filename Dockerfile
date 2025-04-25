FROM python:3.12

WORKDIR /app
ADD . /app

ARG requirements=requirements/reqs.txt

RUN pip install --no-cache-dir -r $requirements

CMD uvicorn app:app --host 0.0.0.0 --port 8001 --reload