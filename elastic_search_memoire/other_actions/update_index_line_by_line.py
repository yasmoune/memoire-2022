import requests
import pandas as pd

#update line by line

df = pd.read_csv("healthcare_tosave.csv")
df_iter = df.iterrows()
for index, line in df_iter:
    url = "http://localhost:9200/area1/_update/{}".format(line["0"])
    print(url)

    data = {
                    "script": {
                        "source": "ctx._source.healthcare.addAll(params.healthcare)",
                        "params": {
                        "healthcare": [{
                            "gps_coordinates": line["geometry"],
                            "category": line["Type_détaillé"],
                              "name_text": line["name"],
                              "name_keyword": line["name"]
                        }]}
                    }
                    }

    response  = requests.post(url, json = data)
    print(response.json())





# url_1 = "http://localhost:9200/area1/_search"

# data1 = {
#   "query": {
#     "terms": {
#       "_id": [ "0" ] 
#     }
#   }
# }

# response1  = requests.get(url_1, json = data1)
# print(response1.json())

