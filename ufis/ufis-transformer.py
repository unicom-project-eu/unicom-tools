import requests
from os import listdir
import json
import re

# FOLDER = "ee-PPLCreator-v2/fhir-data/fsh-generated/resources"
FOLDER = "./ufis-fsh/input/fsh/instances"

for file in listdir(FOLDER):
    print(file)
    res = file.split("-")[-1].split(".")[0]
    print(res)

    resname = file.rsplit("-", 1)[0]
    print(resname)
    with open(FOLDER + "/" + file) as f:
        contents = f.read()
        #   print(contents)

        contents = contents.replace("$220000000060_1", "$220000000060")

        contents = contents.replace("$200000000004_1", "$200000000004")
        contents = contents.replace("$100000000004_1", "$100000000004")
        contents = contents.replace("$100000072051_1", "$100000072051")
        contents = contents.replace("$100000000002_1", "$100000000002")
        contents = contents.replace("$100000072049_1", "$100000072049")
        contents = contents.replace("$200000000014_1", "$200000000014")
        contents = contents.replace("$100000093533_1", "$100000093533")
        contents = contents.replace("$100000072050_1", "$100000072050")
        contents = contents.replace("$100000154441_1", "$100000154441")
        contents = contents.replace("$100000154442_1", "$100000154442")
        contents = contents.replace("$100000072052_1", "$100000072052")

        contents = contents.replace("$100000073345_1", "$100000073345")
        contents = contents.replace("$atc_1", "$atc")
        contents = contents.replace("$SubstanceDefinition_1", "$SubstanceDefinition")

        contents = contents.replace("[0].", "[+].")

        if '.coding.code = "' in contents:  ###gofsh error?
            contents = re.sub(
                r'.coding.code = "(\w+)"', r".coding.code = #\1", contents
            )
        if ".amount.code = " in contents:  ###gofsh error?
            contents = re.sub(
                r'.amount.code = "(\w+)"', r".amount.code = #\1", contents
            )
        if ".code = " in contents:  ###gofsh error?
            contents = re.sub(r'.code = "(\w+)"', r".code = #\1", contents)

        if "InstanceOf: MedicinalProductDefinition" in contents:
            #    print("yes")
            contents = contents.replace(
                "InstanceOf: MedicinalProductDefinition",
                "InstanceOf: PPLMedicinalProductDefinition",
            )
            contents = contents.replace(
                "name.countryLanguage.country",
                "name.usage.country",
            )
            contents = contents.replace(
                "name.countryLanguage.language",
                "name.usage.language",
            )
            contents = contents.replace(
                "name.namePart",
                "name.part",
            )
        if (
            'extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"'
            in contents
        ):
            if "extension.valueCoding " in contents:
                contents = contents.replace(
                    "extension.valueCoding", "combinedPharmaceuticalDoseForm"
                )

        if "InstanceOf: Ingredient" in contents:
            #    print("yes")
            contents = contents.replace(
                "InstanceOf: Ingredient",
                "InstanceOf: PPLIngredient",
            )
            contents = contents.replace(
                '* role = $100000072072#100000072072 "Active"',
                '* role = $100000072050#100000072072 "Active"',
            )
        if "InstanceOf: ManufacturedItemDefinition" in contents:
            #   print("yes")
            contents = contents.replace(
                "InstanceOf: ManufacturedItemDefinition",
                "InstanceOf: PPLManufacturedItemDefinition",
            )

        if "InstanceOf: PackagedProductDefinition" in contents:
            #   print("yes")
            contents = contents.replace(
                "InstanceOf: PackagedProductDefinition",
                "InstanceOf: PPLPackagedProductDefinition",
            )
            contents = contents.replace(
                "package.package",
                "packaging.packaging",
            )
            contents = contents.replace(
                "package.",
                "packaging.",
            )

            contents = contents.replace(
                '* packaging.type.coding.code = "100000073498"',
                "* packaging.type.coding.code = #100000073498",
            )

        if (
            'extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"'
            in contents
        ):
            if "extension.valueQuantity" in contents:
                contents = contents.replace(
                    "extension.valueQuantity", "containedItemQuantity"
                )
        if (
            'extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity'
            in contents
        ):
            if "extension.valueQuantity" in contents:
                contents = contents.replace(
                    "extension.valueQuantity", "containedItemQuantity"
                )
        if "InstanceOf: RegulatedAuthorization" in contents:
            #   print("yes")
            contents = contents.replace(
                "InstanceOf: RegulatedAuthorization",
                "InstanceOf: PPLRegulatedAuthorization",
            )

            contents = contents.replace(
                '* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber',
                '* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber',
            )
        f = open("ufis-fhir/input/fsh/" + file, "w")
        f.write(contents)
        f.close()
