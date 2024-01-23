#!/usr/bin/env python3
'''12-log_stats'''


import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]

all_logs = collection.count_documents({})

print(f"{all_logs} logs")

print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    method_count = collection.count_documents({"method": method})
    print(f"\tmethod {method.upper()}: {method_count}")

status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_count} status check")
