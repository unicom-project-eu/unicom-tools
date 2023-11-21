import os
import json
import xml.etree.ElementTree as ET
import xmltodict

administrable_product_definitions = []


def prettify(element):
    from xml.dom import minidom

    rough_string = ET.tostring(element, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def get_administrable_product_definitions(directory):
    administrable_product_definitions = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xml"):
                print(file)
                file_path = os.path.join(root, file)
                tree = ET.parse(file_path)
                root_element = tree.getroot()
                # print(root_element)
                namespaces = {"fhir": root_element.tag.split("}")[0].strip("{")}

                for entry in root_element.findall(".//fhir:entry", namespaces):
                    print(entry)
                    res_element = entry.find(".//fhir:resource", namespaces)
                    print(res_element)
                    adm = entry.find(
                        ".//fhir:AdministrableProductDefinition", namespaces
                    )
                    if adm is not None:
                        adm_dict = xmltodict.parse(ET.tostring(adm, encoding="utf-8"))

                        administrable_product_definitions.append(adm_dict)
                    # print(adm)
                    # administrable_product_definitions.append(
                    #      ET.tostring(adm, encoding="unicode")
                    #  )

    return administrable_product_definitions


directory = "../../source-data/ufis/submitted-UFIS/v5.0.0-snapshot1/"
administrable_product_definitions = get_administrable_product_definitions(directory)
print(administrable_product_definitions)
with open("output.json", "w") as file:
    json.dump(administrable_product_definitions, file)
