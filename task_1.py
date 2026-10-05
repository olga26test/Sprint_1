time_period = '1h 45m,360s,25m,30m 120s,2h 60s'
time_period = time_period.replace(' ', ',').split(',') #преобразовали в список
total_time = 0
for i in time_period:
    if 'h' in i:
        i = i.split('h')
        i = int(i[0]) * 60 
        total_time += i
    elif 'm' in i:
        i = i.split('m')
        i = int(i[0])
        total_time += i
    elif 's' in i:
        i = i.split('s')
        i = int(i[0]) // 60 
        total_time += i
print('Общее количество минут:', total_time)