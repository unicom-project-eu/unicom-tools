import requests
from os import listdir
import json


# FOLDER = "ee-PPLCreator-v2/fhir-data/fsh-generated/resources"
# FOLDER = "ee-PPLCreator-v3/fhir-data/fsh-generated/resources"
# FOLDER = "pt-PPLCreator/fhir-data/fsh-generated/resources"
FOLDER = "ufis/ufis-fhir/fsh-generated/resources"

SERVER = "http://fhir.hl7.pt:8080/fhir/"
# SERVER = "https://jpa.unicom.datawizard.it/fhir/"

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
f = open("validation_output.txt", "w")
f.write("starting...\n")
f.close()
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
                    x = requests.put(
                        SERVER + "/" + res + "/" + _id, json=item["resource"]
                    )
                    # print(x.status_code)
                    if x.status_code == 400:
                        print(res)
                        print(x.text)
            else:
                f = open(FOLDER + "/" + file)
                data = json.load(f)
                id_ = data["id"]
                x = requests.put(SERVER + "/" + res + "/" + id_, json=data)
                # print(x.status_code)
                if x.status_code == 400:
                    errors += 1
                    print(res)
                    print(x.text)
                    f = open("validation_output.txt", "a")
                    f.write(res)
                    f.write("\n")
                    f.write(file)
                    f.write("\n")
                    f.write(x.text)
                    f.write("\n")
                    f.close()

print("errors", errors)
