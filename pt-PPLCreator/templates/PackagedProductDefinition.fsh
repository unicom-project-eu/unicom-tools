{% for index,row in data["data"]["Package"].iterrows() %}

{% set ns = namespace() %}



Instance: ppd-{{ row["EMB ID"]}}
InstanceOf: PPLPackagedProductDefinition
Title: "{{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Nome PMS","MED ID")}} {{row["Package description  4.2"]}}"
Description: "{{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Nome PMS","MED ID")}} {{row["Package description  4.2"]}}"
Usage: #example

{% set ns.loc_id = row['MED ID']|get_data_from_sheet(data["data"],"Titular-Medicine","Titular AIM - OMS LOC-ID 2.8\n(SPOR-OMS LOC-ID)","MED ID") %}

* identifier[pcid].value = "PT-{{ns.loc_id|replace('LOC-','')}}-{{row["MED ID"]}}-{{row["CNPEM"]}}"

* name = "{{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Nome PMS","MED ID")}} {{row["Package description  4.2"]}}"

* description = "{{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Nome PMS","MED ID")}} {{row["Package description  4.2"]}}"

* status = #active

{% if row["Pack size 4.3 (qtd)"]|string !="nan"  %}

* containedItemQuantity = {{ row["Pack size 4.3 (qtd)"] }} $200000000014#{{ row["Pack size 4.3 (apresentação).1"]}} "{{ row["Pack size 4.3 (apresentação).1"]|get_data_from_sheet(data["data"],"SPOR_EN","200000000014_descr","200000000014")}}"
//* containedItemQuantity = {{ row["Pack size 4.3 (qtd)"] }} $200000000014#{{ row["Pack size 4.3 (apresentação).1"]}} "{{ row["Pack size 4.3 (apresentação)"]}}"

{% endif %}


* marketingStatus.country = $100000000002#100000000501 "Portuguese Republic"
* marketingStatus.status = $100000072052#100000072083 "Marketed"


* packaging
  * quantity = {{row["Package item (container) quantity - 4.7.5"]}}
  //* type = $100000073346#{{row["4.10.2 - Manufactured Item quantity - Unit RMS ID"]}} "{{row["Package item type"]}}"
  * type = $100000073346#{{row["Package item type 4.7.1"]}} "{{row["Package item type 4.7.1"]|get_data_from_sheet(data["data"],"SPOR_EN","100000073346_descr","100000073346")}}"


  * packaging.
    //* type = $100000073346#{{ row["Package item type 4.7.1.1"]}} "{{ row["Package item type.1"] }}"
    * type = $100000073346#{{ row["Package item type 4.7.1.1"]}} "{{ row["Package item type 4.7.1.1"]|get_data_from_sheet(data["data"],"SPOR_EN","100000073346_descr","100000073346")}}"

    * containedItem.item.reference = Reference(mid-{{row["MED ID"]}})
    * containedItem.amount.value = {{ row["Pack size 4.3 (qtd)"]}}

// for: {{ ns.name_to_has }}
* packageFor = Reference(mp-{{row["MED ID"]}})

// Reference to Organization: MAH
//* manufacturer = Reference({{ row['Müügiloa hoidja organisatsiooni ORG ID'] }})

{%- endfor %}