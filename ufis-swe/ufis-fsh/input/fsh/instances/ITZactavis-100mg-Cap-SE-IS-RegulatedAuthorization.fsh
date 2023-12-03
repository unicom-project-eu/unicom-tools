Instance: ITZactavis-100mg-Cap-SE-IS-RegulatedAuthorization
InstanceOf: RegulatedAuthorization
Usage: #inline
* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber"
* identifier.value = "20352"
* subject = Reference(ITZactavis-100mg-Cap-SE-IS-MedicinalProductDefinition)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region = $100000000002#100000000535 "Sweden"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2005-07-01"
* holder.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* holder.identifier.value = "LOC-100001873"
* holder.display = "Actavis Group PTC ehf."
* case.type = $authorisationDateType#dateOfFirstAuthorisation "First Authorisation"
* case.dateDateTime = "2005-07-01"