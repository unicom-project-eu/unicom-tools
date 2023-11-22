import xmltodict
import json


# Paste your XML data here
xml_data = [
    """
<root>
<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form --> 
	<id value="Fragmin-7500IE-Solution-SE-IS-AdministrableProductDefinition"/> <!-- NPL-id (produkt)-SE-PharmProd -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-7500IE-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-7500IE-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-7500IE-Solution-SE-IS-AdministrableProductDefinition" />
    </request>
 </entry>
</root>
""",
    """<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form --> 
  <id value="Fragmin-15000IE-Solution-SE-IS-AdministrableProductDefinition"/> <!-- Unik kod ENTRY 3. Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-15000IE-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-15000IE-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-15000IE-Solution-SE-IS-AdministrableProductDefinition" />
    </request>
 </entry>
""",
    """<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form --> 
  <id value="Fragmin-2500IEml-Solution-SE-IS-AdministrableProductDefinition"/> <!-- Unik kod ENTRY 3. Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-2500IEml-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-2500IEml-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-2500IEml-Solution-SE-IS-AdministrableProductDefinition" />
    </request>
 </entry>
""",
    """
<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form --> 
  <id value="Fragmin-5000IE-Solution-SE-IS-AdministrableProductDefinition"/> <!-- Unik kod ENTRY 3. Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-5000IE-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-5000IE-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-5000IE-Solution-SE-IS-AdministrableProductDefinition" /> 
    </request>
 </entry>
 """,
    """<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form --> 
  <id value="Fragmin-10000IE-Solution-SE-IS-AdministrableProductDefinition"/> <!-- Unik kod ENTRY 3. Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-10000IE-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-10000IE-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-10000IE-Solution-SE-IS-AdministrableProductDefinition" /> 
    </request>
 </entry>""",
    """<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form --> 
  <id value="Fragmin-18000IE-Solution-SE-IS-AdministrableProductDefinition"/> <!-- Unik kod ENTRY 3. Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-18000IE-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-18000IE-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-18000IE-Solution-SE-IS-AdministrableProductDefinition" />
    </request>
 </entry>
""",
    """<entry>
  <resource>
  <AdministrableProductDefinition> <!-- Beskriver läkemedlet i bruksfärdig (administrerad) form -->
    <id value="Fragmin-10000IEml-Solution-SE-IS-AdministrableProductDefinition"/> <!-- Unik kod ENTRY 3. Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
        <status value="active"/>
		<formOf>
           <reference value="MedicinalProductDefinition/Fragmin-10000IEml-Solution-SE-IS-MedicinalProductDefinition" /> <!-- Referens till ENTRY 1 = MedicinalProductDefinition -->
        </formOf>
		
	<administrableDoseForm> <!-- Anger läkemedelsform för bruksfärdigt läkemedel -->
    <coding>
        <system value="http://spor.ema.europa.eu/v1/lists/200000000004" /> <!-- SPOR-lista "Pharmaceutical Dose Form" -->
        <code value="100000073863" /> <!-- Kod -->
		<display value="Solution for injection"/> <!-- Textbeskrivning bruksfärdig läkemedelsform -->        
    </coding>
    </administrableDoseForm>
	
	<producedFrom>
		<reference value="ManufacturedItemDefinition/Fragmin-10000IEml-Solution-SE-IS-ManufacturedItemDefinition" /> <!-- Referens till ENTRY 5 = ManufacturedItemDefinition (alla entry) -->
	</producedFrom>
	
	<routeOfAdministration> <!-- Administreringsväg(ar). Hämtas från EIRA -->
    <code>
     <coding> <!-- Administreringsväg 1 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073611" /> <!-- Kod -->
		<display value="Intravenous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 2 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000073633" /> <!-- Kod -->
		<display value="Subcutaneous use"/> <!-- Textbeskrivning -->   
     </coding>
     <coding> <!-- Administreringsväg 3 -->
        <system value="http://spor.ema.europa.eu/v1/lists/100000073345" /> <!-- SPOR-lista "Routes and Methods of Administration" -->
        <code value="100000075556" /> <!-- Kod -->
		<display value="Extracorporeal use"/> <!-- Textbeskrivning -->   
     </coding>
    </code>
    </routeOfAdministration>
		
  </AdministrableProductDefinition>
  </resource>
    <request>
      <method value="PUT" />
      <url value="AdministrableProductDefinition/Fragmin-10000IEml-Solution-SE-IS-AdministrableProductDefinition" /> <!-- Produktnamn-styrka-läkemedelsform-SE-IS-resource0X -->
    </request>
 </entry>
""",
]
for entry in xml_data:
    json_data = json.dumps(xmltodict.parse(entry), indent=4)
    print(json_data)
# Convert XML to JSON

# Print the JSON data
