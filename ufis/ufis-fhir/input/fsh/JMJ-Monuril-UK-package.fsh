Instance: JMJ-Monuril-UK-package
InstanceOf: PPLPackagedProductDefinition

* name = "Monuril 3g granules for solution; pack of 1 sachet"
* packageFor = Reference(JMJ-Monuril-product-example)
* status = $publication-status#active "Active"
* statusDate = "2022-02-21"
* containedItemQuantity.value = 1
* legalStatusOfSupply.code.coding[0] = $legal-status-of-supply#100000072084 "Medicinal product subject to medical prescription"
* legalStatusOfSupply.code.coding[+] = $100000072051#100000072084 "Medicinal product subject to medical prescription"
* marketingStatus.country.coding[0] = urn:iso:std:iso:3166#GB "United Kingdom of Great Britain and Northern Ireland"
* marketingStatus.country.coding[+] = $100000000002#100000000556 "United Kingdom of Great Britain and Northern Ireland"
//DUMMY
* marketingStatus.status.coding[0] = $100000072052#100000072083 "Marketed"
* marketingStatus.status.coding[+] = $100000072052#100000072083 "Marketed"
* marketingStatus.dateRange.start = "1994-03-18"
* packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding[=].code = #100000073498
* packaging.type.coding[=].display = "Box"
* packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding[=].code = #100000073498
* packaging.type.coding[=].display = "Box"
* packaging.quantity = 1
* packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/JMJ-Monuril-UK-manufacturedItem-example"
//DUMMY
* description = "dummy"