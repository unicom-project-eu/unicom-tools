Instance: Diclofenac-Mylan-180mg-Medicated-plaster-EE-I
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(Diclofenac-Mylan-180mg-Medicated-plaster-EE-MPD)
* for[+] = Reference(Diclofenac-Mylan-180mg-Medicated-plaster-EE-MID)
* for[+] = Reference(AdministrableProductDefinition/Diclofenac-Mylan-180mg-Medicated-plaster-EE-APD)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000085789 "Diclofenac epolamine"
* substance.strength.presentationRatio.numerator = 180 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002140 "Plaster"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092272 "Diclofenac sodium"

* substance.strength.referenceStrength.strengthRatio.numerator = 140 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002140 "Plaster"