# -*- coding: utf-8 -*-
"""
This is the common settings file, intended to set defaults
"""

ALL_LANGUAGES = (
    [u"aa", u"Afar"],
    [u"ab", u"Abkhazian"],
    [u"af", u"Afrikaans"],
    [u"ak", u"Akan"],
    [u"sq", u"Albanian"],
    [u"am", u"Amharic"],
    [u"ar", u"Arabic"],
    [u"an", u"Aragonese"],
    [u"hy", u"Armenian"],
    [u"as", u"Assamese"],
    [u"av", u"Avaric"],
    [u"ae", u"Avestan"],
    [u"ay", u"Aymara"],
    [u"az", u"Azerbaijani"],
    [u"ba", u"Bashkir"],
    [u"bm", u"Bambara"],
    [u"eu", u"Basque"],
    [u"be", u"Belarusian"],
    [u"bn", u"Bengali"],
    [u"bh", u"Bihari languages"],
    [u"bi", u"Bislama"],
    [u"bs", u"Bosnian"],
    [u"br", u"Breton"],
    [u"bg", u"Bulgarian"],
    [u"my", u"Burmese"],
    [u"ca", u"Catalan"],
    [u"ch", u"Chamorro"],
    [u"ce", u"Chechen"],
    [u"zh", u"Chinese"],
    [u"zh_HANS", u"Simplified Chinese"],
    [u"zh_HANT", u"Traditional Chinese"],
    [u"cu", u"Church Slavic"],
    [u"cv", u"Chuvash"],
    [u"kw", u"Cornish"],
    [u"co", u"Corsican"],
    [u"cr", u"Cree"],
    [u"cs", u"Czech"],
    [u"da", u"Danish"],
    [u"dv", u"Divehi"],
    [u"nl", u"Dutch"],
    [u"dz", u"Dzongkha"],
    [u"en", u"English"],
    [u"eo", u"Esperanto"],
    [u"et", u"Estonian"],
    [u"ee", u"Ewe"],
    [u"fo", u"Faroese"],
    [u"fj", u"Fijian"],
    [u"fi", u"Finnish"],
    [u"fr", u"French"],
    [u"fy", u"Western Frisian"],
    [u"ff", u"Fulah"],
    [u"ka", u"Georgian"],
    [u"de", u"German"],
    [u"gd", u"Gaelic"],
    [u"ga", u"Irish"],
    [u"gl", u"Galician"],
    [u"gv", u"Manx"],
    [u"el", u"Greek"],
    [u"gn", u"Guarani"],
    [u"gu", u"Gujarati"],
    [u"ht", u"Haitian"],
    [u"ha", u"Hausa"],
    [u"he", u"Hebrew"],
    [u"hz", u"Herero"],
    [u"hi", u"Hindi"],
    [u"ho", u"Hiri Motu"],
    [u"hr", u"Croatian"],
    [u"hu", u"Hungarian"],
    [u"ig", u"Igbo"],
    [u"is", u"Icelandic"],
    [u"io", u"Ido"],
    [u"ii", u"Sichuan Yi"],
    [u"iu", u"Inuktitut"],
    [u"ie", u"Interlingue"],
    [u"ia", u"Interlingua"],
    [u"id", u"Indonesian"],
    [u"ik", u"Inupiaq"],
    [u"it", u"Italian"],
    [u"jv", u"Javanese"],
    [u"ja", u"Japanese"],
    [u"kl", u"Kalaallisut"],
    [u"kn", u"Kannada"],
    [u"ks", u"Kashmiri"],
    [u"kr", u"Kanuri"],
    [u"kk", u"Kazakh"],
    [u"km", u"Central Khmer"],
    [u"ki", u"Kikuyu"],
    [u"rw", u"Kinyarwanda"],
    [u"ky", u"Kirghiz"],
    [u"kv", u"Komi"],
    [u"kg", u"Kongo"],
    [u"ko", u"Korean"],
    [u"kj", u"Kuanyama"],
    [u"ku", u"Kurdish"],
    [u"lo", u"Lao"],
    [u"la", u"Latin"],
    [u"lv", u"Latvian"],
    [u"li", u"Limburgan"],
    [u"ln", u"Lingala"],
    [u"lt", u"Lithuanian"],
    [u"lb", u"Luxembourgish"],
    [u"lu", u"Luba-Katanga"],
    [u"lg", u"Ganda"],
    [u"mk", u"Macedonian"],
    [u"mh", u"Marshallese"],
    [u"ml", u"Malayalam"],
    [u"mi", u"Maori"],
    [u"mr", u"Marathi"],
    [u"ms", u"Malay"],
    [u"mg", u"Malagasy"],
    [u"mt", u"Maltese"],
    [u"mn", u"Mongolian"],
    [u"na", u"Nauru"],
    [u"nv", u"Navajo"],
    [u"nr", u"Ndebele, South"],
    [u"nd", u"Ndebele, North"],
    [u"ng", u"Ndonga"],
    [u"ne", u"Nepali"],
    [u"nn", u"Norwegian Nynorsk"],
    [u"nb", u"Bokmål, Norwegian"],
    [u"no", u"Norwegian"],
    [u"ny", u"Chichewa"],
    [u"oc", u"Occitan"],
    [u"oj", u"Ojibwa"],
    [u"or", u"Oriya"],
    [u"om", u"Oromo"],
    [u"os", u"Ossetian"],
    [u"pa", u"Panjabi"],
    [u"fa", u"Persian"],
    [u"pi", u"Pali"],
    [u"pl", u"Polish"],
    [u"pt", u"Portuguese"],
    [u"ps", u"Pushto"],
    [u"qu", u"Quechua"],
    [u"rm", u"Romansh"],
    [u"ro", u"Romanian"],
    [u"rn", u"Rundi"],
    [u"ru", u"Russian"],
    [u"sg", u"Sango"],
    [u"sa", u"Sanskrit"],
    [u"si", u"Sinhala"],
    [u"sk", u"Slovak"],
    [u"sl", u"Slovenian"],
    [u"se", u"Northern Sami"],
    [u"sm", u"Samoan"],
    [u"sn", u"Shona"],
    [u"sd", u"Sindhi"],
    [u"so", u"Somali"],
    [u"st", u"Sotho, Southern"],
    [u"es", u"Spanish"],
    [u"sc", u"Sardinian"],
    [u"sr", u"Serbian"],
    [u"ss", u"Swati"],
    [u"su", u"Sundanese"],
    [u"sw", u"Swahili"],
    [u"sv", u"Swedish"],
    [u"ty", u"Tahitian"],
    [u"ta", u"Tamil"],
    [u"tt", u"Tatar"],
    [u"te", u"Telugu"],
    [u"tg", u"Tajik"],
    [u"tl", u"Tagalog"],
    [u"th", u"Thai"],
    [u"bo", u"Tibetan"],
    [u"ti", u"Tigrinya"],
    [u"to", u"Tonga (Tonga Islands)"],
    [u"tn", u"Tswana"],
    [u"ts", u"Tsonga"],
    [u"tk", u"Turkmen"],
    [u"tr", u"Turkish"],
    [u"tw", u"Twi"],
    [u"ug", u"Uighur"],
    [u"uk", u"Ukrainian"],
    [u"ur", u"Urdu"],
    [u"uz", u"Uzbek"],
    [u"ve", u"Venda"],
    [u"vi", u"Vietnamese"],
    [u"vo", u"Volapük"],
    [u"cy", u"Welsh"],
    [u"wa", u"Walloon"],
    [u"wo", u"Wolof"],
    [u"xh", u"Xhosa"],
    [u"yi", u"Yiddish"],
    [u"yo", u"Yoruba"],
    [u"za", u"Zhuang"],
    [u"zu", u"Zulu"]
)
