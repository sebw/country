def _nic_server():
	nic_server = 'ftp.ripe.net'
	return nic_server

def _nic():
	nic = { 'Africa':['/pub/stats/afrinic/','delegated-afrinic-extended-latest'],
		'Asia Pacific':['/pub/stats/apnic/','delegated-apnic-extended-latest'],
		'America':['/pub/stats/arin/','delegated-arin-extended-latest'],
		'Latin America Caribbean':['/pub/stats/lacnic/','delegated-lacnic-extended-latest'],
		'Europe':['/pub/stats/ripencc/','delegated-ripencc-extended-latest']}
	return nic

def _country():
	country = {
		'AD':"Andorra",'AE':"United Arab Emirates",'AF':"Afghanistan",'AG':"Antigua and Barbuda",'AI':"Anguilla",'AL':"Albania",'AM':"Armenia",'AO':"Angola",'AP':"Asia/Pacific Region",'AQ':"Antarctica",'AR':"Argentina",'AS':"American Samoa",'AT':"Austria",'AU':"Australia",'AW':"Aruba",'AX':"Aland Islands",'AZ':"Azerbaijan",'BA':"Bosnia and Herzegovina",'BB':"Barbados",'BD':"Bangladesh",'BE':"Belgium",'BF':"Burkina Faso",'BG':"Bulgaria",'BH':"Bahrain",'BI':"Burundi",'BJ':"Benin",'BL':"Saint Bartelemey",'BM':"Bermuda",'BN':"Brunei Darussalam",'BO':"Bolivia",'BQ':"Bonaire, Saint Eustatius and Saba",'BR':"Brazil",'BS':"Bahamas",'BT':"Bhutan",'BV':"Bouvet Island",'BW':"Botswana",'BY':"Belarus",'BZ':"Belize",'CA':"Canada",'CC':"Cocos (Keeling) Islands",'CD':"Congo, The Democratic Republic of the",'CF':"Central African Republic",'CG':"Congo",'CH':"Switzerland",'CI':"Cote d'Ivoire",'CK':"Cook Islands",'CL':"Chile",'CM':"Cameroon",'CN':"China",'CO':"Colombia",'CR':"Costa Rica",'CU':"Cuba",'CV':"Cape Verde",'CW':"Curacao",'CX':"Christmas Island",'CY':"Cyprus",'CZ':"Czech Republic",'DE':"Germany",'DJ':"Djibouti",'DK':"Denmark",'DM':"Dominica",'DO':"Dominican Republic",'DZ':"Algeria",'EC':"Ecuador",'EE':"Estonia",'EG':"Egypt",'EH':"Western Sahara",'ER':"Eritrea",'ES':"Spain",'ET':"Ethiopia",'EU':"Europe",'FI':"Finland",'FJ':"Fiji",'FK':"Falkland Islands (Malvinas)",'FM':"Micronesia, Federated States of",'FO':"Faroe Islands",'FR':"France",'GA':"Gabon",'GB':"United Kingdom",'GD':"Grenada",'GE':"Georgia",'GF':"French Guiana",'GG':"Guernsey",'GH':"Ghana",'GI':"Gibraltar",'GL':"Greenland",'GM':"Gambia",'GN':"Guinea",'GP':"Guadeloupe",'GQ':"Equatorial Guinea",'GR':"Greece",'GS':"South Georgia and the South Sandwich Islands",'GT':"Guatemala",'GU':"Guam",'GW':"Guinea-Bissau",'GY':"Guyana",'HK':"Hong Kong",'HM':"Heard Island and McDonald Islands",'HN':"Honduras",'HR':"Croatia",'HT':"Haiti",'HU':"Hungary",'ID':"Indonesia",'IE':"Ireland",'IL':"Israel",'IM':"Isle of Man",'IN':"India",'IO':"British Indian Ocean Territory",'IQ':"Iraq",'IR':"Iran, Islamic Republic of",'IS':"Iceland",'IT':"Italy",'JE':"Jersey",'JM':"Jamaica",'JO':"Jordan",'JP':"Japan",'KE':"Kenya",'KG':"Kyrgyzstan",'KH':"Cambodia",'KI':"Kiribati",'KM':"Comoros",'KN':"Saint Kitts and Nevis",'KP':"Korea, Democratic People's Republic of",'KR':"Korea, Republic of",'KW':"Kuwait",'KY':"Cayman Islands",'KZ':"Kazakhstan",'LA':"Lao People's Democratic Republic",'LB':"Lebanon",'LC':"Saint Lucia",'LI':"Liechtenstein",'LK':"Sri Lanka",'LR':"Liberia",'LS':"Lesotho",'LT':"Lithuania",'LU':"Luxembourg",'LV':"Latvia",'LY':"Libyan Arab Jamahiriya",'MA':"Morocco",'MC':"Monaco",'MD':"Moldova, Republic of",'ME':"Montenegro",'MF':"Saint Martin",'MG':"Madagascar",'MH':"Marshall Islands",'MK':"Macedonia",'ML':"Mali",'MM':"Myanmar",'MN':"Mongolia",'MO':"Macao",'MP':"Northern Mariana Islands",'MQ':"Martinique",'MR':"Mauritania",'MS':"Montserrat",'MT':"Malta",'MU':"Mauritius",'MV':"Maldives",'MW':"Malawi",'MX':"Mexico",'MY':"Malaysia",'MZ':"Mozambique",'NA':"Namibia",'NC':"New Caledonia",'NE':"Niger",'NF':"Norfolk Island",'NG':"Nigeria",'NI':"Nicaragua",'NL':"Netherlands",'NO':"Norway",'NP':"Nepal",'NR':"Nauru",'NU':"Niue",'NZ':"New Zealand",'OM':"Oman",'PA':"Panama",'PE':"Peru",'PF':"French Polynesia",'PG':"Papua New Guinea",'PH':"Philippines",'PK':"Pakistan",'PL':"Poland",'PM':"Saint Pierre and Miquelon",'PN':"Pitcairn",'PR':"Puerto Rico",'PS':"Palestinian Territory",'PT':"Portugal",'PW':"Palau",'PY':"Paraguay",'QA':"Qatar",'RE':"Reunion",'RO':"Romania",'RS':"Serbia",'RU':"Russian Federation",'RW':"Rwanda",'SA':"Saudi Arabia",'SB':"Solomon Islands",'SC':"Seychelles",'SD':"Sudan",'SE':"Sweden",'SG':"Singapore",'SH':"Saint Helena",'SI':"Slovenia",'SJ':"Svalbard and Jan Mayen",'SK':"Slovakia",'SL':"Sierra Leone",'SM':"San Marino",'SN':"Senegal",'SO':"Somalia",'SR':"Suriname",'SS':"South Sudan",'ST':"Sao Tome and Principe",'SV':"El Salvador",'SX':"Sint Maarten",'SY':"Syrian Arab Republic",'SZ':"Swaziland",'TC':"Turks and Caicos Islands",'TD':"Chad",'TF':"French Southern Territories",'TG':"Togo",'TH':"Thailand",'TJ':"Tajikistan",'TK':"Tokelau",'TL':"Timor-Leste",'TM':"Turkmenistan",'TN':"Tunisia",'TO':"Tonga",'TR':"Turkey",'TT':"Trinidad and Tobago",'TV':"Tuvalu",'TW':"Taiwan",'TZ':"Tanzania, United Republic of",'UA':"Ukraine",'UG':"Uganda",'UM':"United States Minor Outlying Islands",'US':"United States",'UY':"Uruguay",'UZ':"Uzbekistan",'VA':"Holy See (Vatican City State)",'VC':"Saint Vincent and the Grenadines",'VE':"Venezuela",'VG':"Virgin Islands, British",'VI':"Virgin Islands, U.S.",'VN':"Vietnam",'VU':"Vanuatu",'WF':"Wallis and Futuna",'WS':"Samoa",'YE':"Yemen",'YT':"Mayotte",'ZA':"South Africa",'ZM':"Zambia",'ZW':"Zimbabwe" }
	return country

def _country_continent():
	country_continent = {
		"AD":"EU","AE":"AS","AF":"AS",'AG':'NA','AI':'NA','AL':'EU','AM':'AS','AN':'NA','AO':'AF','AP':'AS','AQ':'AN','AR':'SA','AS':'OC','AT':'EU','AU':'OC','AW':'NA','AX':'EU','AZ':'AS','BA':'EU','BB':'NA','BD':'AS','BE':'EU','BF':'AF','BG':'EU','BH':'AS','BI':'AF','BJ':'AF','BL':'NA','BM':'NA','BN':'AS','BO':'SA','BR':'SA','BS':'NA','BT':'AS','BV':'AN','BW':'AF','BY':'EU','BZ':'NA','CA':'NA','CC':'AS','CD':'AF','CF':'AF','CG':'AF','CH':'EU','CI':'AF','CK':'OC','CL':'SA','CM':'AF','CN':'AS','CO':'SA','CR':'NA','CU':'NA','CV':'AF','CX':'AS','CY':'AS','CZ':'EU','DE':'EU','DJ':'AF','DK':'EU','DM':'NA','DO':'NA','DZ':'AF','EC':'SA','EE':'EU','EG':'AF','EH':'AF','ER':'AF','ES':'EU','ET':'AF','EU':'EU','FI':'EU','FJ':'OC','FK':'SA','FM':'OC','FO':'EU','FR':'EU','FX':'EU','GA':'AF','GB':'EU','GD':'NA','GE':'AS','GF':'SA','GG':'EU','GH':'AF','GI':'EU','GL':'NA','GM':'AF','GN':'AF','GP':'NA','GQ':'AF','GR':'EU','GS':'AN','GT':'NA','GU':'OC','GW':'AF','GY':'SA','HK':'AS','HM':'AN','HN':'NA','HR':'EU','HT':'NA','HU':'EU','ID':'AS','IE':'EU','IL':'AS','IM':'EU','IN':'AS','IO':'AS','IQ':'AS','IR':'AS','IS':'EU','IT':'EU','JE':'EU','JM':'NA','JO':'AS','JP':'AS','KE':'AF','KG':'AS','KH':'AS','KI':'OC','KM':'AF','KN':'NA','KP':'AS','KR':'AS','KW':'AS','KY':'NA','KZ':'AS','LA':'AS','LB':'AS','LC':'NA','LI':'EU','LK':'AS','LR':'AF','LS':'AF','LT':'EU','LU':'EU','LV':'EU','LY':'AF','MA':'AF','MC':'EU','MD':'EU','ME':'EU','MF':'NA','MG':'AF','MH':'OC','MK':'EU','ML':'AF','MM':'AS','MN':'AS','MO':'AS','MP':'OC','MQ':'NA','MR':'AF','MS':'NA','MT':'EU','MU':'AF','MV':'AS','MW':'AF','MX':'NA','MY':'AS','MZ':'AF','NA':'AF','NC':'OC','NE':'AF','NF':'OC','NG':'AF','NI':'NA','NL':'EU','NO':'EU','NP':'AS','NR':'OC','NU':'OC','NZ':'OC','OM':'AS','PA':'NA','PE':'SA','PF':'OC','PG':'OC','PH':'AS','PK':'AS','PL':'EU','PM':'NA','PN':'OC','PR':'NA','PS':'AS','PT':'EU','PW':'OC','PY':'SA','QA':'AS','RE':'AF','RO':'EU','RS':'EU','RU':'EU','RW':'AF','SA':'AS','SB':'OC','SC':'AF','SD':'AF','SE':'EU','SG':'AS','SH':'AF','SI':'EU','SJ':'EU','SK':'EU','SL':'AF','SM':'EU','SN':'AF','SO':'AF','SR':'SA','ST':'AF','SV':'NA','SY':'AS','SZ':'AF','TC':'NA','TD':'AF','TF':'AN','TG':'AF','TH':'AS','TJ':'AS','TK':'OC','TL':'AS','TM':'AS','TN':'AF','TO':'OC','TR':'EU','TT':'NA','TV':'OC','TW':'AS','TZ':'AF','UA':'EU','UG':'AF','UM':'OC','US':'NA','UY':'SA','UZ':'AS','VA':'EU','VC':'NA','VE':'SA','VG':'NA','VI':'NA','VN':'AS','VU':'OC','WF':'OC','WS':'OC','YE':'AS','YT':'AF','ZA':'AF','ZM':'AF','ZW':'AF' }
	return country_continent

def _continent():
	continent = {
		'AF':'Africa',
		'AS':'Asia',
		'EU':'Europe',
		'SA':'Latin America Caribbean',
		'NA':'America' }
	return continent
