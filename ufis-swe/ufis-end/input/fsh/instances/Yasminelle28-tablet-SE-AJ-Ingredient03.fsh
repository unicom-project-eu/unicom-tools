Instance: Yasminelle28-tablet-SE-AJ-Ingredient03
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(Yasminelle28-tablet-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Yasminelle28-tablet-SE-AJ-ManufacturedItemDefinition01)
* for[+] = Reference(AdministrableProductDefinitionYasminelle28-tablet-SE-AJ-AdministrableProductDefinition01)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092375 "drospirenone"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 3 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition_1#100000092375 "drospirenone"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 3 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"