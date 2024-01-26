Instance: Smofkabiven-Emulsion-SE-IS-PackagedProductDefinition02
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-29T06:44:56.851+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* extension.valueQuantity = 3 http://spor.ema.europa.eu/v1/lists/200000000014#200000002143 "Sachet"
* packageFor = Reference(Smofkabiven-Emulsion-SE-IS-MedicinalProductDefinition)
* description = "Trekammarpåse, 4 x 1477 ml (Biofine)"
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
* package.shelfLifeStorage[0].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* package.shelfLifeStorage[=].type.coding.code = "100000073403"
* package.shelfLifeStorage[=].type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* package.shelfLifeStorage[=].periodDuration.value = 2
* package.shelfLifeStorage[=].periodDuration.unit = "years"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[0].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.code = "100000073410"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.display = "Do not store above 25 °C"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.code = "100000073421"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.display = "Store in the original package"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.code = "100000073420"
* package.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.display = "Do not freeze"
* package.shelfLifeStorage[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* package.shelfLifeStorage[=].type.coding.code = "100000073405"
* package.shelfLifeStorage[=].type.coding.display = "Shelf life after dilution or reconstitution according to directions"
* package.shelfLifeStorage[=].periodDuration.value = 24
* package.shelfLifeStorage[=].periodDuration.unit = "hours"
* package.shelfLifeStorage[=].specialPrecautionsForStorage.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage[=].specialPrecautionsForStorage.coding.code = "100000073414"
* package.shelfLifeStorage[=].specialPrecautionsForStorage.coding.display = "Store in a refrigerator (2°C – 8°C)"
* package.package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.type.coding.code = "100000073540"
* package.package.type.coding.display = "Pouch"
* package.package.quantity = 1
* package.package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material.coding.code = "200000003208"
* package.package.material.coding.display = "Plastic"
* package.package.package.type.coding[0].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.package.type.coding[=].code = "100000075664"
* package.package.package.type.coding[=].display = "Administration system"
* package.package.package.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.package.type.coding[=].code = "100000073493"
* package.package.package.type.coding[=].display = "Bag"
* package.package.package.quantity = 1
* package.package.package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.package.material.coding.code = "200000003208"
* package.package.package.material.coding.display = "Plastic"
* package.package.package.package[0].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.package.package[=].type.coding.code = "200000002143"
* package.package.package.package[=].type.coding.display = "Sachet"
* package.package.package.package[=].quantity = 1
* package.package.package.package[=].material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.package.package[=].material.coding.code = "200000003208"
* package.package.package.package[=].material.coding.display = "Plastic"
* package.package.package.package[=].containedItem.item.reference.reference = "ManufacturedItemDefinition/Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition"
* package.package.package.package[=].containedItem.amount.value = 750
* package.package.package.package[=].containedItem.amount.code = "100000110655"
* package.package.package.package[=].containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* package.package.package.package[=].containedItem.amount.unit = "milligram(s)"
* package.package.package.package[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.package.package[=].type.coding.code = "200000002143"
* package.package.package.package[=].type.coding.display = "Sachet"
* package.package.package.package[=].quantity = 1
* package.package.package.package[=].material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.package.package[=].material.coding.code = "200000003208"
* package.package.package.package[=].material.coding.display = "Plastic"
* package.package.package.package[=].containedItem.item.reference.reference = "ManufacturedItemDefinition/Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition"
* package.package.package.package[=].containedItem.amount.value = 281
* package.package.package.package[=].containedItem.amount.code = "100000110655"
* package.package.package.package[=].containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* package.package.package.package[=].containedItem.amount.unit = "milligram(s)"
* package.package.package.package[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.package.package[=].type.coding.code = "200000002143"
* package.package.package.package[=].type.coding.display = "Sachet"
* package.package.package.package[=].quantity = 1
* package.package.package.package[=].material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.package.package[=].material.coding.code = "200000003208"
* package.package.package.package[=].material.coding.display = "Plastic"
* package.package.package.package[=].containedItem.item.reference.reference = "ManufacturedItemDefinition/Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition"
* package.package.package.package[=].containedItem.amount.value = 446
* package.package.package.package[=].containedItem.amount.code = "100000110655"
* package.package.package.package[=].containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* package.package.package.package[=].containedItem.amount.unit = "milligram(s)"