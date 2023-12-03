Instance: AMLaccord-5mg-Tablet-SE-IS-RegulatedAuthorization
InstanceOf: RegulatedAuthorization
Usage: #inline
* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber"
* identifier.value = "26703"
* subject = Reference(AMLaccord-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region = $100000000002#100000000535 "Sweden"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2008-10-10"
* holder.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* holder.identifier.value = "LOC-100007148"
* holder.display = "Accord Healthcare B.V."
* case.type = $authorisationDateType#dateOfFirstAuthorisation "First Authorisation"
* case.dateDateTime = "2008-10-10"