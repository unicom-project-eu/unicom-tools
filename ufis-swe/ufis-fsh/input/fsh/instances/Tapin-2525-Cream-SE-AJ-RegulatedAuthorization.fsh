Instance: Tapin-2525-Cream-SE-AJ-RegulatedAuthorization
InstanceOf: RegulatedAuthorization
Usage: #inline
* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber"
* identifier.value = "23074"
* subject = Reference(Tapin-2525-Cream-SE-AJ-MedicinalProductDefinition)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region = $100000000002#100000000535 "Sweden"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2008-02-22"
* holder.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* holder.identifier.value = "LOC-100005206"
* holder.display = "Orifarm Generics A/S"
* case.type = $authorisationDateType#dateOfFirstAuthorisation "First Authorisation"
* case.dateDateTime = "2008-02-22"