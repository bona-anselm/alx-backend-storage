#!/usr/bin/env python3
""" Defines insert_school """


def insert_school(mongo_collection, **kwargs):
    """ Iinserts a new document in a collection based on kwargs """
    inserted_document = mongo_collection.insert_one(kwargs)
    return inserted_document.inserted_id
