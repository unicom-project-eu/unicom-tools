{%- for index,row in data["data"]["ManufacturedItem"].iterrows() -%}

{% set ns = namespace() %}

{% set ns.ing_id = row["Ingredient ID"]|string %}

{%- if ns.ing_id|string != "nan" -%}
{%- for idx in range(0,ns.ing_id.count(";")+1) -%} 
{% set ns.ing_name = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Nome Substância\n(Substance name)","Ingredient ID") %}
{% set ns.ing_type = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Tipo Ingrediente\n(Ingredient role)","Ingredient ID") %}

{% set ns.ing_reference_descr = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Descrição\n(Description)","Ingredient ID") %}
{% set ns.ing_reference_id = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","EU-SMS/SRS","Ingredient ID") %}
{% set ns.ing_sms_id = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","EU-SMS/SRS.1","Ingredient ID") %}

{% set ns.num_value = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator value","Ingredient ID") %}
{% set ns.num_unit = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator unities RMS ID","Ingredient ID") %}
{% set ns.num_unit_desc = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator unity","Ingredient ID") %}
{% set ns.num_unit_desc_en = ns.num_unit|get_data_from_sheet(data["data"],"SPOR_EN","100000110633_descr","100000110633") %}

{% set ns.den_value = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator value","Ingredient ID") %}
{% set ns.den_unit = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator unities RMS ID","Ingredient ID") %}
{% set ns.den_unit_desc = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator unity","Ingredient ID") %}
{% set ns.den_unit_desc_en = ns.den_unit|int|get_data_from_sheet(data["data"],"SPOR_EN","200000000014_descr","200000000014") %}

{% set ns.ref_num_value = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator value.2","Ingredient ID") %}
{% set ns.ref_num_unit = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator unities RMS ID.2","Ingredient ID") %}
{% set ns.ref_num_unit_desc = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator unity.2","Ingredient ID") %}
{% set ns.ref_num_unit_desc_en = ns.ref_num_unit|get_data_from_sheet(data["data"],"SPOR_EN","100000110633_descr","100000110633") %}

{% set ns.ref_den_value = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator value.2","Ingredient ID") %}
{% set ns.ref_den_unit = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator unities RMS ID.2","Ingredient ID") %}
{% set ns.ref_den_unit_desc = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator unity.2","Ingredient ID") %}
{% set ns.ref_den_unit_desc_en = ns.ref_den_unit|int|get_data_from_sheet(data["data"],"SPOR_EN","200000000014_descr","200000000014") %}

{%- if ns.num_value|string == "nan" -%}

{% set ns.num_value = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator value.1","Ingredient ID") %}
{% set ns.num_unit = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator unities RMS ID.1","Ingredient ID") %}
{% set ns.num_unit_desc = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Numerator unity.1","Ingredient ID")%}
{% set ns.num_unit_desc_en = ns.num_unit|get_data_from_sheet(data["data"],"SPOR_EN","100000110633_descr","100000110633") %}

{% set ns.den_value = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator value.1","Ingredient ID") %}
{% set ns.den_unit = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator unities RMS ID.1","Ingredient ID") %}
{% set ns.den_unit_desc = ns.ing_id.split(";")[idx]|float| get_data_from_sheet(data["data"],"Ingredient","Denominator unity.1","Ingredient ID") %}
{% set ns.den_unit_desc_en = ns.den_unit|get_data_from_sheet(data["data"],"SPOR_EN","200000000014_descr","200000000014") %}
{%- endif -%}

{%- if ns.den_unit_desc_en|string == "None" -%}
{{"// ERROR[10] - Code wrong on the sheet [100000110633 vs 200000000014]  for unit denominator at INDEX:{}".format(index+1) }}

{% set ns.den_unit_desc_en = ns.den_unit|get_data_from_sheet(data["data"],"SPOR_EN","100000110633_descr","100000110633") %}
{%- endif -%}

{%- if ns.ref_den_unit_desc_en|string == "None" -%}
{{"// ERROR[10] - Code wrong on the sheet [100000110633 vs 200000000014] for unit reference denominator at INDEX:{}".format(index+1) }}

{% set ns.ref_den_unit_desc_en = ns.ref_den_unit|get_data_from_sheet(data["data"],"SPOR_EN","100000110633_descr","100000110633") %}
{%- endif -%}



{%- if ns.ref_den_value|string == "1.0" -%}
{% set ns.ref_den_value =ns.ref_den_value|int %}
{%- endif -%}

{%- if ns.den_value|string == "1.0" -%}
{% set ns.den_value =ns.den_value|int %}
{%- endif -%}

{%- if ns.ing_name|string != "None" -%}

//{{ns.ing_name}}//{{ns.ing_id}}
{% set ns.ing_id_hash = ns.ing_name~row["MED ID"]~ns.num_value %}
Instance: ingredient-{{ ns.ing_id_hash|create_hash_id}}
InstanceOf: PPLIngredient
Title: "{{ ns.ing_name}}"
Description: "ingredient {{ns.ing_name}} with strength {{ns.num_value}} as {{ ns.ing_type}} for {{ row["MED ID"]}}"
Usage: #example

* role = $100000072050#100000072072 "active"
* status = #active
//* substance.code.concept = $sms#{{ns.ing_sms_id|int}} "{{ns.ing_name}}" //name pt?
//* substance.code.concept = $sms#{{ns.ing_reference_id|int}} "{{ns.ing_reference_id|int|get_data_from_sheet(data["data"],"SPOR_EN","sms_descr","sms")}}"
* substance.code.concept = $sms#{{ns.ing_sms_id|int}} "{{ns.ing_sms_id|int|get_data_from_sheet(data["data"],"SPOR_EN","sms_descr","sms")}}"

* substance.strength.presentationRatio.numerator = {{ ns.num_value }}  $100000110633#{{ ns.num_unit|int}}  "{{ ns.num_unit_desc_en }}"
* substance.strength.presentationRatio.denominator = {{ ns.den_value }}  $200000000014#{{ ns.den_unit|int}}  "{{ ns.den_unit_desc_en }}"


* substance.strength.referenceStrength.strengthRatio.numerator = {{ ns.ref_num_value }}  $100000110633#{{ ns.ref_num_unit|int}}  "{{ ns.ref_num_unit_desc_en }}"
* substance.strength.referenceStrength.strengthRatio.denominator =  {{ ns.ref_den_value|int }}  $200000000014#{{ ns.ref_den_unit|int}}  "{{ ns.ref_den_unit_desc_en }}"

//* substance.strength.referenceStrength.substance.concept = $sms#{{ns.ing_reference_id}} "{{ns.ing_reference_descr}}"
//* substance.strength.referenceStrength.substance.concept = $sms#{{ns.ing_sms_id|int}} "{{ns.ing_sms_id|get_data_from_sheet(data["data"],"SPOR_EN","sms_descr","sms")}}"
* substance.strength.referenceStrength.substance.concept = $sms#{{ns.ing_reference_id|int}} "{{ns.ing_reference_id|get_data_from_sheet(data["data"],"SPOR_EN","sms_descr","sms")}}"

// Reference to products item
* for[0] = Reference(mp-{{row["MED ID"]}})
* for[+] = Reference(ap-{{row["MED ID"]}})
* for[+] = Reference(mid-{{row["MED ID"]}})

{%- else  -%}
{{"// ERROR[7] - No Ingredient Id for ns.ing_id at INDEX:{}".format(index+1) }}
{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- endfor -%}