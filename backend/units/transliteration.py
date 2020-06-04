letters = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Ґ': 'G',
    'Д': 'D',
    'Е': 'E',
    'Є': 'JE',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'U',
    'І': 'I',
    'Ї': 'JI',
    'Й': 'J',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SCH',
    'Ь': '',
    'Ю': 'JU',
    'Я': 'JA',
    ' ': '_'
}


def transliteration_ua_eng(text):
    """
    Трансляція українського в анлійський
    для slug url, символи, який немає вище, залишаються такими ж
    """
    formatted_text = '{}'.format(text).upper()
    return ''.join(letters.get(x, x) for x in formatted_text).lower()