Instance: Amoxicillin-ratiopharm-750mg-Film-coated-tablet-EE-I
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(Amoxicillin-ratiopharm-750mg-Film-coated-tablet-EE-MPD)
* for[+] = Reference(Amoxicillin-ratiopharm-750mg-Film-coated-tablet-EE-MID)
* for[+] = Reference(AdministrableProductDefinition/Amoxicillin-ratiopharm-750mg-Film-coated-tablet-EE-APD)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092629 "AMOXICILLIN TRIHYDRATE"
* substance.strength.presentationRatio.numerator = 861 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091596 "Amoxicillin"

* substance.strength.referenceStrength.strengthRatio.numerator = 750 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"