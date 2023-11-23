Instance: MetforminSandoz-850mg-Tablet-SE-BS-PackagedProductDefinition-02
InstanceOf: PPLPackagedProductDefinition

* extension[+].url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 200 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* extension[+].url = "http://ema.europa.eu/fhir/extension/language"
* extension[=].valueCoding = $100000072057#100000072288 "Swedish"
* packageFor = Reference(MetforminSandoz-850mg-Tablet-SE-BS-MedicinalProductDefinition)
* description = "Burk, 200 tabletter"
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
* packaging.packaging.type.coding.code = #100000073497
* packaging.packaging.type.coding.display = "Bottle"
* packaging.packaging.quantity = 1
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003215
* packaging.packaging.material.coding[=].display = "High Density PolyEthylene"
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003216
* packaging.packaging.material.coding[=].display = "Low Density PolyEthylene"
* packaging.packaging.material.coding[+].system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding[=].code = #200000003219
* packaging.packaging.material.coding[=].display = "PolyPropylene"
* packaging.packaging.containedItem.item.reference = Reference(MetforminSandoz-850mg-Tablet-SE-BS-ManufacturedItemDefinition)
* packaging.packaging.containedItem.amount.value = 200
* packaging.packaging.containedItem.amount.code = #200000002152
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633~200000000014"
* packaging.packaging.containedItem.amount.unit = "Tablet"