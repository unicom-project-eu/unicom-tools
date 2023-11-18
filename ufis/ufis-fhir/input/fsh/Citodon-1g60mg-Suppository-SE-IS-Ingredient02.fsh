Instance: Citodon-1g60mg-Suppository-SE-IS-Ingredient02
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-20T16:03:19.631+00:00"
* status = #active
* for[0] = Reference(Citodon-1g60mg-Suppository-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Citodon-1g60mg-Suppository-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/Citodon-1g60mg-Suppository-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090188 "Codeine phosphate hemihydrate"


* substance.strength.concentrationRatio.numerator = 60 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000153319 "Codeine anhydrous"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 44.2 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"