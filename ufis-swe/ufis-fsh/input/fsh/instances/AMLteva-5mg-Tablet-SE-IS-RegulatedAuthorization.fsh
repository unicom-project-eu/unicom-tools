Instance: AMLteva-5mg-Tablet-SE-IS-RegulatedAuthorization
InstanceOf: RegulatedAuthorization
Usage: #inline
* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber"
* identifier.value = "26391"
* subject = Reference(AMLteva-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region = $100000000002#100000000535 "Sweden"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2008-07-18"
* holder.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* holder.identifier.value = "LOC-100001602"
* holder.display = "Teva Sweden AB"
* case.type = $authorisationDateType#dateOfFirstAuthorisation "First Authorisation"
* case.dateDateTime = "2008-07-18"