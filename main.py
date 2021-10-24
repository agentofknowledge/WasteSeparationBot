import telebot
from telebot import types

bot = telebot.TeleBot("")

# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='пошаговый алгоритм организации раздельного сбора мусора',
                                       callback_data='1')
    keyboard.add(key_1)
    key_2 = types.InlineKeyboardButton(text='категории пластика и их различия', callback_data='2')
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text='пункты приёма вторсырья', callback_data='3')
    keyboard.add(key_3)

    bot.send_message(message.from_user.id, 'Привет! Я - бот, который помогает разобраться в многогранной '
                                           'теме раздельного сбора мусора. Рассказываю о различиях между '
                                           'категориями вторсырья и отдельно углубляюсь в тему пластика. '
                                           'Поделюсь, как и куда сдавать накопленные отходы, а главное - '
                                           'дам пошаговый алгоритм организации раздельного сбора у себя дома '
                                           'без серьёзных и резких изменений в быту. Выбери, что тебе интереснее '
                                           'сейчас узнать:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='пошаговый алгоритм организации раздельного сбора мусора',
                                       callback_data='1')
    keyboard.add(key_1)
    key_2 = types.InlineKeyboardButton(text='категории пластика и их различия', callback_data='2')
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text='пункты приёма вторсырья', callback_data='3')
    keyboard.add(key_3)

    keyboard1 = types.InlineKeyboardMarkup()
    key_4 = types.InlineKeyboardButton(text='дальше', callback_data='4')
    keyboard1.add(key_4)
    key_5 = types.InlineKeyboardButton(text='назад в меню', callback_data='5')
    keyboard1.add(key_5)

    keyboard2 = types.InlineKeyboardMarkup()
    key_6 = types.InlineKeyboardButton(text='дальше', callback_data='6')
    keyboard2.add(key_6)
    key_7 = types.InlineKeyboardButton(text='назад в меню', callback_data='7')
    keyboard2.add(key_7)

    keyboard3 = types.InlineKeyboardMarkup()
    key_8 = types.InlineKeyboardButton(text='дальше', callback_data='8')
    keyboard3.add(key_8)
    key_9 = types.InlineKeyboardButton(text='назад в меню', callback_data='9')
    keyboard3.add(key_9)

    keyboard4 = types.InlineKeyboardMarkup()
    key_10 = types.InlineKeyboardButton(text='дальше', callback_data='10')
    keyboard4.add(key_10)
    key_11 = types.InlineKeyboardButton(text='назад в меню', callback_data='11')
    keyboard4.add(key_11)

    keyboard5 = types.InlineKeyboardMarkup()
    key_12 = types.InlineKeyboardButton(text='дальше', callback_data='12')
    keyboard5.add(key_12)
    key_13 = types.InlineKeyboardButton(text='назад в меню', callback_data='13')
    keyboard5.add(key_13)

    keyboard6 = types.InlineKeyboardMarkup()
    key_14 = types.InlineKeyboardButton(text='назад в меню', callback_data='14')
    keyboard6.add(key_14)

    keyboard7 = types.InlineKeyboardMarkup()
    key_15 = types.InlineKeyboardButton(text='категория 1 - PET', callback_data='15')
    keyboard7.add(key_15)
    key_16 = types.InlineKeyboardButton(text='категория 2 - HDPE', callback_data='16')
    keyboard7.add(key_16)
    key_17 = types.InlineKeyboardButton(text='категория 3 - PVC', callback_data='17')
    keyboard7.add(key_17)
    key_18 = types.InlineKeyboardButton(text='категория 4 - LDPE', callback_data='18')
    keyboard7.add(key_18)
    key_19 = types.InlineKeyboardButton(text='категория 5 - PP', callback_data='19')
    keyboard7.add(key_19)
    key_20 = types.InlineKeyboardButton(text='категория 6 - PS', callback_data='20')
    keyboard7.add(key_20)
    key_21 = types.InlineKeyboardButton(text='категория 7 - O', callback_data='21')
    keyboard7.add(key_21)
    key_22 = types.InlineKeyboardButton(text='общие рекомендации', callback_data='22')
    keyboard7.add(key_22)
    key_23 = types.InlineKeyboardButton(text='назад в меню', callback_data='23')
    keyboard7.add(key_23)

    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Новичок? Не знаешь, с чего начать, и боишься запутаться? '
                                               'Первый совет - не усложняй. Информации о различном вторсырье, проектах раздельного '
                                               'сбора мусора и правилах подготовки отходов в Интернете масса, и это часто пугает начинающих. '
                                               'Тебе не нужно устраивать тотальное разделение по пластику, макулатуре, металлу и прочим '
                                               'отходам с самого начала. Менять свои отношения с мусором стоит постепенно. Итак, твой план '
                                               'действий:')
        bot.send_message(call.message.chat.id, '1. Выяснить информацию о ближайших пунктах раздельного сбора мусора и '
                                               'определить наиболее удобный вариант для себя. Конечно, часто рядом с домом принимают '
                                               'довольно ограниченное количество категорий вторсырья, но твоя задача на первое время - '
                                               'потренироваться, выработать привычку и комфортно настроить свой раздельный сбор. '
                                               'Посмотреть ближайшие пункты приёма вторсырья можно на https://recyclemap.ru/spb.',
                         reply_markup=keyboard1)
    elif call.data == '2':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/oHRt/WdBZTs3as')
        bot.send_message(call.message.chat.id, 'Полиэтилены, полистиролы, полипропилены, полиэтилентерефталаты 🤯 '
                                               'Как не сойти с ума с таким количеством разного пластика, научиться его '
                                               'различать и правильно с ним обращаться? Предлагаю тебе взглянуть на '
                                               'краткую иллюстрированную инструкцию от экологического клуба ITMO GREEN '
                                               '(https://vk.com/itmo_green) университета ИТМО. Выбери категорию, про '
                                               'которую тебе бы хотелось сейчас узнать больше:', reply_markup=keyboard7)
    elif call.data == '3':
        bot.send_message(call.message.chat.id,
                         '- Экотакси - https://vk.com/ecotaxispb (служба доставки вторсырья до пунтов переработки)\n'
                         '- Правила Деления - https://vk.com/pravila.deleniya (экостанции при магазинах "МЕГИ" на Парнасе и Дыбенко)\n'
                         '- Чистые Игры - https://cleangames.org/ (экологические соревнования по уборке и сортировке мусора)\n'
                         '- Акции "РазДельный сбор" - https://vk.com/rsbor (акции по сбору вторсырья во всех районах Петербурга)\n''- Зелёнка сбор - https://zelenka-sbor.ru/ (приём и вывоз вторсырья от частных и юридических лиц на территории Санкт-Петербурга и ЛО)\n'
                         '- 99recycle - https://99recycle.ru/ (производство аксессуаров, сумок, мерча и интерьерной продукции из вторичного сырья; приём вторсырья)\n'
                         '- Собиратор - https://sobirator.ru/ (акции, экоцентр, вывоз вторсырья, блог)\n'
                         '- Зелёный сбор - https://vk.com/green_academy (благотворительный мобильный пункт по бесконтактному приёму вторсырья)\n'
                         '- Фудшеринг - https://vk.com/foodsharing_spb (обмен едой, борьба с перепроизводством)\n'
                         '- Переработкинская - https://vk.com/pererabotkinskaya (пункт приёма вторсырья, эковывоз)\n'
                         '- Крышечки доброты - https://capsgood.ru/ (эколого-благотворительный проект по сбору пластиковых крышечек для помощи детям с особенностями развития)\n'
                         '- Благотворительный фонд "Лепта" - https://lepta.info/ (благотворительный фонд, использующий ненужную одежду для помощи людям)\n'
                         '- "Спасибо" - https://vk.com/kudaotdatveshi (собирает одежду у горожан, затем распределяет её по благотворительным организациям и даёт возможность одеться нуждающимся горожанам)\n'
                         '- Свалка - https://svalka.me/ru/#order (бесплатный сервис по вывозу ненужных вещей)\n'
                         '- 7other - https://vk.com/7other (переработка редких и сложных пластиков)\n\n'
                         'Не забывай, что ближайший к тебе пункт переработки (не обязательно из вышеперечисленных) всегда можно посмотреть на  https://recyclemap.ru/spb.',
                         reply_markup=keyboard6)
    elif call.data == '4':
        bot.send_message(call.message.chat.id, '2. Определиться с тем, что ты будешь сдавать. Долго думать не надо '
                                               '- просто посмотри, что принимают в том самом пункте приёма вторсырья '
                                               'из шага №1. Не обязательно выбирать сразу все категории, прикинь, с '
                                               'чего тебе было бы проще начать. Возможно, ты будешь относить макулатуру '
                                               'в контейнер рядом с домом, батарейки сдавать в ящики от управляющей '
                                               'компании, а пластиковые крышечки - в свой любимый магазин, где их '
                                               'принимают. Вариантов может быть много, поэтому тебе нужно ответить '
                                               'на первые два самых важных вопроса самостоятельно, у каждого всё индивидуально.',
                         reply_markup=keyboard2)
    elif call.data == '5':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)
    elif call.data == '6':
        bot.send_message(call.message.chat.id, '3. Выделить место у себя дома под раздельный сбор мусора. У каждого '
                                               'свои условия по размеру жилья, количеству домочадцев и производимому '
                                               'мусору соответственно. Советую сначала определить один контейнер '
                                               '(коробку, пакет и т.д.), куда будет складываться всё вторсырьё, что '
                                               'ты решил сдавать на начальном этапе. Как только контейнер наполнится, '
                                               'разложи всё по категориям и отнеси вторсырьё в пункт приёма. '
                                               'Со временем тебе станет понятно, какие категории набираются в доме '
                                               'быстрее, а какие наоборот. Тогда при желании для некоторых категорий '
                                               'можно выделить своё отдельное место. Или оставить всё, как есть, если '
                                               'тебе это удобно.', reply_markup=keyboard3)
    elif call.data == '7':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)
    elif call.data == '8':
        bot.send_message(call.message.chat.id, '4. Выяснить для себя, что такое маркировка, как она выглядит и как в '
                                               'ней разбираться. Эта информация поможет тебе в дальнейшем при определении '
                                               'видов вторсырья, ведь, например, только одного пластика существует 7 '
                                               'категорий! Смешивать их между собой при сдаче нельзя, так как при переработке '
                                               'получится некачественный материал. Более того, очень редко бывает такое, что в '
                                               'один пункт приёма можно сдать сразу все категории. К тому же есть разделение '
                                               'на твёрдый и мягкий пластик. Обо всём этом можно почитать в статье проекта '
                                               '"Раздельный сбор" - https://rsbor.ru/where-to-start/kak-razobratsya-v-markirovkax/. '
                                               'Сверяйся со списком принимаемого вторсырья в пункте приёма и сдавай только необходимое!',
                         reply_markup=keyboard4)
    elif call.data == '9':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)
    elif call.data == '10':
        bot.send_message(call.message.chat.id, '5. Изучить правила подготовки вторсырья. Да, это ещё одна тонкость, '
                                               'которую придётся учитывать при сдаче, ведь у приёмщиков нет возможности '
                                               'вручную подготавливать каждый отход на проивзодстве. У каждого эти '
                                               'правила свои, но есть и некоторые общие моменты:\n'
                                               '- сдавай всё сухим и чистым (как минимум ополосни вторсырьё от '
                                               'остатков пищи и других загрязнений)\n'
                                               '- уменьшай объём вторсырья, насколько это возможно (например, '
                                               'сплющи консервные банки и пластиковые бутылки, разложи тетрапак в '
                                               'плоскость, вложи яичные лотки один в другой и т.д.)\n\n'
                                               'Некоторые приёмщики требуют снимать крышки, пластиковые кольца с '
                                               'бутылок и этикетки. Уточняй эти моменты на сайте пункта приёма, а '
                                               'также в их социальных сетях.', reply_markup=keyboard5)
    elif call.data == '11':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)
    elif call.data == '12':
        bot.send_message(call.message.chat.id, '6. Сдать вторсырьё на переработку. Подготовка - это хорошо, однако '
                                               'не сильно застревай на этом этапе. Ведь самое главное - это начать '
                                               'действовать и постепенно менять свой образ жизни. Ничего страшного, '
                                               'если в начале у тебя будет всего одна категория, которую ты будешь '
                                               'сдавать. Ничего страшного, если ты ещё не до конца понимаешь, как '
                                               'организовать раздельный сбор дома до всех мелочей. Начни, а дальше '
                                               'уже всё встанет на свои места :)\n\n'
                                               'Как только освоишься и поймёшь, что готов идти дальше, можешь '
                                               'расширять список сдаваемого вторсырья, ознакамливаться с новыми '
                                               'пунктами переработки и менять систему раздельного сбора отходов так, '
                                               'как тебе это удобно! Желаю удачи на этом пути в более экологичный образ '
                                               'жизни 🌿', reply_markup=keyboard6)
    elif call.data == '13':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)
    elif call.data == '14':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)
    elif call.data == '15':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/L7qk/xqVwTmABr')
        bot.send_message(call.message.chat.id, '♻️1 — полиэтилентерефталат\n'
                                               'Самый распространённый вид пластика: "популярные" пластиковые бутылки, '
                                               'подложки для фруктов, контейнеры. Несмотря на распространенность, его '
                                               'можно использовать всего один раз, иначе выделяются токсичные фталаты❗',
                         reply_markup=keyboard7)
    elif call.data == '16':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/pgX1/MjXkWcLho')
        bot.send_message(call.message.chat.id, '♻️2 — полиэтилен высокой плотности\n'
                                               'Его можно увидеть среди пластиковых крышечек, пакетов, контейнеров '
                                               'и упаковок от моющих средств. Безопасен для пищевого применения, в '
                                               'него даже можно класть горячее, но не жирное! Не рекомендуется нагревать.',
                         reply_markup=keyboard7)
    elif call.data == '17':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/uuDE/A4V3QtdZ6')
        bot.send_message(call.message.chat.id, '♻️3 — поливинилхлорид\n'
                                               'Один из самых опасных видов пластика. Не пригоден для переработки '
                                               'и пищевого использования. Несмотря на это, может встречаться даже '
                                               'среди детских игрушек и пищевых плёнок — лишний повод тщательно '
                                               'проверять этикетки перед покупкой!', reply_markup=keyboard7)
    elif call.data == '18':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/wwUY/JXaDLEmQr')
        bot.send_message(call.message.chat.id, '♻️4 — полиэтилен низкой плотности\n'
                                               'Как правило, это пакеты для фасовки и мягкая упаковка, однако может '
                                               'встречаться и среди более плотных изделий, трудно перерабатываемых. '
                                               'Представляет опасность при контакте с прямыми солнечными лучами, '
                                               'жирами и маслами, но в целом безопасен для пищевого применения.',
                         reply_markup=keyboard7)
    elif call.data == '19':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/qR6e/uefkH977W')
        bot.send_message(call.message.chat.id, '♻️5 — полипропилен\n'
                                               'Из пятого вида пластика производят пищевые контейнеры, стаканчики '
                                               'из-под йогурта и шуршащую упаковку. Он безопасен для контактов с '
                                               'пищей и может поддаваться нагреву при наличии соответствующей '
                                               'маркировки.', reply_markup=keyboard7)
    elif call.data == '20':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/i7mv/899U1BnGw')
        bot.send_message(call.message.chat.id, '♻️6 — полистирол\n'
                                               'Вспененный пластик — пригоден только для одноразового ⚠️применения, '
                                               'как и полиэтилентерефталат. Ему нельзя контактировать с горячим, '
                                               'кислым и алкоголем — выделяется стирол. По возможности лучше вовсе '
                                               'от него отказаться!', reply_markup=keyboard7)
    elif call.data == '21':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/9LLj/3Qe6qAUCk')
        bot.send_message(call.message.chat.id, '♻️7 — другое\n'
                                               'Это пластик, который не относится к вышеперечисленным видам. '
                                               'Его опасность использования сложно оценить, поэтому будь осторожен '
                                               'и внимательно изучай этикетку. Не принимается на переработку.',
                         reply_markup=keyboard7)
    elif call.data == '22':
        bot.send_photo(call.message.chat.id, 'https://cloud.mail.ru/public/YBXb/N1YS5kE2i')
        bot.send_message(call.message.chat.id, 'Стоит отметить, что некоторые виды пластика, которые помечены в '
                                               'инструкции как те, что не принимаются на переработку, всё-таки можно '
                                               'сдать, но это скорее редкость. Недалеко от дома таких пунктов вы '
                                               'наверняка не найдёте, если только не живёте рядом с перерабатывающим '
                                               'заводом. Однако, некоторые компании сейчас предлагают удобный сервис '
                                               'вывоза вторсырья, поэтому если вы хотите идти дальше и сдавать даже '
                                               'сложные в переработке виды пластика, то вот несколько сервисов с такими '
                                               'услугами:\n'
                                               '- Экотакси - https://vk.com/ecotaxispb\n'
                                               '- Переработкинская - https://vk.com/pererabotkinskaya\n'
                                               '- 7other - https://vk.com/7other (нет услуги вывоза вторсырья, но '
                                               'принимают тот самый сложный пластик)', reply_markup=keyboard7)
    elif call.data == '23':
        bot.send_message(call.message.chat.id, 'Выбери, что тебе интереснее сейчас узнать:', reply_markup=keyboard)


bot.polling()