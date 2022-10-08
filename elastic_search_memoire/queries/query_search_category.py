from elasticsearch import Elasticsearch
import requests

es = Elasticsearch("http://localhost:9200", timeout=30)
# es =  Elasticsearch([{'host': "localhost", 'port':9200, 'scheme': 'http'}]) 

print(es.info())


url = "http://localhost:9200/area1/_search"

#Query to search  docs where there are pharmacy
data = {
  "query": {
    "nested": {
      "path": "healthcare",
      "query": {
            "bool": {
              "must": [
                { "match": { "healthcare.category": "Pharmacie" } }
              ]
            }
          }
        }
      }
}

response  = requests.get(url, json = data)

print(response.json())


# es.indices.put_settings(index="area1", body={
#     "index.mapping.total_fields.limit": 100000
# })