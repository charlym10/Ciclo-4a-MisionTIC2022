from pymongo import MongoClient

from os import environ

url_cluster = environ['URL_CLUSTER']
username = environ['DB_USERNAME']
password = environ['DB_PASSWORD']
database = environ['DATABASE']

client = MongoClient(
    f'mongodb+srv://{username}:{password}@{url_cluster}/{database}?retryWrites=true&w=majority'
)

database = client['Orders_Ciclo4a_MisionTIC22']
