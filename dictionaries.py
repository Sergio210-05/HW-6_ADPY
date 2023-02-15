# Lesson 4 -Collections of data. Dictionaries. Sets

# Task N1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# russia_only = []
index = 0
key = None

while index < len(geo_logs):
    key = list(geo_logs[index].keys())
    if 'Россия' not in geo_logs[index][key[0]]:
        geo_logs.pop(index)
    else:
        index += 1

print('Visits in Russia:')
print(geo_logs)
print('\n')

#############################################

# Task N2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_id = set()
for geo_list in ids.values():
    unique_id.update(geo_list)
unique_id_list = list(unique_id)
print('Unique values:', unique_id_list)
print('\n')


############################################

# Task N3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

accuracy = 2
queries_list = []
letter_quantity = []

for search in queries:
    search_words = search.split()
    for index, words in enumerate(search_words):
        search_words[index] = words.strip(',.!;:&*?+-*/=_()#@"')
    index = 0
    while index < len(search_words):
        if search_words[index] == '':
            del search_words[index]
        else:
            index += 1
    letter_quantity.append(len(search_words))
    queries_list.append(search_words)
set_let_quan = set(letter_quantity)
total = 0
for num in sorted(list(set_let_quan)):
    repeat = round(letter_quantity.count(num) / len(letter_quantity) * 100,
                   accuracy)
    dev = round(abs(100 - (total + repeat)), accuracy)
    if dev == round(1 / 10 ** accuracy, accuracy):
        repeat = round(100 - total, accuracy)
    total = round(total + repeat, 10)
    print(f'Search queries from {num} word(s) - {repeat}%')

print('\n')


############################################################################

# Task N4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
sales = [sale for sale in stats.values()]
# print(sales)
best_sites = []
for site, sale in stats.items():
    if sale == max(sales):
        print(f'Maximum-statistic site is {site} with {sale} sales')
        best_sites.append(site)

print('\n')

############################################################################

# Task N5

some_list = ['2018-01-01', 'yandex', 'cpc', 100]
new_list = some_list[::]
new_dict = {}
# index = -1

# while abs(index) < len(new_list):
while len(new_list) >= 2:
    new_dict = {}
    new_dict[new_list[-2]] = new_list[-1]
    new_list[-2:] = [dict(new_dict)]

print(dict(new_dict))
