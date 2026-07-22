FROM python:3.14-slim

WORKDIR /work
COPY pydeps.sh .
RUN sh pydeps.sh

COPY app .

CMD read NONEXISTING