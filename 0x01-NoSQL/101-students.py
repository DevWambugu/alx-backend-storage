#!/usr/bin/env python3
'''101-students'''


def top_students(mongo_collection):
    '''returns all students sorted by average score'''
    students_result = mongo_collection.aggregate([
        {"$project": {
        "name": "$name",
        "averageScore": {"$avg": "$topics.score"}
    }},
        {"$sort": {"averageScore": -1}}
    ])


    return students_result
