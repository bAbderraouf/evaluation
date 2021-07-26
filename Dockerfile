FROM python:3.8-slim-buster
COPY /eval.py /opt
WORKDIR /opt

RUN apt update -y && apt upgrade -y && \
    apt install openssh-client -y && apt install openssh-server -y && \
    apt install nmap -y && apt install git -y && \
    pip3 install paramiko && pip3 install python-nmap 
ENTRYPOINT ["python3" , "eval.py"]

