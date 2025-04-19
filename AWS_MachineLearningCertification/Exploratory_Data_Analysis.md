# EDA

## AWS services that get the data

### Kinesis Data Streams

#### Pros
  - Massively scalable and durable real-time data
  - Continuously capture gigabytes
  - Enables real time analytics

#### Algorithm
*4 key concepts*:
- Producer: Feeds stream. Creates partition key for each chunk of record being fed into the stream.
- Shard: Constituents of stream. Partition keys created by producer determines which shard ingests the record in the stream.
- Consumer: Consumes stream
- Data stream: Grouping of shards (saves for 24hrs/7 days (with extension applied))

*Process*:
- Gets data from producers (e.g social media, hardware, log files)
- Uses shards to stream data to consumers (ec2, lambda funcs)
- consumers can send data to storages/analytics/BAU layer

*Data into streams*:
- API: Amazon Kinesis Producers Library, Amazon Kinesis Agent (Java app installed on servers)

>[!IMPORTANT]
> 1. Shards are append only shards
> 2. 1 shard can ingest 1000 data records per second
> 3. Shard contained order sequence of records ordered by time
> 4. Specify number of shards needed when stream is created
> 5. Can change the number of shards needed dynamically when running via API, lambda, auto-scaling
> 6. Enhanced fan-out: 1mb/sec in for shard, 2mb/sec out for each consumer
> 7. Non enhanced fan out: 1mb/sec in for shard, 2mb/sec out all consumer

### Kinesis Data Firehouse

*Process*:
  - Gets data from producers (e.g social media, hardware, log files)
  - Uses lambda func to ETL
  - lambda can send data to storages/analytics/BAU tools/Storage
  - S3 Event to store to dynamodb

- Kinesis Video stream
  - Gets data from producers (e.g radar, video, web cam)
  - Consumers: Kinesis video streams (ec2 continuous/batch)
  - Sends data to storage S3

- Kinesis Data Analytics
  - Uses sql to process streaming data
  - Sources: Kinesis Data Stream, Kinesis Data Firehose
  - SQL queries put to s3, redshift or BAU tools

