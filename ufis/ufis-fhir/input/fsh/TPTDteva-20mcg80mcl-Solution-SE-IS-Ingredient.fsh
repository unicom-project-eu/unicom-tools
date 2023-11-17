Instance: TPTDteva-20mcg80mcl-Solution-SE-IS-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-08T17:35:45.261+00:00"
* status = #active
* for[0] = Reference(TPTDteva-20mcg80mcl-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(TPTDteva-20mcg80mcl-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/TPTDteva-20mcg80mcl-Solution-SE-IS-AdminProdDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000089193 "Teriparatide"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.concentrationRatio.numerator = 0.25 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "milliliter(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000089193 "Teriparatide"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 0.25 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "milliliter(s)"