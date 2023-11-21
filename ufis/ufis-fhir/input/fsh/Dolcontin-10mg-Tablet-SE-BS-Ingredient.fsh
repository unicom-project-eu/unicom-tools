Instance: Dolcontin-10mg-Tablet-SE-BS-Ingredient
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(Dolcontin-10mg-Tablet-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(Dolcontin-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(Dolcontin-10mg-Tablet-SE-BS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090222 "Morphine sulfate pentahydrate"
* substance.strength.presentationRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091372 "Morphine"

* substance.strength.referenceStrength.strengthRatio.numerator = 7.5 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"