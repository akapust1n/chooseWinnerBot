GAME_RULES = '''
Правила игры <b>Пидор Дня</b> (только для групповых чатов):
<b>1</b>. Зарегистрируйтесь в игру по команде /pidoreg
<b>2</b>. Подождите пока зарегиструются все желающие
<b>3</b>. Запустите розыгрыш по команде /pidor
<b>4</b>. Статистика доступна по команде /pidostats
<b>Важно</b>, розыгрыш проходит только <b>раз в день</b>, повторная команда выведет <b>результат</b> игры.

Сброс розыгрыша происходит каждый день в полночь по Москве.
------------
Каждый игрок имеет право на ролл бана 3 раза в день + количество выигрышей в пидоре дня в этом месяцe.
Редкость банов:
<b>Common</b>: 10-20 минут бана
<b>Uncommon</b>: 1-2 часа бана
<b>Rare</b>: 4-6 часов бана
<b>Mythical</b>: 15-20 часов бана
<b>LEGENGARY</b>: + одно очков в игре Пидор дня**'''

common_phrases = {
    'already_in_the_game': 'Эй, ты уже в игре!',
    'not_in_the_game': 'Эй, ты и так не в игре, <b>пидор</b>!',
    'added_to_the_game': '<b>OK!</b> Ты теперь участвуешь в игре "<b>Пидор Дня</b>"',
    'removed_from_the_game': '<b>OK</b>! Ты больше не участвуешь в игре "<b>Пидор Дня</b>" '
                             '(это не затронет данные предыдущих игр)',
    'winner_known': 'Согласно моей информации, по результатам сегодняшнего розыгрыша <b>пидор дня</b> - {name}!',
    'no_players': 'Эй, <b>пидоры</b>! А кто регистрироваться-то будет?',
    'only_one_player': 'В игре только один <b>пидор</b>',
    'access_denied': 'Извините, данная команда доступна только в группах или супергруппах.',
    'no_winners': 'Эй, <b>пидоры</b>! А кто играть-то будет?',
    'list_players_header': 'В чат призываются:',
    # 'unknown_command': 'Нет такой команды, <b>пидор</b>!',
    # 'echo_started': 'Начал трансляцию!',
    # 'echo_finished': 'Остановил трансляцию',
}

stats_phrases = {
    'header': 'Топ-10 <b>пидоров</b> за текущий месяц:',
    'header_all': 'Топ-10 <b>пидоров</b> за все время:',
    'header_lootcrate1': 'Топ-10 владельцев сундука #1',
    'template': '<b>{num}</b>. {name} — <i>{cnt} раз(а)</i>',
    'template_lootcrate': '<b>{num}</b>. {name} — <i>{cnt} шт</i>',
    'footer': 'Всего участников — <i>{players_cnt}</i>',
    'footer_lootcrate': 'Всего владельцев — <i>{players_cnt}</i>'
}

scan_phrases = [
    [
        'Осторожно! <b>Пидор дня</b> активирован!',
        'Система взломана. Нанесён урон. Запущено планирование контрмер.',
        'Сейчас поколдуем...',
        'Инициирую поиск <b>пидора дня</b>...',
        'Итак... кто же сегодня <b>пидор дня</b>?',
        'Кто сегодня счастливчик? Неужели Антон?'
    ],
    [
        '<i>Шаманим-шаманим</i>...',
        '<i>Где-же он</i>...',
        '<i>Сканирую</i>...',
        '<i>Военный спутник запущен, коды доступа внутри</i>...',
        '<i>Хм</i>...',
        '<i>Интересно</i>...'
    ],
    [
        'Так-так, что же тут у нас...',
        'КЕК!',
        'Доступ получен. Аннулирование протокола.',
        'Проверяю данные...',
        'Ох...',
        'Высокий приоритет мобильному юниту.'
    ],
    [
        'Ого, вы посмотрите только! А <b>пидор дня</b> то - {name}',
        'Кажется, <b>пидор дня</b> - {name}',
        '''
.∧＿∧
( ･ω･｡)つ━☆・*。
⊂  ノ    ・゜+.
しーＪ   °。+ *´¨)
         .· ´¸.·*´¨)
          (¸.·´ (¸.·'* ☆ ВЖУХ И ТЫ ПИДОР, {name}''',
        'Анализ завершен. Ты <b>пидор</b>, {name}'
    ]
]
