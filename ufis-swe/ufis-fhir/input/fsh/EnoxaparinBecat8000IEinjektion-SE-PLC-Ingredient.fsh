Instance: EnoxaparinBecat8000IEinjektion-SE-PLC-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(EnoxaparinBecat8000IEinjektion-SE-PLC-MedicinalProductDef)
* for[+] = Reference(EnoxaparinBecat8000IEinjektion-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(EnoxaparinBecat8000IEinjektion-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090152 "Enoxaparin sodium"


* substance.strength.concentrationRatio.numerator = 8000 https://spor.ema.europa.eu/v1/lists/100000110633#100000110671 "international unit(s)"
* substance.strength.concentrationRatio.denominator = 0.8 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000085598 "Enoxaparin"

* substance.strength.referenceStrength.strengthRatio.numerator = 8000 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "international unit(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 0.8 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"