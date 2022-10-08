from elasticsearch import Elasticsearch
import requests

es = Elasticsearch("http://localhost:9200", timeout=30)

print(es.info())


url_1 = "http://localhost:9200/area1/_search"


data1 = {
  "query": {
    "terms": {
      "_id": [ "10127"] 
    }
  }
}

response  = requests.get(url_1, json = data1)

print(response.json())


# es.indices.put_settings(index="area1", body={
#     "index.mapping.total_fields.limit": 100000
# })