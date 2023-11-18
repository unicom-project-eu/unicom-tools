Instance: Xylocard-20mgml-InjSol-SE-AJ-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-06T10:02:33.941+00:00"
* status = #active
* for[0] = Reference(Xylocard-20mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Xylocard-20mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinitionXylocard-20mgml-InjSol-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090563 "Lidocaine hydrochloride monohydrate"


* substance.strength.concentrationRatio.numerator = 21.3 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength[+].substance.concept = $SubstanceDefinition#100000091713 "Lidocaine"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength[=].strengthRatio.numerator = 17.31 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligarm(s)"
* substance.strength.referenceStrength[=].strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength[+].substance.concept = $SubstanceDefinition#100000139489 "Lidocaine hydrochloride"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength[=].strengthRatio.numerator = 20 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength[=].strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"