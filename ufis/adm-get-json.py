import os
import json


def get_administrable_product_definitions(directory):
    administrable_product_definitions = {
        "resourceType": "Bundle",
        "id": "27ffa04e9b47c89fcff2850f0962d2dd8986b7e75cf16ba121a8c271810357b4",
        "type": "collection",
        "entry": [],
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                print(file)
                file_path = os.path.join(root, file)
                f = open(file_path)

                try:
                    # returns JSON object as
                    # a dictionary
                    data = json.load(f)

                    # Iterating through the json
                    # list
                    for i in data["entry"]:
                        if (
                            i["resource"]["resourceType"]
                            == "AdministrableProductDefinition"
                        ):
                            administrable_product_definitions["entry"].append(i)
                            # print(i)
                except:
                    print("error on ", file_path)
                    pass
                # Closing file
                f.close()
    return administrable_product_definitions


directory = "../../source-data/ufis/submitted-UFIS/v5.0.0-snapshot1/"
administrable_product_definitions = get_administrable_product_definitions(directory)
print(administrable_product_definitions)
with open("output.json", "w") as file:
    json.dump(administrable_product_definitions, file)
