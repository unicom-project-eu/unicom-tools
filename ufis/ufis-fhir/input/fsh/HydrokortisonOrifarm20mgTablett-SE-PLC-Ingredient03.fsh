Instance: HydrokortisonOrifarm20mgTablett-SE-PLC-Ingredient03
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(HydrokortisonOrifarm20mgTablett-SE-PLC-MedicinalProductDef)
* for[+] = Reference(HydrokortisonOrifarm20mgTablett-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/HydrokortisonOrifarm20mgTablett-SE-PLC-AdminProductDef)
* role = $100000072050#100000072082 "Excipient"
* substance.code.concept = $SubstanceDefinition#100000129311 "Granulated lactose monohydrate"
* substance.strength.concentrationRatio.numerator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"

                //DUMMY

* substance.strength.concentrationRatio.denominator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)" 