Instance: ccdb8e56-4520-4a02-bfad-fa0cb2f07eef
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "2"
* meta.lastUpdated = "2022-06-23T16:14:08.746+00:00"
* language = #FI
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* containedItemQuantity.value = 30
* containedItemQuantity.unit = "tablets"
* identifier.system = "http://ema.europa.eu/fhir/pcId"
* identifier.value = "EE-44680-0002"
* packageFor = Reference(d37bfa6f-ea90-4645-8be4-e7c649dd64f2)
* description = "Repäisypakkaus Alu(Al)/Alu(Al) 300 kpl tabletti, kalvopäällysteinen"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.material.coding.code = #200000003529
* packaging.material.coding.display = "Cardboard"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073559
* packaging.packaging.type.coding.display = "Strip"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003200
* packaging.packaging.material[=].coding.display = "Aluminium"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003200
* packaging.packaging.material[=].coding.display = "Aluminium"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/d9271259-c537-473e-8fb3-708b2a1d66ac"
* packaging.packaging.containedItem.amount.value = 30