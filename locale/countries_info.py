def to_lower():
    for v in COUNTRY_INFO:
        COUNTRY_INFO[v]['code'] = v.lower()
        COUNTRY_INFO[v]['local_name'] = COUNTRY_INFO[v]['name']
        print COUNTRY_INFO[v]
        
    f = open('temp.txt', 'w')
    for v in COUNTRY_INFO:
        f.write('\''+v+'\':')
        f.write(str(COUNTRY_INFO[v]))
        f.write(",\r\n")

COUNTRY_LIST_EU = ('au','be','bg','cy','cz','dk','ee','fi','fr','de','gr','hu','ie','it','lv','lt','lu','mt','nl','pl','pt','ro','sk','si','es','se','gb')

"""
consider adding local names in local aphabet maybe, so far so good
"""
COUNTRY_INFO = {
    'WF':{'code': 'wf', 'name': 'Wallis & Futuna Islands', 'local_name': 'Wallis & Futuna Islands'},
    'JP':{'code': 'jp', 'name': 'Japan', 'local_name': 'Japan'},
    'JM':{'code': 'jm', 'name': 'Jamaica', 'local_name': 'Jamaica'},
    'JO':{'code': 'jo', 'name': 'Jordan', 'local_name': 'Jordan'},
    'WS':{'code': 'ws', 'name': 'Samoa', 'local_name': 'Samoa'},
    'GW':{'code': 'gw', 'name': 'Guinea-Bissau', 'local_name': 'Guinea-Bissau'},
    'GU':{'code': 'gu', 'name': 'Guam', 'local_name': 'Guam'},
    'GT':{'code': 'gt', 'name': 'Guatemala', 'local_name': 'Guatemala'},
    'GS':{'code': 'gs', 'name': 'South Georgia and the South Sandwich Islands', 'local_name': 'South Georgia and the South Sandwich Islands'},
    'GR':{'code': 'gr', 'name': 'Greece', 'local_name': 'Greece'},
    'GQ':{'code': 'gq', 'name': 'Equatorial Guinea', 'local_name': 'Equatorial Guinea'},
    'GP':{'code': 'gp', 'name': 'Guadeloupe', 'local_name': 'Guadeloupe'},
    'GY':{'code': 'gy', 'name': 'Guyana', 'local_name': 'Guyana'},
    'GF':{'code': 'gf', 'name': 'French Guiana', 'local_name': 'French Guiana'},
    'GE':{'code': 'ge', 'name': 'Georgia', 'local_name': 'Georgia'},
    'GD':{'code': 'gd', 'name': 'Grenada', 'local_name': 'Grenada'},
    'GB':{'code': 'gb', 'name': 'United Kingdom (Great Britain)', 'local_name': 'United Kingdom (Great Britain)'},
    'GA':{'code': 'ga', 'name': 'Gabon', 'local_name': 'Gabon'},
    'GN':{'code': 'gn', 'name': 'Guinea', 'local_name': 'Guinea'},
    'GM':{'code': 'gm', 'name': 'Gambia', 'local_name': 'Gambia'},
    'GL':{'code': 'gl', 'name': 'Greenland', 'local_name': 'Greenland'},
    'GI':{'code': 'gi', 'name': 'Gibraltar', 'local_name': 'Gibraltar'},
    'GH':{'code': 'gh', 'name': 'Ghana', 'local_name': 'Ghana'},
    'PR':{'code': 'pr', 'name': 'Puerto Rico', 'local_name': 'Puerto Rico'},
    'PW':{'code': 'pw', 'name': 'Palau', 'local_name': 'Palau'},
    'PT':{'code': 'pt', 'name': 'Portugal', 'local_name': 'Portugal'},
    'PY':{'code': 'py', 'name': 'Paraguay', 'local_name': 'Paraguay'},
    'PA':{'code': 'pa', 'name': 'Panama', 'local_name': 'Panama'},
    'PF':{'code': 'pf', 'name': 'French Polynesia', 'local_name': 'French Polynesia'},
    'PG':{'code': 'pg', 'name': 'Papua New Guinea', 'local_name': 'Papua New Guinea'},
    'PE':{'code': 'pe', 'name': 'Peru', 'local_name': 'Peru'},
    'PK':{'code': 'pk', 'name': 'Pakistan', 'local_name': 'Pakistan'},
    'PH':{'code': 'ph', 'name': 'Philippines', 'local_name': 'Philippines'},
    'PN':{'code': 'pn', 'name': 'Pitcairn', 'local_name': 'Pitcairn'},
    'PL':{'code': 'pl', 'name': 'Poland', 'local_name': 'Poland'},
    'PM':{'code': 'pm', 'name': 'St. Pierre & Miquelon', 'local_name': 'St. Pierre & Miquelon'},
    'ZM':{'code': 'zm', 'name': 'Zambia', 'local_name': 'Zambia'},
    'ZA':{'code': 'za', 'name': 'South Africa', 'local_name': 'South Africa'},
    'ZZ':{'code': 'zz', 'name': 'Unknown or unspecified country', 'local_name': 'Unknown or unspecified country'},
    'ZW':{'code': 'zw', 'name': 'Zimbabwe', 'local_name': 'Zimbabwe'},
    'ZR':{'code': 'zr', 'name': 'Zaire', 'local_name': 'Zaire'},
    'MD':{'code': 'md', 'name': 'Moldova, Republic of', 'local_name': 'Moldova, Republic of'},
    'MG':{'code': 'mg', 'name': 'Madagascar', 'local_name': 'Madagascar'},
    'MA':{'code': 'ma', 'name': 'Morocco', 'local_name': 'Morocco'},
    'MC':{'code': 'mc', 'name': 'Monaco', 'local_name': 'Monaco'},
    'MM':{'code': 'mm', 'name': 'Myanmar', 'local_name': 'Myanmar'},
    'ML':{'code': 'ml', 'name': 'Mali', 'local_name': 'Mali'},
    'MO':{'code': 'mo', 'name': 'Macau', 'local_name': 'Macau'},
    'MN':{'code': 'mn', 'name': 'Mongolia', 'local_name': 'Mongolia'},
    'MH':{'code': 'mh', 'name': 'Marshall Islands', 'local_name': 'Marshall Islands'},
    'MU':{'code': 'mu', 'name': 'Mauritius', 'local_name': 'Mauritius'},
    'MT':{'code': 'mt', 'name': 'Malta', 'local_name': 'Malta'},
    'MW':{'code': 'mw', 'name': 'Malawi', 'local_name': 'Malawi'},
    'MV':{'code': 'mv', 'name': 'Maldives', 'local_name': 'Maldives'},
    'MQ':{'code': 'mq', 'name': 'Martinique', 'local_name': 'Martinique'},
    'MP':{'code': 'mp', 'name': 'Northern Mariana Islands', 'local_name': 'Northern Mariana Islands'},
    'MS':{'code': 'ms', 'name': 'Monserrat', 'local_name': 'Monserrat'},
    'MR':{'code': 'mr', 'name': 'Mauritania', 'local_name': 'Mauritania'},
    'MY':{'code': 'my', 'name': 'Malaysia', 'local_name': 'Malaysia'},
    'MX':{'code': 'mx', 'name': 'Mexico', 'local_name': 'Mexico'},
    'MZ':{'code': 'mz', 'name': 'Mozambique', 'local_name': 'Mozambique'},
    'FR':{'code': 'fr', 'name': 'France', 'local_name': 'France'},
    'FX':{'code': 'fx', 'name': 'France, Metropolitan', 'local_name': 'France, Metropolitan'},
    'FI':{'code': 'fi', 'name': 'Finland', 'local_name': 'Finland'},
    'FJ':{'code': 'fj', 'name': 'Fiji', 'local_name': 'Fiji'},
    'FK':{'code': 'fk', 'name': 'Falkland Islands (Malvinas)', 'local_name': 'Falkland Islands (Malvinas)'},
    'FM':{'code': 'fm', 'name': 'Micronesia', 'local_name': 'Micronesia'},
    'FO':{'code': 'fo', 'name': 'Faroe Islands', 'local_name': 'Faroe Islands'},
    'CK':{'code': 'ck', 'name': 'Cook Iislands', 'local_name': 'Cook Iislands'},
    'CI':{'code': 'ci', 'name': 'Ivory Coast', 'local_name': 'Ivory Coast'},
    'CH':{'code': 'ch', 'name': 'Switzerland', 'local_name': 'Switzerland'},
    'CO':{'code': 'co', 'name': 'Colombia', 'local_name': 'Colombia'},
    'CN':{'code': 'cn', 'name': 'China', 'local_name': 'China'},
    'CM':{'code': 'cm', 'name': 'Cameroon', 'local_name': 'Cameroon'},
    'CL':{'code': 'cl', 'name': 'Chile', 'local_name': 'Chile'},
    'CC':{'code': 'cc', 'name': 'Cocos (Keeling) Islands', 'local_name': 'Cocos (Keeling) Islands'},
    'CA':{'code': 'ca', 'name': 'Canada', 'local_name': 'Canada'},
    'CG':{'code': 'cg', 'name': 'Congo', 'local_name': 'Congo'},
    'CF':{'code': 'cf', 'name': 'Central African Republic', 'local_name': 'Central African Republic'},
    'CZ':{'code': 'cz', 'name': 'Czech Republic', 'local_name': 'Czech Republic'},
    'CY':{'code': 'cy', 'name': 'Cyprus', 'local_name': 'Cyprus'},
    'CX':{'code': 'cx', 'name': 'Christmas Island', 'local_name': 'Christmas Island'},
    'CR':{'code': 'cr', 'name': 'Costa Rica', 'local_name': 'Costa Rica'},
    'CV':{'code': 'cv', 'name': 'Cape Verde', 'local_name': 'Cape Verde'},
    'CU':{'code': 'cu', 'name': 'Cuba', 'local_name': 'Cuba'},
    'SZ':{'code': 'sz', 'name': 'Swaziland', 'local_name': 'Swaziland'},
    'SY':{'code': 'sy', 'name': 'Syrian Arab Republic', 'local_name': 'Syrian Arab Republic'},
    'SR':{'code': 'sr', 'name': 'Suriname', 'local_name': 'Suriname'},
    'SV':{'code': 'sv', 'name': 'El Salvador', 'local_name': 'El Salvador'},
    'ST':{'code': 'st', 'name': 'Sao Tome & Principe', 'local_name': 'Sao Tome & Principe'},
    'SK':{'code': 'sk', 'name': 'Slovakia', 'local_name': 'Slovakia'},
    'SJ':{'code': 'sj', 'name': 'Svalbard & Jan Mayen Islands', 'local_name': 'Svalbard & Jan Mayen Islands'},
    'SI':{'code': 'si', 'name': 'Slovenia', 'local_name': 'Slovenia'},
    'SH':{'code': 'sh', 'name': 'St. Helena', 'local_name': 'St. Helena'},
    'SO':{'code': 'so', 'name': 'Somalia', 'local_name': 'Somalia'},
    'SN':{'code': 'sn', 'name': 'Senegal', 'local_name': 'Senegal'},
    'SM':{'code': 'sm', 'name': 'San Marino', 'local_name': 'San Marino'},
    'SL':{'code': 'sl', 'name': 'Sierra Leone', 'local_name': 'Sierra Leone'},
    'SC':{'code': 'sc', 'name': 'Seychelles', 'local_name': 'Seychelles'},
    'SB':{'code': 'sb', 'name': 'Solomon Islands', 'local_name': 'Solomon Islands'},
    'SA':{'code': 'sa', 'name': 'Saudi Arabia', 'local_name': 'Saudi Arabia'},
    'SG':{'code': 'sg', 'name': 'Singapore', 'local_name': 'Singapore'},
    'SE':{'code': 'se', 'name': 'Sweden', 'local_name': 'Sweden'},
    'SD':{'code': 'sd', 'name': 'Sudan', 'local_name': 'Sudan'},
    'YE':{'code': 'ye', 'name': 'Yemen', 'local_name': 'Yemen'},
    'YU':{'code': 'yu', 'name': 'Yugoslavia', 'local_name': 'Yugoslavia'},
    'YT':{'code': 'yt', 'name': 'Mayotte', 'local_name': 'Mayotte'},
    'LB':{'code': 'lb', 'name': 'Lebanon', 'local_name': 'Lebanon'},
    'LC':{'code': 'lc', 'name': 'Saint Lucia', 'local_name': 'Saint Lucia'},
    'LA':{'code': 'la', 'name': "Lao People's Democratic Republic", 'local_name': "Lao People's Democratic Republic"},
    'LK':{'code': 'lk', 'name': 'Sri Lanka', 'local_name': 'Sri Lanka'},
    'LI':{'code': 'li', 'name': 'Liechtenstein', 'local_name': 'Liechtenstein'},
    'LV':{'code': 'lv', 'name': 'Latvia', 'local_name': 'Latvia'},
    'LT':{'code': 'lt', 'name': 'Lithuania', 'local_name': 'Lithuania'},
    'LU':{'code': 'lu', 'name': 'Luxembourg', 'local_name': 'Luxembourg'},
    'LR':{'code': 'lr', 'name': 'Liberia', 'local_name': 'Liberia'},
    'LS':{'code': 'ls', 'name': 'Lesotho', 'local_name': 'Lesotho'},
    'LY':{'code': 'ly', 'name': 'Libyan Arab Jamahiriya', 'local_name': 'Libyan Arab Jamahiriya'},
    'VA':{'code': 'va', 'name': 'Vatican City State (Holy See)', 'local_name': 'Vatican City State (Holy See)'},
    'VC':{'code': 'vc', 'name': 'St. Vincent & the Grenadines', 'local_name': 'St. Vincent & the Grenadines'},
    'VE':{'code': 've', 'name': 'Venezuela', 'local_name': 'Venezuela'},
    'VG':{'code': 'vg', 'name': 'British Virgin Islands', 'local_name': 'British Virgin Islands'},
    'IQ':{'code': 'iq', 'name': 'Iraq', 'local_name': 'Iraq'},
    'VI':{'code': 'vi', 'name': 'United States Virgin Islands', 'local_name': 'United States Virgin Islands'},
    'IS':{'code': 'is', 'name': 'Iceland', 'local_name': 'Iceland'},
    'IR':{'code': 'ir', 'name': 'Islamic Republic of Iran', 'local_name': 'Islamic Republic of Iran'},
    'IT':{'code': 'it', 'name': 'Italy', 'local_name': 'Italy'},
    'VN':{'code': 'vn', 'name': 'Viet Nam', 'local_name': 'Viet Nam'},
    'IL':{'code': 'il', 'name': 'Israel', 'local_name': 'Israel'},
    'IO':{'code': 'io', 'name': 'British Indian Ocean Territory', 'local_name': 'British Indian Ocean Territory'},
    'IN':{'code': 'in', 'name': 'India', 'local_name': 'India'},
    'IE':{'code': 'ie', 'name': 'Ireland', 'local_name': 'Ireland'},
    'ID':{'code': 'id', 'name': 'Indonesia', 'local_name': 'Indonesia'},
    'BD':{'code': 'bd', 'name': 'Bangladesh', 'local_name': 'Bangladesh'},
    'BE':{'code': 'be', 'name': 'Belgium', 'local_name': 'Belgium'},
    'BF':{'code': 'bf', 'name': 'Burkina Faso', 'local_name': 'Burkina Faso'},
    'BG':{'code': 'bg', 'name': 'Bulgaria', 'local_name': 'Bulgaria'},
    'BA':{'code': 'ba', 'name': 'Bosnia and Herzegovina', 'local_name': 'Bosnia and Herzegovina'},
    'BB':{'code': 'bb', 'name': 'Barbados', 'local_name': 'Barbados'},
    'BM':{'code': 'bm', 'name': 'Bermuda', 'local_name': 'Bermuda'},
    'BN':{'code': 'bn', 'name': 'Brunei Darussalam', 'local_name': 'Brunei Darussalam'},
    'BO':{'code': 'bo', 'name': 'Bolivia', 'local_name': 'Bolivia'},
    'BH':{'code': 'bh', 'name': 'Bahrain', 'local_name': 'Bahrain'},
    'BI':{'code': 'bi', 'name': 'Burundi', 'local_name': 'Burundi'},
    'BJ':{'code': 'bj', 'name': 'Benin', 'local_name': 'Benin'},
    'BT':{'code': 'bt', 'name': 'Bhutan', 'local_name': 'Bhutan'},
    'BV':{'code': 'bv', 'name': 'Bouvet Island', 'local_name': 'Bouvet Island'},
    'BW':{'code': 'bw', 'name': 'Botswana', 'local_name': 'Botswana'},
    'BR':{'code': 'br', 'name': 'Brazil', 'local_name': 'Brazil'},
    'BS':{'code': 'bs', 'name': 'Bahama', 'local_name': 'Bahama'},
    'BY':{'code': 'by', 'name': 'Belarus', 'local_name': 'Belarus'},
    'BZ':{'code': 'bz', 'name': 'Belize', 'local_name': 'Belize'},
    'RU':{'code': 'ru', 'name': 'Russian Federation', 'local_name': 'Russian Federation'},
    'RW':{'code': 'rw', 'name': 'Rwanda', 'local_name': 'Rwanda'},
    'RE':{'code': 're', 'name': 'Reunion', 'local_name': 'Reunion'},
    'RO':{'code': 'ro', 'name': 'Romania', 'local_name': 'Romania'},
    'OM':{'code': 'om', 'name': 'Oman', 'local_name': 'Oman'},
    'HR':{'code': 'hr', 'name': 'Croatia', 'local_name': 'Croatia'},
    'HT':{'code': 'ht', 'name': 'Haiti', 'local_name': 'Haiti'},
    'HU':{'code': 'hu', 'name': 'Hungary', 'local_name': 'Hungary'},
    'HK':{'code': 'hk', 'name': 'Hong Kong', 'local_name': 'Hong Kong'},
    'HN':{'code': 'hn', 'name': 'Honduras', 'local_name': 'Honduras'},
    'HM':{'code': 'hm', 'name': 'Heard & McDonald Islands', 'local_name': 'Heard & McDonald Islands'},
    'EH':{'code': 'eh', 'name': 'Western Sahara', 'local_name': 'Western Sahara'},
    'EE':{'code': 'ee', 'name': 'Estonia', 'local_name': 'Estonia'},
    'EG':{'code': 'eg', 'name': 'Egypt', 'local_name': 'Egypt'},
    'EC':{'code': 'ec', 'name': 'Ecuador', 'local_name': 'Ecuador'},
    'ET':{'code': 'et', 'name': 'Ethiopia', 'local_name': 'Ethiopia'},
    'ES':{'code': 'es', 'name': 'Spain', 'local_name': 'Spain'},
    'ER':{'code': 'er', 'name': 'Eritrea', 'local_name': 'Eritrea'},
    'UY':{'code': 'uy', 'name': 'Uruguay', 'local_name': 'Uruguay'},
    'UZ':{'code': 'uz', 'name': 'Uzbekistan', 'local_name': 'Uzbekistan'},
    'US':{'code': 'us', 'name': 'United States of America', 'local_name': 'United States of America'},
    'UM':{'code': 'um', 'name': 'United States Minor Outlying Islands', 'local_name': 'United States Minor Outlying Islands'},
    'UG':{'code': 'ug', 'name': 'Uganda', 'local_name': 'Uganda'},
    'UA':{'code': 'ua', 'name': 'Ukraine', 'local_name': 'Ukraine'},
    'VU':{'code': 'vu', 'name': 'Vanuatu', 'local_name': 'Vanuatu'},
    'NI':{'code': 'ni', 'name': 'Nicaragua', 'local_name': 'Nicaragua'},
    'NL':{'code': 'nl', 'name': 'Netherlands', 'local_name': 'Netherlands'},
    'NO':{'code': 'no', 'name': 'Norway', 'local_name': 'Norway'},
    'NA':{'code': 'na', 'name': 'Namibia', 'local_name': 'Namibia'},
    'NC':{'code': 'nc', 'name': 'New Caledonia', 'local_name': 'New Caledonia'},
    'NE':{'code': 'ne', 'name': 'Niger', 'local_name': 'Niger'},
    'NF':{'code': 'nf', 'name': 'Norfolk Island', 'local_name': 'Norfolk Island'},
    'NG':{'code': 'ng', 'name': 'Nigeria', 'local_name': 'Nigeria'},
    'NZ':{'code': 'nz', 'name': 'New Zealand', 'local_name': 'New Zealand'},
    'NP':{'code': 'np', 'name': 'Nepal', 'local_name': 'Nepal'},
    'NR':{'code': 'nr', 'name': 'Nauru', 'local_name': 'Nauru'},
    'NU':{'code': 'nu', 'name': 'Niue', 'local_name': 'Niue'},
    'KG':{'code': 'kg', 'name': 'Kyrgyzstan', 'local_name': 'Kyrgyzstan'},
    'KE':{'code': 'ke', 'name': 'Kenya', 'local_name': 'Kenya'},
    'KI':{'code': 'ki', 'name': 'Kiribati', 'local_name': 'Kiribati'},
    'KH':{'code': 'kh', 'name': 'Cambodia', 'local_name': 'Cambodia'},
    'KN':{'code': 'kn', 'name': 'St. Kitts and Nevis', 'local_name': 'St. Kitts and Nevis'},
    'KM':{'code': 'km', 'name': 'Comoros', 'local_name': 'Comoros'},
    'KR':{'code': 'kr', 'name': 'Korea, Republic of', 'local_name': 'Korea, Republic of'},
    'KP':{'code': 'kp', 'name': "Korea, Democratic People's Republic of", 'local_name': "Korea, Democratic People's Republic of"},
    'KW':{'code': 'kw', 'name': 'Kuwait', 'local_name': 'Kuwait'},
    'KZ':{'code': 'kz', 'name': 'Kazakhstan', 'local_name': 'Kazakhstan'},
    'KY':{'code': 'ky', 'name': 'Cayman Islands', 'local_name': 'Cayman Islands'},
    'DO':{'code': 'do', 'name': 'Dominican Republic', 'local_name': 'Dominican Republic'},
    'DM':{'code': 'dm', 'name': 'Dominica', 'local_name': 'Dominica'},
    'DJ':{'code': 'dj', 'name': 'Djibouti', 'local_name': 'Djibouti'},
    'DK':{'code': 'dk', 'name': 'Denmark', 'local_name': 'Denmark'},
    'DE':{'code': 'de', 'name': 'Germany', 'local_name': 'Germany'},
    'DZ':{'code': 'dz', 'name': 'Algeria', 'local_name': 'Algeria'},
    'TZ':{'code': 'tz', 'name': 'Tanzania, United Republic of', 'local_name': 'Tanzania, United Republic of'},
    'TV':{'code': 'tv', 'name': 'Tuvalu', 'local_name': 'Tuvalu'},
    'TW':{'code': 'tw', 'name': 'Taiwan, Province of China', 'local_name': 'Taiwan, Province of China'},
    'TT':{'code': 'tt', 'name': 'Trinidad & Tobago', 'local_name': 'Trinidad & Tobago'},
    'TR':{'code': 'tr', 'name': 'Turkey', 'local_name': 'Turkey'},
    'TP':{'code': 'tp', 'name': 'East Timor', 'local_name': 'East Timor'},
    'TN':{'code': 'tn', 'name': 'Tunisia', 'local_name': 'Tunisia'},
    'TO':{'code': 'to', 'name': 'Tonga', 'local_name': 'Tonga'},
    'TM':{'code': 'tm', 'name': 'Turkmenistan', 'local_name': 'Turkmenistan'},
    'TJ':{'code': 'tj', 'name': 'Tajikistan', 'local_name': 'Tajikistan'},
    'TK':{'code': 'tk', 'name': 'Tokelau', 'local_name': 'Tokelau'},
    'TH':{'code': 'th', 'name': 'Thailand', 'local_name': 'Thailand'},
    'TF':{'code': 'tf', 'name': 'French Southern Territories', 'local_name': 'French Southern Territories'},
    'TG':{'code': 'tg', 'name': 'Togo', 'local_name': 'Togo'},
    'TD':{'code': 'td', 'name': 'Chad', 'local_name': 'Chad'},
    'TC':{'code': 'tc', 'name': 'Turks & Caicos Islands', 'local_name': 'Turks & Caicos Islands'},
    'AE':{'code': 'ae', 'name': 'United Arab Emirates', 'local_name': 'United Arab Emirates'},
    'AD':{'code': 'ad', 'name': 'Andorra', 'local_name': 'Andorra'},
    'AG':{'code': 'ag', 'name': 'Antigua & Barbuda', 'local_name': 'Antigua & Barbuda'},
    'AF':{'code': 'af', 'name': 'Afghanistan', 'local_name': 'Afghanistan'},
    'AI':{'code': 'ai', 'name': 'Anguilla', 'local_name': 'Anguilla'},
    'AM':{'code': 'am', 'name': 'Armenia', 'local_name': 'Armenia'},
    'AL':{'code': 'al', 'name': 'Albania', 'local_name': 'Albania'},
    'AO':{'code': 'ao', 'name': 'Angola', 'local_name': 'Angola'},
    'AN':{'code': 'an', 'name': 'Netherlands Antilles', 'local_name': 'Netherlands Antilles'},
    'AQ':{'code': 'aq', 'name': 'Antarctica', 'local_name': 'Antarctica'},
    'AS':{'code': 'as', 'name': 'American Samoa', 'local_name': 'American Samoa'},
    'AR':{'code': 'ar', 'name': 'Argentina', 'local_name': 'Argentina'},
    'AU':{'code': 'au', 'name': 'Australia', 'local_name': 'Australia'},
    'AT':{'code': 'at', 'name': 'Austria', 'local_name': 'Austria'},
    'AW':{'code': 'aw', 'name': 'Aruba', 'local_name': 'Aruba'},
    'AZ':{'code': 'az', 'name': 'Azerbaijan', 'local_name': 'Azerbaijan'},
    'QA':{'code': 'qa', 'name': 'Qatar', 'local_name': 'Qatar'},
}
