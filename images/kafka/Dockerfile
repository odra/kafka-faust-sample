FROM quay.io/centos/centos:stream9

ENV JAVA_HOME=/usr/lib/jvm/java-openjdk

RUN yum install -y \
	java-1.8.0-openjdk \
	java-1.8.0-openjdk-devel \
	java-1.8.0-openjdk-headless

RUN mkdir -p /usr/local/kafka /var/lib/kafka

ADD https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz kafka_2.13-3.0.0.tgz

RUN tar -zxvpf kafka_2.13-3.0.0.tgz && \
mv kafka_2.13-3.0.0/* /usr/local/kafka && \
rm kafka_2.13-3.0.0.tgz
