Instance: Xylocain-WOP-2-Gel-SE-AJ-Ingredient
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(Xylocain-WOP-2-Gel-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Xylocain-WOP-2-Gel-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinitionXylocain-WOP-2-Gel-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090563 "lidocaine hydrochloride monohydrate"


* substance.strength.concentrationRatio.numerator = 21.33 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"
* substance.strength.referenceStrength[+].substance.concept = $SubstanceDefinition#100000139489 "lidocaine hydrochloride"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength[=].strengthRatio.numerator = 20 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength[=].strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"
* substance.strength.referenceStrength[+].substance.concept = $SubstanceDefinition#100000091713 "lidocaine"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength[=].strengthRatio.numerator = 17.31 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength[=].strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"