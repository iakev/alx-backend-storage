# alx-backend-storage - NoSQL

## Introduction

This section of the **alx-backend-storage** repository contains a collection of NoSQL database queries and operations. NoSQL databases are known for their flexibility and scalability, making them suitable for various applications, including handling large volumes of unstructured data, real-time data processing, and more.

Explore the programs and scripts in this section to learn and practice NoSQL database interactions.

## Program Descriptions

1. [0-list_databases](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/0-list_databases): Python script to list all databases in a MongoDB server.
2. [1-use_or_create_collection](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/1-use_or_create_collection): Python script to create or access a MongoDB collection.
3. [2-insert](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/2-insert): Python script to insert documents into a MongoDB collection.
4. [3-all](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/3-all): Python script to list all documents in a MongoDB collection.
5. [4-match](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/4-match): Python script to list documents that match specific criteria in a MongoDB collection.
6. [5-count](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/5-count): Python script to count the number of documents in a MongoDB collection that match specific criteria.
7. [6-update](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/6-update): Python script to update documents in a MongoDB collection.
8. [7-delete](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/7-delete): Python script to delete documents from a MongoDB collection.
9. [8-all](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/8-all.py): Python script to list all documents from a MongoDB collection and return them as a list.
10. [9-insert_school](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/9-insert_school.py): Python script to insert a document into a MongoDB collection representing a school.
11. [10-update_topics](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/10-update_topics.py): Python script to update documents in a MongoDB collection representing schools to include a new topic.
12. [11-schools_by_topic](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/11-schools_by_topic.py): Python script to query MongoDB to find schools that have a specific topic.
13. [12-log_stats](https://github.com/iakev/alx-backend-storage/blob/main/0x01-NoSQL/12-log_stats.py): Python script to parse and analyze logs from a MongoDB collection.

## Compiling and Executing

To run these Python scripts, ensure you have a MongoDB server installed and running. You'll also need the `pymongo` library, which you can install using pip:

```bash
pip install pymongo
```

After installing the required dependencies, you can execute the scripts using a Python interpreter:

```bash
python <script_name.py>
```

Make sure to modify the scripts as needed to match your MongoDB server configuration.

## Resources

For additional learning and reference, explore these resources related to NoSQL databases:

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/): A detailed explanation that covers the fundamentals of NoSQL databases and their use cases.
- [What is NoSQL?](https://riak.com/resources/nosql-databases/): An video explanation that provides an overview of NoSQL databases, their types, and characteristics.
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8): A beginner-friendly video tutorial on working with MongoDB in Python.
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE): Part 2 of a MongoDB tutorial series covering essential operations like inserting, updating, removing, and querying data.
- [Aggregation](https://docs.mongodb.com/manual/aggregation/): MongoDB's official documentation on aggregation, a powerful way to process and transform data.
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/): A comprehensive tutorial on using MongoDB with Python, including examples and code snippets.
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/): MongoDB's official documentation on mongo shell methods, which are useful for interacting with MongoDB from the command line.
- [The mongo Shell](https://docs.mongodb.com/manual/mongo/): MongoDB's official documentation on the mongo shell, a JavaScript interface for MongoDB.

Feel free to explore these resources to deepen your understanding of NoSQL databases, particularly MongoDB, and their integration with Python.

---

This README provides an overview of the NoSQL section in the **alx-backend-storage** repository. Explore the individual scripts for detailed descriptions and examples of NoSQL database operations.
