from os import listdir
import hashlib
import re

f = open("ufis-fhir/input/fsh/Organization.fsh", "w")
f.truncate()
f.close()

list_of_locs = []


def create_org(regauth):
    # print(regauth)
    instance_value = re.search(r"Instance:\s*(\S+)", regauth)
    if instance_value:
        value = instance_value.group(1)
    #  print(value)
    ### get loc value
    if "* holder.identifier.value" in regauth:
        loc_value = re.search(r"\* holder.identifier.value = \"(\S+)\"", regauth)
        if loc_value:
            loc = loc_value.group(1)

    #  print(loc)
    else:
        print(
            "no loc --------------------------------------------------------------------------"
        )
        return regauth
    ### get loc value
    if "* holder.display" in regauth:
        disp_value = re.search(r"\* holder.display = \"(.+)\"", regauth)
        if disp_value:
            disp = disp_value.group(1)
            # print(disp)
    else:
        disp = "No name"
    if loc not in list_of_locs:
        f = open("ufis-fhir/input/fsh/Organization.fsh", "a")

        f.write("""Instance:""")
        f.write(" " + loc)
        f.write(
            """\nInstanceOf: PPLOrganization
Usage: #example
Description: "Marketing Authorisation Holder / Organisation"

* identifier[loc].value = """
        )
        f.write('"' + loc + '"\n' + '* name = "' + disp + '"\n\n')
        # f.write(contents)
        f.close()
        list_of_locs.append(loc)

    regauth = re.sub("\* holder.+ = .+\n", "", regauth)
    regauth += "\n* holder = Reference(" + loc + ")\n"
    # print(regauth)

    return regauth


"""

Instance: LOC-100009199-Mip
InstanceOf: PPLOrganization
Usage: #example
Description: "Marketing Authorisation Holder / Organisation"

* identifier[loc].value = "LOC-100009199"
* name = "Mip Pharma GmbH"

"""
# FOLDER = "ee-PPLCreator-v2/fhir-data/fsh-generated/resources"
FOLDER = "./ufis-fsh/input/fsh/instances"

for file in listdir(FOLDER):
    # print(file)
    res = file.split("-")[-1].split(".")[0]
    # print(res)

    resname = file.rsplit("-", 1)[0]
    # print(resname)
    with open(FOLDER + "/" + file) as f:
        contents = f.read()
        #   print(contents)

        # Find the value after "Instance:" using regex
        instance_value = re.search(r"Instance:\s*(\S+)", contents)
        if instance_value:
            value = instance_value.group(1)
            # print("Original value:", value)

            # Check the length of the value
            if len(value) > 64:
                # Generate a hash and replace the value
                hashed_value = hashlib.sha256(value.encode()).hexdigest()
                contents = contents.replace(value, hashed_value)
                # print("Replaced value:", hashed_value)
                # print(contents)
        contents = re.sub(r"\* meta.versionId = \"(\S+)\"", "", contents)
        contents = re.sub(r"\* meta.lastUpdated = \"(.+)\"\n", "", contents)
        contents = contents.replace("$220000000060_1", "$220000000060")

        contents = contents.replace("Usage: #inline\n", "")

        ##non just numeric ids
        contents = re.sub(r"Reference\((\d{3,20})\)\n", r"Reference(j\1) \n", contents)
        contents = re.sub(r"resource = (\d{3,20})\n", r"resource = j\1 \n", contents)
        contents = re.sub(r"Instance: (\d{3,20})\n", r"Instance: j\1 \n", contents)

        # Instance: 20170630100020

        contents = contents.replace(
            '* holder = Reference(1) "Glaxosmithkline Produtos Farmaceuticos Lda."',
            '//DUMMY\n* holder = Reference(LOC-100000549) "Glaxosmithkline Produtos Farmaceuticos Lda."',
        )
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

        ####### Administrable PRODUCT DEFINITION ####################################
        if "InstanceOf: AdministrableProductDefinition" in contents:
            print("yes")
            contents = contents.replace(
                "InstanceOf: AdministrableProductDefinition",
                "InstanceOf: PPLAdministrableProductDefinition",
            )
            print(contents)

            contents = re.sub(
                r"formOf = Reference\(\w+\/(.+)\)",
                r"formOf = Reference(\1)",
                contents,
            )
            contents = re.sub(
                r"producedFrom = Reference\(\w+\/(.+)\)",
                r"producedFrom = Reference(\1)",
                contents,
            )
            # print("Original value:", value)
        # * formOf = Reference(MedicinalProductDefinition/Amlodistad-5mg-Tablet-SE-IS-MedicinalProductDefinition)
        # * administrableDoseForm = $200000000004#100000073664 "Tablet"
        # * producedFrom = Reference(ManufacturedItemDefinition/Amlodistad-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
        ####### MEDICINAL PRODUCT DEFINITION ####################################

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
            contents = contents.replace(
                '* marketingStatus.status.coding[0] = xx#xx "xx"',
                '//DUMMY\n* marketingStatus.status.coding[0] = $100000072052#100000072083 "Marketed"',
            )

            if "* legalStatusOfSupply" not in contents:
                contents += '\n//DUMMY\n* legalStatusOfSupply = $100000072051#100000072084 "Medicinal product subject to medical prescription"'

            if "* domain" not in contents:
                contents += (
                    '\n//DUMMY\n* domain = $100000000004#100000000012 "Human use"'
                )

            if (
                'extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"'
                in contents
            ):
                if "* extension.valueCoding " in contents:
                    contents = contents.replace(
                        "* extension.valueCoding", "* combinedPharmaceuticalDoseForm"
                    )
            if "* combinedPharmaceuticalDoseForm" not in contents:
                contents += '\n//DUMMY\n* combinedPharmaceuticalDoseForm = $200000000004#100000116186 "Powder for solution for injection/infusion"'

            contents = contents.replace(
                """* legalStatusOfSupply.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* legalStatusOfSupply.coding.extension.valueInteger = 1""",
                "",
            )
            contents = contents.replace(
                """* domain.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* domain.coding.extension.valueInteger = 1""",
                "",
            )
            contents = contents.replace(
                """* combinedPharmaceuticalDoseForm.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* combinedPharmaceuticalDoseForm.extension.valueInteger = 1""",
                "",
            )
            contents = contents.replace(
                """* classification[+].coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* classification[=].coding.extension.valueInteger = 1""",
                "",
            )

            contents = contents.replace(
                """* classification[=].coding = $200000000324#200000003517 "Other"\n""",
                """* classification[+].coding = $200000000324#200000003517 "Other"\n""",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"',
                "",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"',
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"\n""",
                "",
            )

            contents = contents.replace(
                """* attachedDocument = Reference(DocumentReference/Curocef1500mgPulver-A-HL-DocumentReference01)
* masterFile = Reference(mfl1)
* contact[+].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* contact[=].type.coding.extension.valueInteger = 1
* contact[=].type.coding = $100000154441#100000155057 "Qualified Person in the EEA for Pharmacovigilance"
* contact[=].contact = Reference(qppv1)
* contact[+].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* contact[=].type.coding.extension.valueInteger = 3
* contact[=].type.coding = $100000154441#200000017719
* contact[=].contact = Reference(phvenq1)""",
                "",
            )
        ####### INGREDIENT ############################################################################################################
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

            contents = contents.replace(
                """* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"\n""",
                "",
            )
            contents = contents.replace(
                """* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"\n""",
                "",
            )

            if "substance.strength" not in contents:
                contents += """\n* substance.strength.concentrationRatio.numerator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"\n
                //DUMMY\n
* substance.strength.concentrationRatio.denominator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)" """

            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"',
                "",
            )
            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"',
                "",
            )
            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000165006 "quantity sufficient"',
                "",
            )
            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000052 "less than or equal to"',
                "",
            )

            contents = contents.replace(
                '* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator""',
                "",
            )
            contents = contents.replace(
                '* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"',
                "",
            )

            contents = contents.replace(
                '* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000051 "more than"',
                "",
            )

            contents = contents.replace(
                '* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"',
                "",
            )

            if (
                "* substance.strength.concentrationRatio.numerator " in contents
                and "* substance.strength.concentrationRatio.denominator"
                not in contents
            ):
                contents += '\n* substance.strength.concentrationRatio[=].denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000025238 "dose"'

            if (
                "* substance.strength.referenceStrength.strengthRatio.numerator "
                in contents
                and "* substance.strength.referenceStrength.strengthRatio.denominator"
                not in contents
            ):
                contents += '\n* substance.strength.referenceStrength.strengthRatio[=].denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000025238 "dose"'

            if (
                '* extension.url = "http://ema.europa.eu/fhir/extension/subject"'
                in contents
            ):
                contents = contents.replace(
                    '* extension.url = "http://ema.europa.eu/fhir/extension/subject"',
                    "",
                )
                # print(contents)
                ref_value = re.search(r"\* extension.valueReference = (.+)", contents)
                if ref_value:
                    ref = ref_value.group(1)
                    contents += "\n* for[+] = " + ref
                # contents = contents.replace("* extension.valueReference", "* for[+]")

                contents = re.sub(r"\* extension.valueReference = (.+)", "", contents)

            contents = re.sub(
                r"Reference\(AdministrableProductDefinition\/(.+)\)",
                r"Reference(\1)",
                contents,
            )

            contents = re.sub(
                r"Reference\(AdministrableProductDefinition(.+)\)",
                r"Reference(\1)",
                contents,
            )
        ####### MANUFACTURED ITEM DEFINITION ############################################################################################################

        if "InstanceOf: ManufacturedItemDefinition" in contents:
            #   print("yes")
            contents = contents.replace(
                "InstanceOf: ManufacturedItemDefinition",
                "InstanceOf: PPLManufacturedItemDefinition",
            )

            if "unitOfPresentation" not in contents:
                contents += '\n//DUMMY\n* unitOfPresentation = $200000000014#200000002152 "Tablet"'

            contents = contents.replace(
                """* unitOfPresentation.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* unitOfPresentation.coding.extension.valueInteger = 1\n""",
                "",
            )

            contents = contents.replace(
                """* manufacturedDoseForm.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* manufacturedDoseForm.coding.extension.valueInteger = 1\n""",
                "",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/subject"', ""
            )
            contents = re.sub(
                r"\* extension.valueReference = Reference\(.+\)", "", contents
            )

        ####### PACKAGED PRODUCT DEFINITION ####################################

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
            if (
                'extension[+].url = "http://ema.europa.eu/fhir/extension/containedItemQuantity'
                in contents
            ):
                if "extension[=].valueQuantity" in contents:
                    contents = contents.replace(
                        "extension[=].valueQuantity", "containedItemQuantity"
                    )
            contents = contents.replace(
                "http://hl7.org/fhir/ValueSet/packaging-type",
                "https://spor.ema.europa.eu/v1/lists/100000073346",
            )

            contents = contents.replace(
                '* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346/terms/100000073498"',
                '* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"',
            )
            contents = contents.replace(
                '* marketingStatus.status.coding[0] = xx#xx "xx"',
                '//DUMMY\n* marketingStatus.status.coding[0] = $100000072052#100000072083 "Marketed"',
            )

            contents = contents.replace(
                '* packaging.packaging.type.coding[=].code = "?"',
                "* packaging.packaging.type.coding[=].code = #?",
            )

            contents = contents.replace(
                """* extension[+].url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension[=].valueQuantity = 6 http://spor.ema.europa.eu/v1/lists/200000000014#200000002137 "Pessary"
* extension[+].url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension[=].valueQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002156 "Tube"\n""",
                """* containedItemQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002156 "Tube"\n""",
            )
            contents = contents.replace(
                '* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"',
                "",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"',
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"\n""",
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072172 "Estonian"\n""",
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072251#100000072251 "Portuguese"\n""",
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072178 "German"\n""",
                "",
            )
            if "* description" not in contents:
                contents += '\n//DUMMY\n* description = "dummy"'

            contents = re.sub(
                r'packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/(.+)"',
                r"packaging.containedItem.item.reference = Reference(\1)",
                contents,
            )
        ####### RegulatedAuthorization ########################################################################

        if "InstanceOf: RegulatedAuthorization" in contents:
            #   print("yes")
            # print(contents)
            contents = contents.replace(
                "InstanceOf: RegulatedAuthorization",
                "InstanceOf: PPLRegulatedAuthorization",
            )

            contents = contents.replace(
                '* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber',
                '* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber',
            )

            if "* identifier" not in contents:
                contents += '\n//DUMMY\n* identifier.value = "dummy"'

            if "* status" not in contents:
                contents += '\n//DUMMY\n* status = $100000072049#200000017708 "Valid - Renewed/Varied"'

            if "* region" not in contents:
                contents += '\n//DUMMY\n* region = $100000000002#100000000388 "Republic of Estonia"'

            contents.replace("$220000000061#220000000061", "$220000000060#220000000061")

            contents = contents.replace(
                '* type = $100000072055#100000072062 "Marketing Authorisation"',
                '* type = $220000000060#220000000061 "Marketing Authorisation"',
            )
            contents = contents.replace(
                '* type = $220000000061#220000000061 "Marketing Authorisation"',
                '* type = $220000000060#220000000061 "Marketing Authorisation"',
            )
            contents = create_org(contents)
        if "InstanceOf: Bundle" in contents:
            contents = contents.replace(
                "* type = #transaction",
                "* type = #collection",
            )
            contents = contents.replace(
                "* entry[=].request.method = #PUT",
                "",
            )
            contents = re.sub(r"\* entry\[=\].request.url = \"(.+)\"", "", contents)

        f = open("ufis-fhir/input/fsh/" + file, "w")
        f.write(contents)
        f.close()
