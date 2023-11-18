Instance: IMAgrindeks-100mg-Capsule-SE-IS-Ingredient
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(IMAgrindeks-100mg-Capsule-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(IMAgrindeks-100mg-Capsule-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/IMAgrindeks-100mg-Capsule-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091825 "Imatinib mesilate"
* substance.strength.presentationRatio.numerator = 119.5 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091894 "Imatinib"

* substance.strength.referenceStrength.strengthRatio.numerator = 100 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"