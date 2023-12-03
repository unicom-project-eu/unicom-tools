Instance: Losec-10mg-Tablet-SE-BS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(Losec-10mg-Tablet-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(Losec-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(Losec-10mg-Tablet-SE-BS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000085918 "Omeprazole magnesium"
* substance.strength.presentationRatio.numerator = 10.3 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092047 "Omeprazole"

* substance.strength.referenceStrength.strengthRatio.numerator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"