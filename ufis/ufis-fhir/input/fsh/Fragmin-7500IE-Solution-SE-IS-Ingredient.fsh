Instance: Fragmin-7500IE-Solution-SE-IS-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-27T11:14:35.37+00:00"
* status = #active
* for[0] = Reference(Fragmin-7500IE-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Fragmin-7500IE-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/Fragmin-7500IE-Solution-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091301 "dalteparin sodium"


* substance.strength.concentrationRatio.numerator = $100000000008#100000165006 "quantity sufficient"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000127573 "dalteparin"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 7500 http://spor.ema.europa.eu/v1/lists/100000110633#100000110671 "international unit(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"