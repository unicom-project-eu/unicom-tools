Instance: Tapin-2525-Plaster-SE-AJ-Ingredient02
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(Tapin-2525-Plaster-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Tapin-2525-Plaster-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(Tapin-2525-Plaster-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092015 "Prilocaine"
* substance.strength.presentationRatio.numerator = 25 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002140 "plaster"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092015 "Prilocaine"

* substance.strength.referenceStrength.strengthRatio.numerator = 25 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002140 "plaster"