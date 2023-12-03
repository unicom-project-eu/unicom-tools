Instance: DicTratiopharma25mgFilmtablet-SE-PLC-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(DicTratiopharma25mgFilmtablet-SE-PLC-MedicinalProductDef)
* for[+] = Reference(DicTratiopharma25mgFilmtablet-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(DicTratiopharma25mgFilmtablet-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092368 "Diclofenac potassium"
* substance.strength.presentationRatio.numerator = 25 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092798 "Diclofenac"

* substance.strength.referenceStrength.strengthRatio.numerator = 22.1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"