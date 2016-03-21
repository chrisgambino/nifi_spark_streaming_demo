
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="kafkaTest")
ssc = StreamingContext(sc,5)


kvs = KafkaUtils.createStream(ssc, "localhost:2181", "spark_streaming", {"inter_transact": 1})
kvs.pprint(10)



ssc.start()

ssc.awaitTermination()
