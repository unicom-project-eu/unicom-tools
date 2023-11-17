Instance: Smofkabiven-Emulsion-SE-IS-PackagedProductDefinition04
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-29T06:44:56.892+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 3 http://spor.ema.europa.eu/v1/lists/200000000014#200000002143 "Sachet"
* packageFor = Reference(Smofkabiven-Emulsion-SE-IS-MedicinalProductDefinition)
* description = "Trekammarpåse, 4 x 986 ml (Biofine)"
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
* packaging.shelfLifeStorage[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* packaging.shelfLifeStorage[=].type.coding.code = #100000073403
* packaging.shelfLifeStorage[=].type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* packaging.shelfLifeStorage[=].periodDuration.value = 2
* packaging.shelfLifeStorage[=].periodDuration.unit = "years"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.code = #100000073410
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.display = "Do not store above 25 °C"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.code = #100000073421
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.display = "Store in the original package"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.code = #100000073420
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage[=].coding.display = "Do not freeze"
* packaging.shelfLifeStorage[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* packaging.shelfLifeStorage[=].type.coding.code = #100000073405
* packaging.shelfLifeStorage[=].type.coding.display = "Shelf life after dilution or reconstitution according to directions"
* packaging.shelfLifeStorage[=].periodDuration.value = 24
* packaging.shelfLifeStorage[=].periodDuration.unit = "hours"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage.coding.code = #100000073414
* packaging.shelfLifeStorage[=].specialPrecautionsForStorage.coding.display = "Store in a refrigerator (2°C – 8°C)"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073540
* packaging.packaging.type.coding.display = "Pouch"
* packaging.packaging.quantity = 1
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003208
* packaging.packaging.material.coding.display = "Plastic"
* packaging.packaging.packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.type.coding[=].code = #100000075664
* packaging.packaging.packaging.type.coding[=].display = "Administration system"
* packaging.packaging.packaging.type.coding[+].system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.type.coding[=].code = #100000073493
* packaging.packaging.packaging.type.coding[=].display = "Bag"
* packaging.packaging.packaging.quantity = 1
* packaging.packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.material.coding.code = #200000003208
* packaging.packaging.packaging.material.coding.display = "Plastic"
* packaging.packaging.packaging.packaging[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.packaging[=].type.coding.code = #200000002143
* packaging.packaging.packaging.packaging[=].type.coding.display = "Sachet"
* packaging.packaging.packaging.packaging[=].quantity = 1
* packaging.packaging.packaging.packaging[=].material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.packaging[=].material.coding.code = #200000003208
* packaging.packaging.packaging.packaging[=].material.coding.display = "Plastic"
* packaging.packaging.packaging.packaging[=].containedItem.item.reference.reference = "ManufacturedItemDefinition/Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.packaging.packaging[=].containedItem.amount.value = 500
* packaging.packaging.packaging.packaging[=].containedItem.amount.code = #100000110655
* packaging.packaging.packaging.packaging[=].containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.packaging.packaging[=].containedItem.amount.unit = "milligram(s)"
* packaging.packaging.packaging.packaging[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.packaging[=].type.coding.code = #200000002143
* packaging.packaging.packaging.packaging[=].type.coding.display = "Sachet"
* packaging.packaging.packaging.packaging[=].quantity = 1
* packaging.packaging.packaging.packaging[=].material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.packaging[=].material.coding.code = #200000003208
* packaging.packaging.packaging.packaging[=].material.coding.display = "Plastic"
* packaging.packaging.packaging.packaging[=].containedItem.item.reference.reference = "ManufacturedItemDefinition/Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.packaging.packaging[=].containedItem.amount.value = 188
* packaging.packaging.packaging.packaging[=].containedItem.amount.code = #100000110655
* packaging.packaging.packaging.packaging[=].containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.packaging.packaging[=].containedItem.amount.unit = "milligram(s)"
* packaging.packaging.packaging.packaging[+].type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.packaging[=].type.coding.code = #200000002143
* packaging.packaging.packaging.packaging[=].type.coding.display = "Sachet"
* packaging.packaging.packaging.packaging[=].quantity = 1
* packaging.packaging.packaging.packaging[=].material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.packaging[=].material.coding.code = #200000003208
* packaging.packaging.packaging.packaging[=].material.coding.display = "Plastic"
* packaging.packaging.packaging.packaging[=].containedItem.item.reference.reference = "ManufacturedItemDefinition/Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.packaging.packaging[=].containedItem.amount.value = 298
* packaging.packaging.packaging.packaging[=].containedItem.amount.code = #100000110655
* packaging.packaging.packaging.packaging[=].containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.packaging.packaging[=].containedItem.amount.unit = "milligram(s)"