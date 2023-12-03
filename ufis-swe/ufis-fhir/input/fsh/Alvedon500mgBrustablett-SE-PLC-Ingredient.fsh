Instance: Alvedon500mgBrustablett-SE-PLC-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(Alvedon500mgBrustablett-SE-PLC-MedicinalProductDef)
* for[+] = Reference(Alvedon500mgBrustablett-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(Alvedon500mgBrustablett-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090270 "Paracetamol"
* substance.strength.presentationRatio.numerator = 500 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000090270 "Paracetamol"

* substance.strength.referenceStrength.strengthRatio.numerator = 500 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"