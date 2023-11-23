Instance: JMJ-Humalog-Mix50-Kwikpen-package
InstanceOf: PPLPackagedProductDefinition

* name = "Humalog Mix50 100 units/ml KwikPen, suspension for injection in a pre-filled pen; pack of 5 3ml pens"
* packageFor = Reference(JMJ-Humalog-Mix50-Kwikpen-product-example)
* status = $publication-status#active "Active"
* statusDate = "2022-04-27"
* containedItemQuantity.value = 5
* legalStatusOfSupply.code.coding[0] = $legal-status-of-supply#100000072084 "Medicinal product subject to medical prescription"
* legalStatusOfSupply.code.coding[+] = $100000072051#100000072084 "Medicinal product subject to medical prescription"
* marketingStatus.country.coding[0] = urn:iso:std:iso:3166#GB "United Kingdom of Great Britain and Northern Ireland"
* marketingStatus.country.coding[+] = $100000000002#100000000556 "United Kingdom of Great Britain and Northern Ireland"
//DUMMY
* marketingStatus.status.coding[0] = $100000072052#100000072083 "Marketed"
* marketingStatus.status.coding[+] = $100000072052#100000072083 "Marketed"
* marketingStatus.dateRange.start = "1996-04-30"
* packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding[=].code = #100000073498
* packaging.type.coding[=].display = "Box"
* packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding[=].code = #100000073498
* packaging.type.coding[=].display = "Box"
* packaging.quantity = 1
* packaging.packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding[=].code = #?
* packaging.packaging.type.coding[=].display = "Pre-filled pen"
* packaging.packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding[=].code = #100000073543
* packaging.packaging.type.coding[=].display = "Pre-filled pen"
* packaging.packaging.quantity = 5
* packaging.packaging.containedItem.item.reference = Reference(JMJ-Humalog-Kwikpen-manufacturedItem-example)
* packaging.packaging.containedItem.amount.value = 3
* packaging.packaging.containedItem.amount.code = #MilliLiter
* packaging.packaging.containedItem.amount.system = "http://unitsofmeasure.org"
* packaging.packaging.containedItem.amount.unit = "mL"
//DUMMY
* description = "dummy"