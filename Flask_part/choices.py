category = {
    "healthcare" : 
        {"name": "Etablissement de santé",
         "category" : ["Clinique", "Pharmacie", "Hopitaux"]
         },
        "charging_station" :
            {"name": "Bornes de chargement", 
            }
            }

total_number = {}
for key, value in category.items() :
    if "category" in value :
        total_number[key] = len(value["category"])
    else :
        total_number[key] = 1

print(total_number)