#!/usr/bin/env python3
'''8-all.py'''


def list_all(mongo_collection):
    '''These func lists all documents in a collection'''
    documents = mongo_collection.find({})

    if mongo_collection.count_documents({}) == 0:
        return []
    return list(documents)
