from elasticsearch import Elasticsearch
import requests

es = Elasticsearch("http://localhost:9200", timeout=30)
# es =  Elasticsearch([{'host': "localhost", 'port':9200, 'scheme': 'http'}]) 

print(es.info())


url_1 = "http://localhost:9200/area1/_search"
# url_1 = "http://localhost:9200/area1"

# data1 = {
#   "query": {
#     "nested": {
#       "path": "healthcare",
#       "query": {
#             "bool": {
#               "must": [
#                 { "match": { "healthcare.category": "Médecin" } },
#                 { "match": { "healthcare.category": "Pharmacie" } }
#               ]
#             }
#           }
#         }
#       }
# }



data1 = {'query': {
                'bool': {
                    'must': [
                        {"nested": {
                        "path": "healthcare",
                        "query": {
                                "bool": {
                                "must": [
                                    { "match": { "healthcare.category": "Cabinet M\u00e9dical et Clinique" } },
                                ]
                                }
                            }
                            }
                        },
                        {"nested": {
                        "path": "healthcare",
                        "query": {
                                "bool": {
                                "must": [
                                    { "match": { "healthcare.category": "Pharmacie" } },
                                ]
                                }
                            }
                            }
                        }
                     
                            ]
                        }
                }
         }



response1  = requests.get(url_1, json = data1)

print(response1.json())


# es.indices.put_settings(index="area1", body={
#     "index.mapping.total_fields.limit": 100000
# })