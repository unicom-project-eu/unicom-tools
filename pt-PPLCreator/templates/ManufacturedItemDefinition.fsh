{% for index,row in data["data"]["ManufacturedItem"].iterrows() %}
{% if row["skip"] not in ['y', 'Y', 'x', 'X'] %}

Instance: mid-{{ row["MED ID"]  }}
InstanceOf: PPLManufacturedItemDefinition
Title: "Manufactured item {{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Nome PMS","MED ID")}}"
Description: "{{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Nome PMS","MED ID")}}"
Usage: #example


* status = #active
//* manufacturedDoseForm = $200000000004#{{row["manufacturedDoseForm - RMS ID"]}} "{{ row["manufacturedDoseForm"] }}"
* manufacturedDoseForm = $200000000004#{{row["manufacturedDoseForm - RMS ID"]}} "{{ row["manufacturedDoseForm - RMS ID"]|get_data_from_sheet(data["data"],"SPOR_EN","200000000004_descr","200000000004") }}"


* unitOfPresentation = $200000000014#{{ row["4.10.1 - Unit of presentation - Unit RMS ID"]|trim|int }} "{{ row["4.10.1 - Unit of presentation - Unit RMS ID"]|trim|int|get_data_from_sheet(data["data"],"SPOR_EN","200000000014_descr","200000000014") }}"
//* unitOfPresentation = $200000000014#{{ row["4.10.2 - Manufactured Item quantity - Unit RMS ID"] }} "{{ row["4.10.1 - Unit of presentation"] }}"


*  manufacturer = Reference({{row["MED ID"]|get_data_from_sheet(data["data"],"Titular-Medicine","Titular AIM - OMS LOC-ID 2.8\n(SPOR-OMS LOC-ID)","MED ID")}})

{%- endif %}
{%- endfor %}

