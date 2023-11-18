Instance: DiklofenakTApofri50mgFilmtablet-SE-PLC-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-13T17:34:08.272+00:00"
* status = #active
* for[0] = Reference(DiklofenakTApofri50mgFilmtablet-SE-PLC-MedicinalProductDef)
* for[+] = Reference(DiklofenakTApofri50mgFilmtablet-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/DiklofenakTApofri50mgFilmtablet-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092368 "Diclofenac potassium"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 50 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092798 "Diclofenac"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 44 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"