Instance: BuprenorphineOri-8mg-Tablet-SE-BS-Ingredient
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(BuprenorphineOri-8mg-Tablet-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(BuprenorphineOri-8mg-Tablet-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(BuprenorphineOri-8mg-Tablet-SE-BS-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092032 "Buprenorphine hydrochloride"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 8.64 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition_1#100000085263 "Buprenorphine"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 8 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"