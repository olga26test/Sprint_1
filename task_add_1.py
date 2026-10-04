types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def double_tickets_del(dict): #функция для удаления дублей
    from copy import deepcopy
    new_tickets = deepcopy(dict) #создали копию, при изменении которой оригинал не изменится
    for key in dict.keys():
        if key != 1:  #для каждого ключа, кроме первого..
            for value in dict.get(key): #берём каждое значение..
                for i in range(1, key): #и сверяем со значениями в каждом ключе выше данного
                    if value in dict.get(key-i):
                        new_tickets[key].remove(value)  #удаляем, если нашли
                        #print(new_tickets)
                        break
        else:
            continue

    return new_tickets 


def types_tickets(dict1, dict2): #функция для связки критичности и тикетов
    tickets_by_type = {}
    i = 1
    for value in dict1.values():
        tickets_by_type[value] = dict2.get(i)
        i += 1
    print(tickets_by_type)


tickets = double_tickets_del(tickets) #этот момент с возвратом уточнила у ИИ, т.к. не получалось вернуть измененный словарь
types_tickets(types, tickets)

