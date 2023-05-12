#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Ensure only executable if not imported
    """
    tab = " " * 4
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    all_logs = list(nginx_collection.find())
    log_count = nginx_collection.estimated_document_count()
    print("{} logs".format(log_count))
    print("Methods:")
    get_docs = nginx_collection.count_documents({"method": "GET"})
    post_docs = nginx_collection.count_documents({"method": "POST"})
    put_docs = nginx_collection.count_documents({"method": "PUT"})
    patch_docs = nginx_collection.count_documents({"method": "PATCH"})
    delete_docs = nginx_collection.count_documents({"method": "DELETE"})
    get_status_docs = nginx_collection.count_documents({"method": "GET",
                                                        "path": "/status"})
    print("\tmethod GET: {}".format(get_docs).expandtabs(4))
    print("\tmethod POST: {}".format(post_docs).expandtabs(4))
    print("\tmethod PUT: {}".format(put_docs).expandtabs(4))
    print("\tmethod PATCH: {}".format(patch_docs).expandtabs(4))
    print("\tmethod DELETE: {}".format(delete_docs).expandtabs(4))
    print("{} status check".format(get_status_docs))
    # for log in all_logs:
    #     print(f"{log}")
