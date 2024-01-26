#!/usr/bin/env python3
'''11-schools_by_topic'''


def schools_by_topic(mongo_collection, topic):
    '''This script returns the list of
    school having a specific topic'''
    list_ = mongo_collection.find({"topics": topic})
    return list_
