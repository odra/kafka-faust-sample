
Sample code to illustrate how to run kafa and faust.

## Usage

Start the local development bu running `docker-compose up` or `podman-compose up`, all container images are public.

You can run `docker exec -it kafka-admin /bin/bash` to "ssh" into the container and run the following command to send messages:

```
# ctrl+c will stop the process
/usr/local/kafka/bin/kafka-console-producer.sh \
--broker-list \
kafka-broker:9092 \
--topic org.fedoraproject.prod.techtalk.message
> {"text": "hello"}
> {"text": "hello"}
> ^C
```

You can either check the `faust-app` logs or run the following command to consume messages from the parsed topic:

```
/usr/local/kafka/bin/kafka-console-consumer.sh \
--bootstrap-server kafka-broker:9092 \
--topic org.fedoraproject.prod.techtalk.message.parsed \
--from-beginning
^C
```

## References

* Faust docs: https://faust.readthedocs.io/en/latest/
* Kafka Quickstart: https://kafka.apache.org/quickstart
* Kafka docs: https://kafka.apache.org/documentation/#introduction

## License

MIT (see LICENSE file)
