Instance: Softacort335mgpermlogondroppar-SE-PLC-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-13T15:04:37.619+00:00"
* status = #active
* for[0] = Reference(Softacort335mgpermlogondroppar-SE-PLC-MedicinalProductDef)
* for[+] = Reference(Softacort335mgpermlogondroppar-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/Softacort335mgpermlogondroppar-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000086691 "Hydrocortisone sodium phosphate"


* substance.strength.concentrationRatio.numerator = 3.35 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092635 "Hydrocortisone"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 2.5 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"