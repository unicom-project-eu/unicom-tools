Instance: TramadolRetardActavis100mgdepot-SE-PLC-Ingredient02
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(TramadolRetardActavis100mgdepot-SE-PLC-MedicinalProductDef)
* for[+] = Reference(TramadolRetardActavis100mgdepot-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(TramadolRetardActavis100mgdepot-SE-PLC-AdminProductDef)
* role = $100000072050_1#100000072082 "Excipient"
* substance.code.concept = $SubstanceDefinition_1#100000092393 "Calcium hydrogen phosphate dihydrate"