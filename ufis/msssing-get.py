import os
import json

list_of_resources = [
    "AtomoxetinMylan-100mg-Capsule-SE-AJ-AdministrableProductDef",
    "TrimonilR-400mg-PRTablet-SE-AJ-AdministrableProductDefinition",
    "Fragmin-18000IE-Solution-SE-IS-AdministrableProductDefinition",
    "Xylocain-100mgml-cutspray-SE-AJ-AdministrableProductDefinition",
    "BupTest-2mg-Tablet-SE-BS-AdministrableProductDef",
    "Triolif-Mint-Lozenge-SE-AJ-AdministrableProductDefinition",
    "TrimonilR-150mg-PRTablet-SE-AJ-AdministrableProductDefinition",
    "AtomoxetinMedValley-10mg-Capsule-SE-AJ-AdministrableProductDef",
    "Smofkabiven-Emulsion-SE-IS-AdministrableProductDefinition",
    "Xylocain-WOP-10mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "Yasminelle28-tablet-SE-AJ-AdministrableProductDefinition01",
    "Xylocard-20mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "Fragmin-10000IE-Solution-SE-IS-AdministrableProductDefinition",
    "Triolif-HonLem-Lozenge-SE-AJ-AdministrableProductDefinition",
    "AtomoxetinActavis-18mg-Capsule-SE-AJ-AdministrableProductDef",
    "Xylocain-Dental-Adrenalin-SE-AJ-AdministrableProductDefinition",
    "Fragmin-2500IEml-Solution-SE-IS-AdministrableProductDefinition",
    "TegretolR-200mg-PRTablet-SE-AJ-AdministrableProductDefinition",
    "Zeldox20mgml2-SE-PLC-AdminProductDef",
    "Bamyl500mgtablett-SE-PLC-AdminProductDef",
    "Attentin-10mg-Tablet-SE-AJ-AdministrableProductDefinition",
    "Yasminelle-tablet-SE-AJ-AdministrableProductDefinition01",
    "AtomoxetinActavis-10mg-Capsule-SE-AJ-AdministrableProductDef",
    "LidoAcc-20mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "Xylocain-10mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "Lido4-Fluor25-EyeDropsSol-SE-AJ-AdministrableProductDefinition",
    "LidokainAgu-20mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "AtomoxetinMylan-10mg-Capsule-SE-AJ-AdministrableProductDef",
    "Tapin-2525-Cream-SE-AJ-AdministrableProductDefinition",
    "Tegretol-200mg-Tablet-SE-AJ-AdministrableProductDefinition",
    "ISOsandoz-20mg-Capsule-SE-IS-AdministrableProductDefinition",
    "DZPorifarm-10mg-Solution-SE-IS-AdministrableProductDefinition",
    "AtomoxetinGlenmark-10mg-Capsule-SE-AJ-AdministrableProductDef",
    "Xyloproct-RectalOintment-SE-AJ-AdministrableProductDefinition",
    "LidokainAgu-10mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "LidPrilAlterNova-2525-Cream-SE-AJ-AdministrableProductDefinition",
    "Fragmin-7500IE-Solution-SE-IS-AdministrableProductDefinition",
    "Fragmin-10000IEml-Solution-SE-IS-AdministrableProductDefinition",
    "CBZEssPharm-250mg-Supp-SE-AJ-AdministrableProductDefinition",
    "Fragmin-12500IE-Solution-SE-IS-AdministrableProductDefinition",
    "Trombyl160mgtablett-SE-PLC-AdminProductDef",
    "TegretolR-400mg-PRTablet-SE-AJ-AdministrableProductDefinition",
    "Yaz-0023mg-tablet-SE-AJ-AdministrableProductDefinition01",
    "Xylocain-2-Gel-SE-AJ-AdministrableProductDefinition",
    "Fragmin-5000IE-Solution-SE-IS-AdministrableProductDefinition",
    "Fragmin-2500IE-Solution-SE-IS-AdministrableProductDefinition",
    "DZPorifarm-5mg-Solution-SE-IS-AdministrableProductDefinition",
    "Tegretol-100mg-Tablet-SE-AJ-AdministrableProductDefinition",
    "Xylocain-20mgml-InjSol-SE-AJ-AdministrableProductDefinition",
    "Tegretol-20mgml-Suspension-SE-AJ-AdministrableProductDefinition",
    "Tegretol-400mg-Tablet-SE-AJ-AdministrableProductDefinition",
    "Xylo10-Adr5-InjSol-SE-AJ-AdministrableProductDefinition",
    "AMLkrka-10mg-Tablet-SE-IS-AdministrableProductDefinition",
    "CefuroximMIP-1500mg-Powder-SE-IS-AdministrableProductDefinition",
    "TrimonilR-200mg-PRTablet-SE-AJ-AdministrableProductDefinition",
    "Tapin-2525-Plaster-SE-AJ-AdministrableProductDefinition",
    "Xylocain-WOP-2-Gel-SE-AJ-AdministrableProductDefinition",
    "Triolif-Orange-Lozenge-SE-AJ-AdministrableProductDefinition",
    "Fragmin-15000IE-Solution-SE-IS-AdministrableProductDefinition",
    "Aspirin500mgtablett-SE-PLC-AdminProductDef",
    "Fragmink-10000IE-Solution-SE-IS-AdministrableProductDefinition",
    "LidoMylan-10mgml-InjSol-SE-AJ-AdministrableProductDefinition",
]


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
                        print(i["resource"]["resourceType"])
                        if i["resource"]["id"] in list_of_resources:
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
with open("output_missing.json", "w") as file:
    json.dump(administrable_product_definitions, file)
