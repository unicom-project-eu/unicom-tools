Instance: Xylocain-WOP-10mgml-InjSol-SE-AJ-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-06T10:01:01.873+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 5 http://spor.ema.europa.eu/v1/lists/200000000014#200000002164 "Ampoule"
* packageFor = Reference(Xylocain-WOP-10mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* description = "Ampull, 5 x 10 ml (blisterförpackning)"
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
* packaging.shelfLifeStorage.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* packaging.shelfLifeStorage.type.coding.code = #100000073403
* packaging.shelfLifeStorage.type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* packaging.shelfLifeStorage.periodDuration.value = 3
* packaging.shelfLifeStorage.periodDuration.code = #200000003434
* packaging.shelfLifeStorage.periodDuration.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.shelfLifeStorage.periodDuration.unit = "Year"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073420
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not freeze"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073410
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not store above 25 °C"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073496
* packaging.packaging.type.coding.display = "Blister"
* packaging.packaging.quantity = 1
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003208
* packaging.packaging.material.coding.display = "Plastic"
* packaging.packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.type.coding.code = #100000073490
* packaging.packaging.packaging.type.coding.display = "Ampoule"
* packaging.packaging.packaging.quantity = 5
* packaging.packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.material.coding.code = #200000003208
* packaging.packaging.packaging.material.coding.display = "Plastic"
* packaging.packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Xylocain-WOP-10mgml-InjSol-SE-AJ-ManufacturedItemDefinition"
* packaging.packaging.packaging.containedItem.amount.value = 10
* packaging.packaging.packaging.containedItem.amount.code = #100000110662
* packaging.packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.packaging.packaging.containedItem.amount.unit = "millilitre(s)"