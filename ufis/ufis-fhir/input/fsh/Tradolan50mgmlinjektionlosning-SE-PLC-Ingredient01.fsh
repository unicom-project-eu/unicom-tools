Instance: Tradolan50mgmlinjektionlosning-SE-PLC-Ingredient01
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-24T16:05:46.654+00:00"
* status = #active
* for[0] = Reference(Tradolan50mgmlinjektionlosning-SE-PLC-MedicinalProductDef)
* for[+] = Reference(Tradolan50mgmlinjektionlosning-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/Tradolan50mgmlinjektionlosning-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000093275 "Tramadol hydrochloride"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.concentrationRatio.numerator = 50 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000077198 "Tramadol"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 44 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"