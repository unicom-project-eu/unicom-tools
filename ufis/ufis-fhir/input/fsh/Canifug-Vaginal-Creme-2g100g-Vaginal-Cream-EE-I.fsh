Instance: Canifug-Vaginal-Creme-2g100g-Vaginal-Cream-EE-I
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(Canifug-Vaginal-Creme-2g100g-Vaginal-Cream-EE-MPD)
* for[+] = Reference(Canifug-Vaginal-Creme-2g100g-Vaginal-Cream-EE-MID)
* for[+] = Reference(AdministrableProductDefinition/Canifug-Vaginal-Creme-2g100g-Vaginal-Cream-EE-APD)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092074 "CLOTRIMAZOLE"
* substance.strength[+].concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength[=].concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength[=].concentrationRatio.numerator = 2 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength[=].concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"
* substance.strength[+].presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength[=].presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength[=].presentationRatio.numerator = 40 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength[=].presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002156 "Tube"