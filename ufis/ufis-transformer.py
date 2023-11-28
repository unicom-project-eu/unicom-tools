from os import listdir, mkdir
import hashlib
import re
import shutil

f = open("ufis-fhir/input/fsh/Organization.fsh", "w")
f.truncate()
f.close()

list_of_locs = []

blacklist_ids = [
    "JMJ-Co-amoxiclav-product-example",
    "JMJ-Humalog-Kwikpen-product-example",
    "JMJ-Humalog-Mix50-Kwikpen-product-example",
    "JMJ-Monuril-product-example",
    "d37bfa6f-ea90-4645-8be4-e7c649dd64f2",
    "bb8c2306-04c5-42df-94c9-aa6d6e68050b",  # PT
    "7f81d47e-9a74-44b3-8ed7-07990093d878",
]

target_folder = "ufis-fhir/input/fsh/"
shutil.rmtree(target_folder)
mkdir(target_folder)


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
##TODO
# clean the target folder

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

        #  if any(blacklist_ids in contents):
        #      print(contents)
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
            # print("yes")
            contents = contents.replace(
                "InstanceOf: AdministrableProductDefinition",
                "InstanceOf: PPLAdministrableProductDefinition",
            )
            # print(contents)

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

            contents = contents.replace(
                "http://spor.ema.europa.eu/v1/lists/100000000002",
                "https://spor.ema.europa.eu/v1/lists/100000000002",
            )
            ###language
            contents = contents.replace(
                """* name.usage.language.coding.system = "http://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072288
* name.usage.language.coding.display = "Swedish\"""",
                """* name.usage.language = urn:ietf:bcp:47#sv "Swedish\" """,
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "http://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072172
* name.usage.language.coding.display = "Estonian\"""",
                """* name.usage.language = urn:ietf:bcp:47#et "Estonian\" """,
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057/terms/100000072251"
* name.usage.language.coding.code = "100000072251"
* name.usage.language.coding.display = "Portuguese\"""",
                """* name.usage.language = urn:ietf:bcp:47#pt "Portuguese\" """,
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072178
* name.usage.language.coding.display = "German\"""",
                """* name.usage.language = urn:ietf:bcp:47#de "German\"\n""",
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = "100000072149"
* name.usage.language.coding.display = "Finnish\"""",
                """* name.usage.language = urn:ietf:bcp:47#fi "Finnish\" """,
            )

            contents = contents.replace(
                "https://hl7.org/fhir/publication-status",
                "http://hl7.org/fhir/publication-status",
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
            ###temporarily remove until further notice
            contents = re.sub(
                r"^\* packaging\.shelfLifeStorage.*\n?",
                "",
                contents,
                flags=re.MULTILINE,
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

            # contents = re.sub(
            #     r"\* packaging.shelfLifeStorage\[=\].periodDuration.value = (.+)\n\* packaging.shelfLifeStorage\[=\].periodDuration.unit = \"(.+)\"",
            #     r"\* packaging.shelfLifeStorage\[=\].periodDuration = \1 '\2'",
            #     contents,
            # )

        # blacklist
        bid = False
        for blids in blacklist_ids:
            if "Instance: " + blids in contents:
                print(contents)
                bid = True
        if not bid:
            f = open(target_folder + file, "w")
            f.write(contents)
            f.close()


###aliases
f = open(target_folder + "aliases.fsh", "w")

f.write(
    """Alias: $200000000004~200000000006~200000000007~200000000008 = https://spor.ema.europa.eu/v1/lists/200000000004~200000000006~200000000007~200000000008
Alias: $100000000004 = https://spor.ema.europa.eu/v1/lists/100000000004
Alias: $200000005003 = https://spor.ema.europa.eu/v1/lists/200000005003
Alias: $100000072051 = https://spor.ema.europa.eu/v1/lists/100000072051
Alias: $100000116677 = https://spor.ema.europa.eu/v1/lists/100000116677
Alias: $220000000060 = https://spor.ema.europa.eu/v1/lists/220000000060
Alias: $100000000002 = https://spor.ema.europa.eu/v1/lists/100000000002
Alias: $100000072049 = https://spor.ema.europa.eu/v1/lists/100000072049
Alias: $authorisation-date-type = https://ema.europa.eu/fhir/code-systems/authorisation-date-type
Alias: $100000072057 = https://spor.ema.europa.eu/v1/lists/100000072057
Alias: $100000072052 = https://spor.ema.europa.eu/v1/lists/100000072052
Alias: $200000000004 = https://spor.ema.europa.eu/v1/lists/200000000004
Alias: $200000000014 = https://spor.ema.europa.eu/v1/lists/200000000014

Alias: $100000093533 = https://spor.ema.europa.eu/v1/lists/100000093533

Alias: $authorisationDateType = https://ema.europa.eu/fhir/authorisationDateType


Alias: $100000154442 = https://spor.ema.europa.eu/v1/lists/100000154442
Alias: $100000160962 = https://spor.ema.europa.eu/v1/lists/100000160962
Alias: $100000155526 = https://spor.ema.europa.eu/v1/lists/100000155526
Alias: $100000072050 = https://spor.ema.europa.eu/v1/lists/100000072050 // Ingredient Role
Alias: $SubstanceDefinition = https://spor.azure-api.net/sms/api/v2/SubstanceDefinition
Alias: $100000000008 = https://spor.ema.europa.eu/v1/lists/100000000008
Alias: $atc = https://www.whocc.no/atc
Alias: $200000003186 = https://spor.ema.europa.eu/v1/lists/200000003186
Alias: $publication-status = https://hl7.org/fhir/publication-status
Alias: $additionalMonitoringIndicator = https://ema.europa.eu/fhir/additionalMonitoringIndicator
Alias: $200000000010 = https://spor.ema.europa.eu/v1/lists/200000000010
Alias: $country = https://hl7.org/fhir/ValueSet/country
Alias: $200000000008 = https://spor.ema.europa.eu/v1/lists/200000000008
Alias: $paediatricUseIndicator = https://ema.europa.eu/fhir/paediatricUseIndicator
Alias: $200000000324 = https://spor.ema.europa.eu/v1/lists/200000000324
Alias: $100000116045 = https://spor.ema.europa.eu/v1/lists/100000116045
Alias: $100000154441 = https://spor.ema.europa.eu/v1/lists/100000154441
Alias: $100000160406 = https://spor.ema.europa.eu/v1/lists/100000160406
Alias: $200000004983 = https://spor.ema.europa.eu/v1/lists/200000004983
Alias: $100000155688 = https://spor.ema.europa.eu/v1/lists/100000155688
Alias: $riskOfSupplyShortage = https://ema.europa.eu/fhir/riskOfSupplyShortage
Alias: $200000000007 = https://spor.ema.europa.eu/v1/lists/200000000007
Alias: $100000073345 = https://spor.ema.europa.eu/v1/lists/100000073345
Alias: $200000003554 = https://spor.ema.europa.eu/v1/lists/200000003554
Alias: $medicinal-product-type = https://hl7.org/fhir/medicinal-product-type
Alias: $200000025915 = https://spor.ema.europa.eu/v1/lists/200000025915
Alias: $medicinal-product-domain = https://hl7.org/fhir/medicinal-product-domain
Alias: $legal-status-of-supply = https://hl7.org/fhir/legal-status-of-supply
Alias: $ = https://www.whocc.no/atc_ddd_index/
Alias: $100000072055 = https://spor.ema.europa.eu/v1/lists/100000072055
Alias: $iso3166-1edition2 = https://terminology.hl7.org/CodeSystem/iso3166-1edition2
Alias: $standardterms = https://standardterms.edqm.eu/

Alias: $200000000006 = https://spor.ema.europa.eu/v1/lists/200000000006
Alias: $200000004946 = https://spor.ema.europa.eu/v1/lists/200000004946
Alias: $100000096162 = https://spor.ema.europa.eu/v1/lists/100000093533/terms/100000096162
Alias: $220000000061 = https://spor.ema.europa.eu/v1/lists/220000000060/terms/220000000061
Alias: $100000072251 = https://spor.ema.europa.eu/v1/lists/100000072057/terms/100000072251
Alias: $100000073665 = https://spor.ema.europa.eu/v1/lists/200000000004/terms/100000073665
Alias: $100000072072 = https://spor.ema.europa.eu/v1/lists/100000072050/terms/100000072072


Alias: $100000073345 = https://spor.ema.europa.eu/v1/lists/100000073345
Alias: $200000002152 = https://spor.ema.europa.eu/v1/lists/200000000014/terms/200000002152
Alias: $100000073619 = https://spor.ema.europa.eu/v1/lists/100000073345/terms/100000073619
"""
)
f.close()
