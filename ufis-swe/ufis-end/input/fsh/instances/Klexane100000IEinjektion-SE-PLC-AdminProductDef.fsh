Instance: Klexane100000IEinjektion-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(Klexane100000IEinjektion-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Klexane100000IEinjektion-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073633 "Subcutaneous use"