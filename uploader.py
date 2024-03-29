import requests
from os import listdir
import json


# FOLDER = "ee-PPLCreator-v2/fhir-data/fsh-generated/resources"
# FOLDER = "ee-PPLCreator-v3/fhir-data/fsh-generated/resources"
FOLDER = "pt-PPLCreator/fhir-data/fsh-generated/resources"
FOLDER = "ufis/ufis-fhir/fsh-generated/resources"

filename = FOLDER.split("/")[0]

SERVER = "http://fhir.hl7.pt:8787/fhir/"
# SERVER = "https://jpa.unicom.datawizard.it/fhir/"
# SERVER = "https://server.fire.ly/r5"

blacklist_ids = [
    "JMJ-Co-amoxiclav-product-example",
    "JMJ-Humalog-Kwikpen-product-example",
    "JMJ-Humalog-Mix50-Kwikpen-product-example",
    "JMJ-Monuril-product-example",
    "d37bfa6f-ea90-4645-8be4-e7c649dd64f2",
    "bb8c2306-04c5-42df-94c9-aa6d6e68050b",
    "7f81d47e-9a74-44b3-8ed7-07990093d878",
]
ORDER_LIST = [
    "Organization",
    "MedicinalProductDefinition",
    "ManufacturedItemDefinition",
    "RegulatedAuthorization",
    "AdministrableProductDefinition",
    "Ingredient",
    "PackagedProductDefinition",
    "Bundle",
]
errors = 0
f = open(filename + "_validation_output.txt", "w")
f.write("starting...\n")
f.close()

headers = {"Content-Type": "application/json"}
s = requests.session()
s.headers = {"Accept": "application/fhir+json", "Content-Type": "application/fhir+json"}
for item in ORDER_LIST:
    for file in listdir(FOLDER):
        #   print(file)
        res = file.split("-")[0]
        if res == item:
            if res == "Bundle":
                f = open(FOLDER + "/" + file)
                data = json.load(f)
                for item in data["entry"]:
                    #    print(item["resource"])
                    res = item["resource"]["resourceType"]
                    _id = item["resource"]["id"]
                    x = s.put(
                        SERVER + "/" + res + "/" + _id,
                        json=item["resource"],
                        headers=headers,
                    )
                    # print(x.status_code)

            else:
                f = open(FOLDER + "/" + file)
                data = json.load(f)
                id_ = data["id"]
                if id_ in blacklist_ids:
                    continue
                x = s.put(SERVER + "/" + res + "/" + id_, json=data, headers=headers)
            #  print(x.status_code)
            #  print(x.text)
            if x.status_code not in [200, 201]:
                errors += 1
                print(res)
                print(x.status_code)
                print(x.text)
                f = open(filename + "_validation_output.txt", "a")
                f.write(res)
                f.write("\n")
                f.write(file)
                f.write("\n")
                f.write(x.text)
                f.write("\n")
                f.close()

print("errors", errors)
