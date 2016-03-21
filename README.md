# nifi_spark_streaming_demo

THIS WAS TESTED ON SANDBOX HDP 2.3

1. start kafka in ambari
	a. there is sometimes a glitch will it not show as started
	b. go to the spark configuration settings in ambari
2. under advanced spark-log4j-properties cahnge “log4j.rootCategory” to be equal to “ERROR”
	a. (Re)Start spark
3. start deployment script "SH deployment_script.sh"
4. in sandbox add service, select nifi and next
5. Go with all default options, if errors are on customize services
	a. remove oozie.authentication.kerberos.name.rules with the red button to the right
	b. set the ranger db root password to anything
6. In virtual box go to settings>network>port forwarding and add port 9090 for nifi
7. separately download “streaming_demo.xml” from the repo and upload as a template in nifi
8. start nifi allprocessors, a few aren't configured to work but event gen through hdfs should work
9. start spark streaming with “sh kafka_test.sh”
