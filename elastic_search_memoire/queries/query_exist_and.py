from elasticsearch import Elasticsearch
import requests

es = Elasticsearch("http://localhost:9200", timeout=30)
# es =  Elasticsearch([{'host': "localhost", 'port':9200, 'scheme': 'http'}]) 

print(es.info())


url = "http://localhost:9200/area1/_search"

 
# data = {
#             "query": {
#                 "nested": {
#                 "path": "healthcare",
#                 "query": {
#                             "exists": {
#                                     "field": "healthcare"
#                                     }
#                         }
#                     }
#                 }
#             }

data = {
            "query": {
                "nested": {
                "path": "healthcare",
                "query": {
                           
                        }
                    }
                }
            }

response1  = requests.get(url, json = data)
# response1  = requests.delete(url_1)

print(response1.json())
