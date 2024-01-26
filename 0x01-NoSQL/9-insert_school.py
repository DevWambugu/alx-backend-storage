#!/usr/bin/env python3
'''9-insert_school'''
def insert_school(mongo_collection, **kwargs):
    '''This function inserts a new
    document in a collection based on kwargs'''
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
