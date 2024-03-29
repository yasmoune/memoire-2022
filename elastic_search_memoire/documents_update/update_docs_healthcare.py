from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pandas as pd


es = Elasticsearch("http://localhost:9200", request_timeout= 30)
print(es.info().body)

# es.indices.put_settings(index="area1", body={
#     "index.mapping.total_fields.limit": 200000
# })

def doc_generator():
  df_iter = df.iterrows()
  for index, line in df_iter:
        yield {
                  "_op_type": "update",
                  "_index": 'area1',
                    "_id" :  line["0"],
                  "script": {
                    "source": "ctx._source.healthcare.addAll(params.healthcare)",
                    "lang": "painless",
                    "params": {
                        "healthcare": [{
                            "gps_coordinates": line["geometry"],
                            "category": line["Type_détaillé"],
                              "name_text": line["name"],
                              "name_keyword": line["name"]
                        }]}                  
              } }   




# def doc_generator():
#   df_iter = df.iterrows()
#   for index, line in df_iter:
#         yield {
#                   "_op_type": "update",
#                   "_index": 'area1',
#                     "_id" :  line["0"],
#                     # "upsert": {
#                     #   "gps_coordinates": line["geometry"],
#                     #     "category": line["Type_détaillé"],
#                     #     "name_text": line["name"],
#                     #     "name_keyword": line["name"]
#                     # },
#                   "doc": { 
#                         "healthcare": [
#                               {
#                               "gps_coordinates": line["geometry"],
#                               "category": line["Type_détaillé"],
#                               "name_text": line["name"],
#                               "name_keyword": line["name"]
#                               }]}
#               }      

for i in [ i * 500 for i in range(60)]:  
  df = pd.read_csv("../csv_files/healthcare_cleaned.csv")[i:i+500]
  df.reset_index(inplace = True)
  helpers.bulk(es, doc_generator())