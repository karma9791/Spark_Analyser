import json

from source.utils.timestamp_utils import long_to_datetime

with open("../resources/sparkEvent1") as f:
    startTime = None
    endTime = None
    for line in f:

        event = json.loads(line)
        event_type = event["Event"]

        if event_type == "SparkListenerApplicationStart":
            print("App Name = ", event["App Name"])
            print("App ID = ", event["App ID"])
            print("startTime = ", long_to_datetime(int(event["Timestamp"])))
            startTime = event["Timestamp"]

        if event_type == "SparkListenerApplicationEnd":
            print("startTime = ", long_to_datetime(int(event["Timestamp"])))
            endTime = event["Timestamp"]

    timediff = endTime - startTime
    print("time taken by job = ", timediff/1000)

