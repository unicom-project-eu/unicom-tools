Instance: ISOactavis-10mg-Capsule-SE-IS-PackagedProductDefinition
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-09T16:35:58.061+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* extension.valueQuantity = 10 http://spor.ema.europa.eu/v1/lists/200000000014#200000002113 "Capsule"
* packageFor = Reference(ISOactavis-10mg-Capsule-SE-IS-MedicinalProductDefinition)
* description = "Blister, 100 kapslar"
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
* package.shelfLifeStorage.periodDuration.value = 3
* package.shelfLifeStorage.periodDuration.unit = "years"
* package.shelfLifeStorage.specialPrecautionsForStorage[0].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = "100000073423"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Keep the container in the outer carton"
* package.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = "100000073430"
* package.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Protect from light"
* package.package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.type.coding.code = "100000073496"
* package.package.type.coding.display = "Blister"
* package.package.quantity = 10
* package.package.material[0].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003222"
* package.package.material[=].coding.display = "PolyVinyl Chloride"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003225"
* package.package.material[=].coding.display = "PolyVinylidene Chloride"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003200"
* package.package.material[=].coding.display = "Aluminium"
* package.package.containedItem.item.reference.reference = "ManufacturedItemDefinition/ISOactavis-10mg-Capsule-SE-IS-ManufacturedItemDefinition"
* package.package.containedItem.amount.value = 10
* package.package.containedItem.amount.code = "200000002113"
* package.package.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* package.package.containedItem.amount.unit = "Capsule"