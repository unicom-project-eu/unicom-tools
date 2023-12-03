Instance: MetforminActavis-850mg-Tablet-SE-BS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(MetforminActavis-850mg-Tablet-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(MetforminActavis-850mg-Tablet-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(MetforminActavis-850mg-Tablet-SE-BS-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091366 "Metformin hydrochloride"
* substance.strength.presentationRatio.numerator = 850 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000085448 "Metformin"

* substance.strength.referenceStrength.strengthRatio.numerator = 663 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"