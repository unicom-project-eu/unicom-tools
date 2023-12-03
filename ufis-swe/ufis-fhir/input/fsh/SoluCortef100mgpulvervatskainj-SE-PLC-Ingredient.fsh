Instance: SoluCortef100mgpulvervatskainj-SE-PLC-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(SoluCortef100mgpulvervatskainj-SE-PLC-MedicinalProductDef)
* for[+] = Reference(SoluCortef100mgpulvervatskainj-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(SoluCortef100mgpulvervatskainj-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092550 "Hydrocortisone sodium succinate"
* substance.strength.presentationRatio.numerator = 134 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002114 "Cartridge"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092635 "Hydrocortisone"

* substance.strength.referenceStrength.strengthRatio.numerator = 100 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002114 "Cartridge"