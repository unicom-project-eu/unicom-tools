Instance: AtomoxetinActavis-18mg-Capsule-SE-AJ-Ingredient
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(AtomoxetinActavis-18mg-Capsule-SE-AJ-MedicinalProductDef)
* for[+] = Reference(AtomoxetinActavis-18mg-Capsule-SE-AJ-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinitionAtomoxetinActavis-18mg-Capsule-SE-AJ-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000137397 "Atomoxetine hydrochloride"
* substance.strength.presentationRatio.numerator = 20.57 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002113 "Capsule"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000090524 "Atomoxetine"

* substance.strength.referenceStrength.strengthRatio.numerator = 18 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002113 "Capsule"