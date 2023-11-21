Instance: Valocordin-Diazepam-10mg-1ml-Oral-drops-solution-EE-I
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(Valocordin-Diazepam-10mg-1ml-Oral-drops-solution-EE-MPD)
* for[+] = Reference(Valocordin-Diazepam-10mg-1ml-Oral-drops-solution-EE-MID)
* for[+] = Reference(Valocordin-Diazepam-10mg-1ml-Oral-drops-solution-EE-APD)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092362 "DIAZEPAM"
* substance.strength[+].presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength[=].presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength[=].presentationRatio.numerator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength[=].presentationRatio.denominator = 28 https://spor.ema.europa.eu/v1/lists/200000000014#200000002121 "Drop"
* substance.strength[+].concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength[=].concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength[=].concentrationRatio.numerator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength[=].concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"