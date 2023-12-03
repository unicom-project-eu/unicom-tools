Instance: BuprenorSTADA-10perh-Transderm-SE-BS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(BuprenorSTADA-10perh-Transderm-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(BuprenorSTADA-10perh-Transderm-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(BuprenorSTADA-10perh-Transderm-SE-BS-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000085263 "Buprenorphine"
* substance.strength.presentationRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000166092 "microgram(s)/hour"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002134 "patch"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000085263 "Buprenorphine"

* substance.strength.referenceStrength.strengthRatio.numerator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000166092 "microgram(s)/hour"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002134 "patch"