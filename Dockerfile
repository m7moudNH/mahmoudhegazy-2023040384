FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip

WORKDIR /app

COPY hello.py .

RUN pip3 install pandas

CMD ["python3", "hello.py"]
