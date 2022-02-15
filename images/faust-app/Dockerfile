FROM quay.io/centos/centos:stream9

RUN yum install -y python3 python3-pip python3-devel nmap-ncat

COPY app /app
RUN pip3 install -r /app/requirements.txt

ENTRYPOINT ["/app/entrypoint"]

WORKDIR /app

