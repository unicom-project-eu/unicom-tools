Instance: Curocef1500mgPulver-A-HL-MedicinalProductDefinition
InstanceOf: PPLMedicinalProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-09-01T20:20:03.316+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"

* combinedPharmaceuticalDoseForm = $200000000004#100000116186 "Powder for solution for injection/infusion"
* identifier.system = "http://ema.europa.eu/fhir/mpId"
* identifier.value = "AT-16569"

* domain.coding = $100000000004#100000000012 "Human use"
* indication = "Curocef wird angewendet zur Behandlung der nachfolgend genannten Infektionen bei Erwachsenen und Kindern, einschließlich Neugeborenen (von Geburt an) ..."
* indication.extension.url = "http://ema.europa.eu/fhir/extension/language"
* indication.extension.valueCoding = $100000072057#100000072178 "German"

* legalStatusOfSupply.coding = $100000072051#100000072079 "Medicinal product on medical prescription for non-renewable delivery"
* additionalMonitoringIndicator = $additionalMonitoringIndicator#True "True"
* pediatricUseIndicator = $paediatricUseIndicator#True "True"

* classification[+].coding = $200000000324#200000003517 "Other"

* classification[=].coding = $100000116045#100000116053 "Well-established use application (Article 10a of Directive No 2001/83/EC)"

* classification[=].coding = $100000093533#100000096183 "J01DC02"

* classification[=].coding = $100000155526#100000155527 "Chemical"
* attachedDocument = Reference(DocumentReference/Curocef1500mgPulver-A-HL-DocumentReference01)
* masterFile = Reference(mfl1)
* contact[+].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* contact[=].type.coding.extension.valueInteger = 1
* contact[=].type.coding = $100000154441#100000155057 "Qualified Person in the EEA for Pharmacovigilance"
* contact[=].contact = Reference(qppv1)
* contact[+].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* contact[=].type.coding.extension.valueInteger = 3
* contact[=].type.coding = $100000154441#200000017719
* contact[=].contact = Reference(phvenq1)
* name.productName = "Curocef 1500 mg Pulver zur Herstellung einer Injektions- oder Infusionslösung"
* name.part[+].part = "Curocef"
* name.part[=].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* name.part[=].type.coding.extension.valueInteger = 1
* name.part[=].type.coding.system = "https://spor.ema.europa.eu/v1/lists/220000000000"
* name.part[=].type.coding.code = #220000000002
* name.part[=].type.coding.display = "Invented name part"
* name.part[+].part = "1500 mg"
* name.part[=].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* name.part[=].type.coding.extension.valueInteger = 1
* name.part[=].type.coding.system = "https://spor.ema.europa.eu/v1/lists/220000000000"
* name.part[=].type.coding.code = #220000000004
* name.part[=].type.coding.display = "Strength part"
* name.part[+].part = "Pulver zur Herstellung einer Injektions- oder Infusionslösung"
* name.part[=].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* name.part[=].type.coding.extension.valueInteger = 1
* name.part[=].type.coding.system = "https://spor.ema.europa.eu/v1/lists/220000000000"
* name.part[=].type.coding.code = #220000000005
* name.part[=].type.coding.display = "Pharmaceutical dose form part"
* name.usage.country.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* name.usage.country.coding.extension.valueInteger = 1
* name.usage.country.coding.system = "https://spor.ema.europa.eu/v1/lists/100000000002"
* name.usage.country.coding.code = #100000000330
* name.usage.country.coding.display = "Austria"
* name.usage.language.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* name.usage.language.coding.extension.valueInteger = 1
* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072178
* name.usage.language.coding.display = "German"
* operation[+].type.concept.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].type.concept.coding.extension.valueInteger = 1
* operation[=].type.concept.coding = $100000160406#100000160467 "Manufacture of active substance"
* operation[=].effectiveDate.start = "2016-07-17"
* operation[=].organization.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* operation[=].organization.identifier.value = "LOC-100000004"
* operation[=].organization.display = "Austrian Agency For Health And Food Safety"
* operation[=].confidentialityIndicator.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].confidentialityIndicator.coding.extension.valueInteger = 1
* operation[=].confidentialityIndicator.coding = $200000004983#200000004984 "Confidential"
* operation[+].type.concept.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].type.concept.coding.extension.valueInteger = 1
* operation[=].type.concept.coding = $100000160406#100000160407 "Manufacturer responsible for batch certification"
* operation[=].effectiveDate.start = "2010-12-22"
* operation[=].organization.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* operation[=].organization.identifier.value = "LOC-100050477"
* operation[=].organization.display = "Acs Dobfar S.P.A."
* operation[=].confidentialityIndicator.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].confidentialityIndicator.coding.extension.valueInteger = 1
* operation[=].confidentialityIndicator.coding = $200000004983#200000004985 "Public"
* operation[+].type.concept.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].type.concept.coding.extension.valueInteger = 1
* operation[=].type.concept.coding = $100000160406#100000160464 "Secondary packaging"
* operation[=].effectiveDate.start = "2020-03-09"
* operation[=].organization.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* operation[=].organization.identifier.value = "LOC-100000004"
* operation[=].organization.display = "Austrian Agency For Health And Food Safety"
* operation[=].confidentialityIndicator.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].confidentialityIndicator.coding.extension.valueInteger = 1
* operation[=].confidentialityIndicator.coding = $200000004983#200000004984 "Confidential"
* operation[+].type.concept.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].type.concept.coding.extension.valueInteger = 1
* operation[=].type.concept.coding = $100000160406#100000160463 "Primary packaging"
* operation[=].effectiveDate.start = "2020-03-09"
* operation[=].organization.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* operation[=].organization.identifier.value = "LOC-100000004"
* operation[=].organization.display = "Austrian Agency For Health And Food Safety"
* operation[=].confidentialityIndicator.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* operation[=].confidentialityIndicator.coding.extension.valueInteger = 1
* operation[=].confidentialityIndicator.coding = $200000004983#200000004984 "Confidential"
//DUMMY
* legalStatusOfSupply = $100000072051#100000072084 "Medicinal product subject to medical prescription"