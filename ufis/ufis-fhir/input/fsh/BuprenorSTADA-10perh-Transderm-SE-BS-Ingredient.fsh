Instance: BuprenorSTADA-10perh-Transderm-SE-BS-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-09T09:17:44.143+00:00"
* status = #active
* for[0] = Reference(BuprenorSTADA-10perh-Transderm-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(BuprenorSTADA-10perh-Transderm-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/BuprenorSTADA-10perh-Transderm-SE-BS-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000085263 "Buprenorphine"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000166092 "microgram(s)/hour"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002134 "patch"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000085263 "Buprenorphine"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000166092 "microgram(s)/hour"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002134 "patch"