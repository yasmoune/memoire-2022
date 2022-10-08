from elasticsearch import Elasticsearch
import requests

es = Elasticsearch("http://localhost:9200", timeout=30)
# es =  Elasticsearch([{'host': "localhost", 'port':9200, 'scheme': 'http'}]) 

print(es.info())


url = "http://localhost:9200/area1"  #area should be replace by the name of the index

response  = requests.delete(url)
