Instance: Hydrocortisone-DAK-10mg1g-Ointment-EE-I
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-14T19:23:26.922+00:00"
* status = #active
* for[0] = Reference(Hydrocortisone-DAK-10mg1g-Ointment-EE-MPD)
* for[+] = Reference(Hydrocortisone-DAK-10mg1g-Ointment-EE-MID)
* for[+] = Reference(AdministrableProductDefinition/Hydrocortisone-DAK-10mg1g-Ointment-EE-APD)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092635 "Hydrocortisone"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.concentrationRatio.numerator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110654 "gram(s)"