Instance: EMLA-2525-Plaster-SE-AJ-PackagedProductDefinition02
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-09T14:19:33.524+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* extension.valueQuantity = 20 http://spor.ema.europa.eu/v1/lists/200000000014#200000002140 "Plaster"
* packageFor = Reference(EMLA-2525-Plaster-SE-AJ-MedicinalProductDefinition)
* description = "Påse, 20 x 1 plåster"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"
* marketingStatus.country = $100000000002#100000000535 "Sweden"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.type.coding.code = "100000073498"
* package.type.coding.display = "Box"
* package.quantity = 1
* package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.material.coding.code = "200000003529"
* package.material.coding.display = "Cardboard"
* package.shelfLifeStorage.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* package.shelfLifeStorage.type.coding.code = "100000073403"
* package.shelfLifeStorage.type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* package.shelfLifeStorage.periodDuration.value = 2
* package.shelfLifeStorage.periodDuration.code = "200000003434"
* package.shelfLifeStorage.periodDuration.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* package.shelfLifeStorage.periodDuration.unit = "Year"
* package.shelfLifeStorage.specialPrecautionsForStorage[0].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = "100000073411"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not store above 30 °C"
* package.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = "100000073420"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not freeze"
* package.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = "100000073419"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not refrigerate"
* package.package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.type.coding.code = "100000073550"
* package.package.type.coding.display = "Single-dose container"
* package.package.quantity = 20
* package.package.material[0].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003208"
* package.package.material[=].coding.display = "Plastic"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003200"
* package.package.material[=].coding.display = "Aluminium"
* package.package.containedItem.item.reference.reference = "ManufacturedItemDefinition/EMLA-2525-Plaster-SE-AJ-ManufacturedItemDefinition"
* package.package.containedItem.amount.value = 1
* package.package.containedItem.amount.code = "200000002140"
* package.package.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* package.package.containedItem.amount.unit = "plaster"