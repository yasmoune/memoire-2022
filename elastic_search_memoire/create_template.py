import requests
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

data = {
  "index_patterns": ["*area*"],
  "template": {
    "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
    },
    "mappings": {
    "properties": {
    "id_df": {
      "type": "integer"
          },
    "polygon": {
        "type": "geo_shape"
            },
    "centroid": {
        "type": "geo_point"
            },
    "coordinates": {
      "type": "nested",
      "properties": {
        "x": {"type":"integer"}, 
        "y":{"type":"integer"}
                    }
                  },
    "healthcare": {
        "type": "nested",
        "properties": 
          {"gps_coordinates": 
            {"type":"geo_point"},
            "category": 
            {"type":"keyword"},
            "name_text":
            {"type":"text"},
            "name_keyword":
            {"type":"keyword"}
          }
        },
    "drinking_water":  {
        "type": "nested",
        "properties": {"gps_coordinates": 
            {"type":"geo_point"}}
                  }, 
    "charging_station":  {
        "type": "nested",
        "properties": {"gps_coordinates": 
            {"type":"geo_point"}}
                  },
    "library": {
        "type": "nested",
        "properties": 
          {"gps_coordinates": 
            {"type":"geo_point"},
            "category": 
            {"type":"keyword"},
            "name_text":
            {"type":"text"},
            "name_keyword":
            {"type":"keyword"}
          }
        },
    }
    }
    },
  "priority": 500
  }

url = "http://localhost:9200/_index_template/template_area"

 
response = requests.post(url, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())