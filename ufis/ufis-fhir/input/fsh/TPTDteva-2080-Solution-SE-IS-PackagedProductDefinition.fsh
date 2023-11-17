Instance: TPTDteva-2080-Solution-SE-IS-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "7"
* meta.lastUpdated = "2022-11-12T08:16:06.69+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 28 http://spor.ema.europa.eu/v1/lists/200000000014#200000002163 "Actuation"
* packageFor = Reference(TPTDteva-2080-Solution-SE-IS-MedicinalProductDefinition)
* description = "Förfylld injektionspenna, 1 x 2,4 ml"
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
* packaging.packaging.type.coding.code = #100000073543
* packaging.packaging.type.coding.display = "Pre-filled pen"
* packaging.packaging.quantity = 1
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003204
* packaging.packaging.material[=].coding.display = "Glass type I"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003226
* packaging.packaging.material[=].coding.display = "Rubber"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003200
* packaging.packaging.material[=].coding.display = "Aluminium"
* packaging.packaging.containedItem[+].item.reference.reference = "ManufacturedItemDefinition/TPTDteva-2080-Solution-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.containedItem[=].amount.value = 28
* packaging.packaging.containedItem[=].amount.code = #200000002163
* packaging.packaging.containedItem[=].amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.containedItem[=].amount.unit = "Actuation"
* packaging.packaging.containedItem[+].item.reference.reference = "DeviceDefinition/TPTDteva-2080-Solution-SE-IS-DeviceDefinition"