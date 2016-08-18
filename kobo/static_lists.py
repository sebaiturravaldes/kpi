from django.utils.translation import ugettext_lazy as _

'''
This file is a place to store static, translatable lists (or tuples!). Choice
lists for registration fields were the original application.
'''

SECTORS = (
    # (value, human-readable label)
    ("Public Administration", _("Public Administration")),
    ("Arts, Entertainment, and Recreation", _("Arts, Entertainment, and Recreation")),
    ("Educational Services / Higher Education", _("Educational Services / Higher Education")),
    ("Health Services / Public Health", _("Health Services / Public Health")),
    ("Finance and Insurance", _("Finance and Insurance")),
    ("Information / Media", _("Information / Media")),
    ("Economic/Social Development", _("Economic/Social Development")),
    ("Security / Police / Peacekeeping", _("Security / Police / Peacekeeping")),
    ("Disarmament & Demobilization", _("Disarmament & Demobilization")),
    ("Environment", _("Environment")),
    ("Private sector", _("Private sector")),
    ("Humanitarian - Coordination / Information Management", _("Humanitarian - Coordination / Information Management")),
    ("Humanitarian - Multiple Clusters", _("Humanitarian - Multiple Clusters")),
    ("Humanitarian - Camp Management & Coordination", _("Humanitarian - Camp Management & Coordination")),
    ("Humanitarian - Early Recovery", _("Humanitarian - Early Recovery")),
    ("Humanitarian - Education", _("Humanitarian - Education")),
    ("Humanitarian - Emergency Shelter", _("Humanitarian - Emergency Shelter")),
    ("Humanitarian - Emergency Telecoms", _("Humanitarian - Emergency Telecoms")),
    ("Humanitarian - Food Security", _("Humanitarian - Food Security")),
    ("Humanitarian - Health", _("Humanitarian - Health")),
    ("Humanitarian - Logistics", _("Humanitarian - Logistics")),
    ("Humanitarian - Nutrition", _("Humanitarian - Nutrition")),
    ("Humanitarian - Protection", _("Humanitarian - Protection")),
    ("Humanitarian - Sanitation, Water & Hygiene", _("Humanitarian - Sanitation, Water & Hygiene")),
    ("Other", _("Other")),
)

'''
You might generate such a list of countries with code like this:

    from __future__ import print_function
    import requests
    import sys

    url = 'https://www.humanitarianresponse.info/api/v1.0/locations?filter[admin_level]=0'
    while url:
        print('Fetching', url, file=sys.stderr)
        response = requests.get(url)
        j = response.json()
        if 'next' in j:
            url = j['next']['href']
        else:
            url = None
        for d in j['data']:
            print("({}, _({}))".format(repr(d['iso3']), repr(d['label'])))
'''

COUNTRIES = (
    # (value, human-readable label)
    (u'AFG', _(u'Afghanistan')),
    (u'ALA', _(u'\xc5land Islands')),
    (u'ALB', _(u'Albania')),
    (u'DZA', _(u'Algeria')),
    (u'ASM', _(u'American Samoa')),
    (u'AND', _(u'Andorra')),
    (u'AGO', _(u'Angola')),
    (u'AIA', _(u'Anguilla')),
    (u'ATA', _(u'Antarctica')),
    (u'ATG', _(u'Antigua and Barbuda')),
    (u'ARG', _(u'Argentina')),
    (u'ARM', _(u'Armenia')),
    (u'ABW', _(u'Aruba')),
    (u'AUS', _(u'Australia')),
    (u'AUT', _(u'Austria')),
    (u'AZE', _(u'Azerbaijan')),
    (u'BHS', _(u'Bahamas')),
    (u'BHR', _(u'Bahrain')),
    (u'BGD', _(u'Bangladesh')),
    (u'BRB', _(u'Barbados')),
    (u'BLR', _(u'Belarus')),
    (u'BEL', _(u'Belgium')),
    (u'BLZ', _(u'Belize')),
    (u'BEN', _(u'Benin')),
    (u'BMU', _(u'Bermuda')),
    (u'BTN', _(u'Bhutan')),
    (u'BOL', _(u'Bolivia, Plurinational State of')),
    (u'BIH', _(u'Bosnia and Herzegovina')),
    (u'BES', _(u'Bonaire, Sint Eustatius and Saba')),
    (u'BWA', _(u'Botswana')),
    (u'BVT', _(u'Bouvet Island')),
    (u'BRA', _(u'Brazil')),
    (u'IOT', _(u'British Indian Ocean Territory')),
    (u'BRN', _(u'Brunei Darussalam')),
    (u'BGR', _(u'Bulgaria')),
    (u'BFA', _(u'Burkina Faso')),
    (u'BDI', _(u'Burundi')),
    (u'KHM', _(u'Cambodia')),
    (u'CMR', _(u'Cameroon')),
    (u'CAN', _(u'Canada')),
    (u'CPV', _(u'Cape Verde')),
    (u'CYM', _(u'Cayman Islands')),
    (u'CAF', _(u'Central African Republic')),
    (u'TCD', _(u'Chad')),
    (u'CHL', _(u'Chile')),
    (u'CHN', _(u'China')),
    (u'CXR', _(u'Christmas Island')),
    (u'CCK', _(u'Cocos (Keeling) Islands')),
    (u'COL', _(u'Colombia')),
    (u'COM', _(u'Comoros')),
    (u'COG', _(u'Congo')),
    (u'COD', _(u'Congo, The Democratic Republic of the')),
    (u'COK', _(u'Cook Islands')),
    (u'CRI', _(u'Costa Rica')),
    (u'CIV', _(u"C\xf4te d'Ivoire")),
    (u'HRV', _(u'Croatia')),
    (u'CUB', _(u'Cuba')),
    (u'CUW', _(u'Cura\xe7ao')),
    (u'CYP', _(u'Cyprus')),
    (u'CZE', _(u'Czech Republic')),
    (u'DNK', _(u'Denmark')),
    (u'DJI', _(u'Djibouti')),
    (u'DMA', _(u'Dominica')),
    (u'DOM', _(u'Dominican Republic')),
    (u'ECU', _(u'Ecuador')),
    (u'EGY', _(u'Egypt')),
    (u'SLV', _(u'El Salvador')),
    (u'GNQ', _(u'Equatorial Guinea')),
    (u'ERI', _(u'Eritrea')),
    (u'EST', _(u'Estonia')),
    (u'ETH', _(u'Ethiopia')),
    (u'FLK', _(u'Falkland Islands (Malvinas)')),
    (u'FRO', _(u'Faroe Islands')),
    (u'FJI', _(u'Fiji')),
    (u'FIN', _(u'Finland')),
    (u'FRA', _(u'France')),
    (u'GUF', _(u'French Guiana')),
    (u'PYF', _(u'French Polynesia')),
    (u'ATF', _(u'French Southern Territories')),
    (u'GAB', _(u'Gabon')),
    (u'GMB', _(u'Gambia')),
    (u'GEO', _(u'Georgia')),
    (u'DEU', _(u'Germany')),
    (u'GHA', _(u'Ghana')),
    (u'GIB', _(u'Gibraltar')),
    (u'GRC', _(u'Greece')),
    (u'GRL', _(u'Greenland')),
    (u'GRD', _(u'Grenada')),
    (u'GLP', _(u'Guadeloupe')),
    (u'GUM', _(u'Guam')),
    (u'GTM', _(u'Guatemala')),
    (u'GGY', _(u'Guernsey')),
    (u'GIN', _(u'Guinea')),
    (u'GNB', _(u'Guinea-Bissau')),
    (u'GUY', _(u'Guyana')),
    (u'HTI', _(u'Haiti')),
    (u'HMD', _(u'Heard Island and McDonald Islands')),
    (u'VAT', _(u'Holy See (Vatican City State)')),
    (u'HND', _(u'Honduras')),
    (u'HKG', _(u'Hong Kong')),
    (u'HUN', _(u'Hungary')),
    (u'ISL', _(u'Iceland')),
    (u'IND', _(u'India')),
    (u'IDN', _(u'Indonesia')),
    (u'IRN', _(u'Iran, Islamic Republic of')),
    (u'IRQ', _(u'Iraq')),
    (u'IRL', _(u'Ireland')),
    (u'IMN', _(u'Isle of Man')),
    (u'ISR', _(u'Israel')),
    (u'ITA', _(u'Italy')),
    (u'JAM', _(u'Jamaica')),
    (u'JPN', _(u'Japan')),
    (u'JEY', _(u'Jersey')),
    (u'JOR', _(u'Jordan')),
    (u'KAZ', _(u'Kazakhstan')),
    (u'KEN', _(u'Kenya')),
    (u'KIR', _(u'Kiribati')),
    (u'PRK', _(u"Korea, Democratic People's Republic of")),
    (u'KOR', _(u'Korea, Republic of')),
    (u'KWT', _(u'Kuwait')),
    (u'KGZ', _(u'Kyrgyzstan')),
    (u'LAO', _(u"Lao People's Democratic Republic")),
    (u'LVA', _(u'Latvia')),
    (u'LBN', _(u'Lebanon')),
    (u'LSO', _(u'Lesotho')),
    (u'LBR', _(u'Liberia')),
    (u'LBY', _(u'Libya')),
    (u'LIE', _(u'Liechtenstein')),
    (u'LTU', _(u'Lithuania')),
    (u'LUX', _(u'Luxembourg')),
    (u'MAC', _(u'Macao')),
    (u'MKD', _(u'Macedonia, The Former Yugoslav Republic of')),
    (u'MDG', _(u'Madagascar')),
    (u'MWI', _(u'Malawi')),
    (u'MYS', _(u'Malaysia')),
    (u'MDV', _(u'Maldives')),
    (u'MLI', _(u'Mali')),
    (u'MLT', _(u'Malta')),
    (u'MHL', _(u'Marshall Islands')),
    (u'MTQ', _(u'Martinique')),
    (u'MRT', _(u'Mauritania')),
    (u'MUS', _(u'Mauritius')),
    (u'MYT', _(u'Mayotte')),
    (u'MEX', _(u'Mexico')),
    (u'FSM', _(u'Micronesia, Federated States of')),
    (u'MDA', _(u'Moldova, Republic of')),
    (u'MCO', _(u'Monaco')),
    (u'MNG', _(u'Mongolia')),
    (u'MNE', _(u'Montenegro')),
    (u'MSR', _(u'Montserrat')),
    (u'MAR', _(u'Morocco')),
    (u'MOZ', _(u'Mozambique')),
    (u'MMR', _(u'Myanmar')),
    (u'NAM', _(u'Namibia')),
    (u'NRU', _(u'Nauru')),
    (u'NPL', _(u'Nepal')),
    (u'NLD', _(u'Netherlands')),
    (u'ANT', _(u'Netherlands Antilles')),
    (u'NCL', _(u'New Caledonia')),
    (u'NZL', _(u'New Zealand')),
    (u'NIC', _(u'Nicaragua')),
    (u'NER', _(u'Niger')),
    (u'NGA', _(u'Nigeria')),
    (u'NIU', _(u'Niue')),
    (u'NFK', _(u'Norfolk Island')),
    (u'MNP', _(u'Northern Mariana Islands')),
    (u'NOR', _(u'Norway')),
    (u'OMN', _(u'Oman')),
    (u'PAK', _(u'Pakistan')),
    (u'PLW', _(u'Palau')),
    (u'PSE', _(u'occupied Palestinian territory')),
    (u'PAN', _(u'Panama')),
    (u'PNG', _(u'Papua New Guinea')),
    (u'PRY', _(u'Paraguay')),
    (u'PER', _(u'Peru')),
    (u'PHL', _(u'Philippines')),
    (u'PCN', _(u'Pitcairn')),
    (u'POL', _(u'Poland')),
    (u'PRT', _(u'Portugal')),
    (u'PRI', _(u'Puerto Rico')),
    (u'QAT', _(u'Qatar')),
    (u'REU', _(u'R\xe9union')),
    (u'ROU', _(u'Romania')),
    (u'RUS', _(u'Russian Federation')),
    (u'RWA', _(u'Rwanda')),
    (u'BLM', _(u'Saint Barth\xe9lemy')),
    (u'SHN', _(u'Saint Helena, Ascension and Tristan da Cunha')),
    (u'KNA', _(u'Saint Kitts and Nevis')),
    (u'LCA', _(u'Saint Lucia')),
    (u'MAF', _(u'Saint Martin (French part)')),
    (u'SPM', _(u'Saint Pierre and Miquelon')),
    (u'VCT', _(u'Saint Vincent and the Grenadines')),
    (u'WSM', _(u'Samoa')),
    (u'SMR', _(u'San Marino')),
    (u'STP', _(u'S\xe3o Tom\xe9 and Pr\xedncipe')),
    (u'SAU', _(u'Saudi Arabia')),
    (u'SEN', _(u'Senegal')),
    (u'SRB', _(u'Serbia')),
    (u'SYC', _(u'Seychelles')),
    (u'SLE', _(u'Sierra Leone')),
    (u'SGP', _(u'Singapore')),
    (u'SXM', _(u'Sint Maarten (Dutch part)')),
    (u'SVK', _(u'Slovakia')),
    (u'SVN', _(u'Slovenia')),
    (u'SLB', _(u'Solomon Islands')),
    (u'SOM', _(u'Somalia')),
    (u'ZAF', _(u'South Africa')),
    (u'SGS', _(u'South Georgia and the South Sandwich Islands')),
    (u'ESP', _(u'Spain')),
    (u'LKA', _(u'Sri Lanka')),
    (u'SSD', _(u'South Sudan')),
    (u'SDN', _(u'Sudan')),
    (u'SUR', _(u'Suriname')),
    (u'SJM', _(u'Svalbard and Jan Mayen')),
    (u'SWZ', _(u'Swaziland')),
    (u'SWE', _(u'Sweden')),
    (u'CHE', _(u'Switzerland')),
    (u'SYR', _(u'Syrian Arab Republic')),
    (u'TWN', _(u'Taiwan, Province of China')),
    (u'TJK', _(u'Tajikistan')),
    (u'TZA', _(u'Tanzania, United Republic of')),
    (u'THA', _(u'Thailand')),
    (u'TLS', _(u'Timor-Leste')),
    (u'TGO', _(u'Togo')),
    (u'TKL', _(u'Tokelau')),
    (u'TON', _(u'Tonga')),
    (u'TTO', _(u'Trinidad and Tobago')),
    (u'TUN', _(u'Tunisia')),
    (u'TUR', _(u'Turkey')),
    (u'TKM', _(u'Turkmenistan')),
    (u'TCA', _(u'Turks and Caicos Islands')),
    (u'TUV', _(u'Tuvalu')),
    (u'UGA', _(u'Uganda')),
    (u'UKR', _(u'Ukraine')),
    (u'ARE', _(u'United Arab Emirates')),
    (u'GBR', _(u'United Kingdom')),
    (u'USA', _(u'United States')),
    (u'UMI', _(u'United States Minor Outlying Islands')),
    (u'URY', _(u'Uruguay')),
    (u'UZB', _(u'Uzbekistan')),
    (u'VUT', _(u'Vanuatu')),
    (u'VEN', _(u'Venezuela, Bolivarian Republic of')),
    (u'VNM', _(u'Viet Nam')),
    (u'VGB', _(u'Virgin Islands, British')),
    (u'VIR', _(u'Virgin Islands, U.S.')),
    (u'WLF', _(u'Wallis and Futuna')),
    (u'ESH', _(u'Western Sahara')),
    (u'YEM', _(u'Yemen')),
    (u'ZMB', _(u'Zambia')),
    (u'ZWE', _(u'Zimbabwe')),
)