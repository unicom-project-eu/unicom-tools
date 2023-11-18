Instance: Lido4-Fluor25-EyeDropsSol-SE-AJ-Ingredient01
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-10T17:17:36.723+00:00"
* status = #active
* for[0] = Reference(Lido4-Fluor25-EyeDropsSol-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Lido4-Fluor25-EyeDropsSol-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinitionLido4-Fluor25-EyeDropsSol-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000139489 "Lidocaine hydrochloride"


* substance.strength.concentrationRatio.numerator = 40 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091713 "Lidocaine"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 34.6 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"