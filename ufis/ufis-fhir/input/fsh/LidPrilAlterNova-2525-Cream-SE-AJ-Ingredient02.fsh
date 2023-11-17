Instance: LidPrilAlterNova-2525-Cream-SE-AJ-Ingredient02
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-06T09:17:38.137+00:00"
* status = #active
* for[0] = Reference(LidPrilAlterNova-2525-Cream-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(LidPrilAlterNova-2525-Cream-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinitionLidPrilAlterNova-2525-Cream-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092015 "Prilocaine"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.concentrationRatio.numerator = 25 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092015 "Prilocaine"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 25 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"