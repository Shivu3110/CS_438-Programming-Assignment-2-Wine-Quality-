# Dockerfile, Image, Container
FROM openjdk:8-jre-slim
FROM python:3.10
RUN apt-get update
RUN apt-get install default-jdk -y
RUN set -ex && \
    apt-get update && \
    pip install numpy && \
    pip install pandas && \
    pip install sklearn && \
    pip install pyspark

RUN mkdir /winequalitypredict
ENV PROG_DIR /winequalitypredict
COPY test.py /winequalitypredict/
COPY ValidationDataset.csv /winequalitypredict/
COPY RandomForestModel.model /winequalitypredict/

ENV PROG_NAME test.py
ADD ${PROG_NAME} .

ENTRYPOINT ["spark-submit","test.py"]
CMD ["ValidationDataset.csv"]