Instance: Sendolor-1mgml-InfSolution-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(Sendolor-1mgml-InfSolution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073870 "Solution for infusion"
* producedFrom = Reference(Sendolor-1mgml-InfSolution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073572 "Epidural use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073608 "Intrathecal use"