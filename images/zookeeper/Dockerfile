FROM quay.io/centos/centos:stream9

ENV JAVA_HOME=/usr/lib/jvm/java-openjdk

RUN yum install -y \
	java-1.8.0-openjdk \
	java-1.8.0-openjdk-devel \
	java-1.8.0-openjdk-headless

RUN mkdir -p /usr/local/zookeeper /var/lib/zookeeper

ADD https://dlcdn.apache.org/zookeeper/zookeeper-3.7.0/apache-zookeeper-3.7.0-bin.tar.gz apache-zookeeper-3.7.0-bin.tar.gz

RUN tar -zxvpf apache-zookeeper-3.7.0-bin.tar.gz && \
mv apache-zookeeper-3.7.0-bin/* /usr/local/zookeeper && \
rm apache-zookeeper-3.7.0-bin.tar.gz

ENTRYPOINT ["/usr/local/zookeeper/bin/zkServer.sh"]

CMD ["--config", "/etc/zookeeper",  "start-foreground"]
