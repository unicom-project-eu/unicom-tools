Instance: ISOorifarm-10mg-Capsule-SE-IS-Ingredient
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(ISOorifarm-10mg-Capsule-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(ISOorifarm-10mg-Capsule-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/ISOorifarm-10mg-Capsule-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000089811 "Isotretinoin"


* substance.strength.concentrationRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000089811 "Isotretinoin"

* substance.strength.referenceStrength.strengthRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"