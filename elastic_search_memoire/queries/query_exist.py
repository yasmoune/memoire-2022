from elasticsearch import Elasticsearch
import requests

es = Elasticsearch("http://localhost:9200", timeout=30)

print(es.info())

url = "http://localhost:9200/area1/_search"
 
data = {
            "query": {
                "bool": {

                "nested": {
                "path": "charging_station",
                "query": {
                            "exists": {
                                    "field": "charging_station"
                                    }
                        }
                    }
                }
            }}


{'query': {
   'bool': {
       'must': [
           {'nested': {
               'path': 'Diagnosis',
               'query': {
                   'bool': {
                       'must': [{'match_phrase': {'Diagnosis.Diagnosis': {'query': "epidemia"}}}]
                   }  
               }
           }},
           {'nested': {
               'path': 'Demographic',
               'query': {
                   'bool': {
                       'must': [{'match_phrase': {'Demographic.Gender': {'query': "female"}}}]
                   }  
               }
           }}
       ]
   }
}}

response  = requests.get(url, json = data)

print(response.json())
