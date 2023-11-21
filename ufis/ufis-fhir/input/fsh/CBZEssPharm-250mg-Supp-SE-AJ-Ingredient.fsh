Instance: CBZEssPharm-250mg-Supp-SE-AJ-Ingredient
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(CBZEssPharm-250mg-Supp-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(CBZEssPharm-250mg-Supp-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(CBZEssPharm-250mg-Supp-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092127 "Carbamazepine"
* substance.strength.presentationRatio.numerator = 250 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002149 "Suppository"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092127 "Carbamazepine"

* substance.strength.referenceStrength.strengthRatio.numerator = 250 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#200000002149 "Suppository"