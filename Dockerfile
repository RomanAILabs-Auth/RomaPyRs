FROM rust:1.70-slim-buster

RUN apt-get update && apt-get install -y python3-pip
RUN pip install astunparse

WORKDIR /app
COPY . .
RUN pip install .

CMD ["romapyrs", "--help"]
