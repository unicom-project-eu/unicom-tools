Instance: BuprenorSTADA-5perh-Transderm-SE-BS-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-08T11:15:12.007+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 12 http://spor.ema.europa.eu/v1/lists/200000000014#200000002134 "Patch"
* packageFor = Reference(BuprenorSTADA-5perh-Transderm-SE-BS-MedicinalProductDefinition)
* description = "Påse, 12 x 1 plåster"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"
* marketingStatus.country = $100000000002#100000000535 "Sweden"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.material.coding.code = #200000003529
* packaging.material.coding.display = "Cardboard"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073547
* packaging.packaging.type.coding.display = "Sachet"
* packaging.packaging.quantity = 12
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003217
* packaging.packaging.material.coding[=].display = "PolyEthylene TerePhthalate"
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003207
* packaging.packaging.material.coding[=].display = "Paper"
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003214
* packaging.packaging.material.coding[=].display = "PolyEthylene"
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003200
* packaging.packaging.material.coding[=].display = "Aluminium"
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000012515
* packaging.packaging.material.coding[=].display = "Ethylene acrylic acid copolymer"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/BuprenorSTADA-5perh-Transderm-SE-BS-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 1
* packaging.packaging.containedItem.amount.code = #200000002134
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633~200000000014"
* packaging.packaging.containedItem.amount.unit = "Patch"