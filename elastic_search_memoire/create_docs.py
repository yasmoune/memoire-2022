from elasticsearch import Elasticsearch
from elasticsearch import helpers

import pandas as pd

df = pd.read_csv("./csv_files/areas.csv")


es = Elasticsearch("http://localhost:9200", timeout=80)
# print(es.info().body)

def doc_generator():
  df_iter = df.iterrows()
  for index, line in df_iter:
        yield {
                  "_index": 'area1',
                    "_id" : f"{index}",
                  "_source": { 
                        "coordinates": 
                        {"x": line["Row"], 
                        "y":  line["Column"]},
                        "centroid": line["centroid"],
                        "polygon": line["radius"], 
                        "healthcare": [], 
                        "charging_station": [],
                        "restaurant":[]
              }}             

helpers.bulk(es, doc_generator())