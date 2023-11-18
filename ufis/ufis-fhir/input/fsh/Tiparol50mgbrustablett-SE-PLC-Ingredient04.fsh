Instance: Tiparol50mgbrustablett-SE-PLC-Ingredient04
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(Tiparol50mgbrustablett-SE-PLC-MedicinalProductDef)
* for[+] = Reference(Tiparol50mgbrustablett-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/Tiparol50mgbrustablett-SE-PLC-AdminProductDef)
* role = $100000072050#100000072082 "Excipient"
* substance.code.concept = $SubstanceDefinition#100000090171 "Dimeticone"
* substance.strength.concentrationRatio.numerator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"

                //DUMMY

* substance.strength.concentrationRatio.denominator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)" 