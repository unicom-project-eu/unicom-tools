Instance: AMLbluefish-5mg-Tablet-SE-IS-RegulatedAuthorization
InstanceOf: PPLRegulatedAuthorization
Usage: #inline

* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber"
* identifier.value = "23987"
* subject = Reference(AMLbluefish-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region = $100000000002#100000000535 "Sweden"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2007-10-26"
* case.type = $authorisationDateType#dateOfFirstAuthorisation "First Authorisation"
* case.dateDateTime = "2007-10-26"
* holder = Reference(LOC-100001076)
