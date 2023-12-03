Instance: Voxra-300mg-Tablet-SE-BS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(Voxra-300mg-Tablet-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(Voxra-300mg-Tablet-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(Voxra-300mg-Tablet-SE-BS-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090431 "Bupropion hydrochloride"
* substance.strength.presentationRatio.numerator = 300 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000002152 "tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000088891 "Bupropion"

* substance.strength.referenceStrength.strengthRatio.numerator = 260.4 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000002152 "tablet"