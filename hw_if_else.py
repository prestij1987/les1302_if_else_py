
#Zadacha 1
#Получить с клавиатуры скорость самолета, 
#названия городов и расстояние (на 12 баллов координаты lat, lon). 
#Вычислить время в пути, считая скорость постоянной. 
#Записать ответ, как в слайде с примером.

#Zadach 2
#На выполнение заданий по питону студент предполагает 
#потратить ч часов м минут (получить с клавиатуры). 
#Во сколько самое позднее ему следует начать, чтобы оставить на дорогу 
#1 час и успеть к 19:00 на занятия? Ответ оформить.

#Zadacha 3
#На дом задано 3 задачи. На решение каждой следующей 
#тратится вдвое меньше времени. Измерьте время, 
#затраченное на первую задачу и оцените общее время выполнения ДЗ. 
#Ответ снова оформить красиво. Сравнить с реальным значением.


speed_plain = input('Ввести скорость самолета: ')
speed_plain1 = int(speed_plain)

city_1 = input('Введите название города: ')
city_2 = input('Введите название города: ')


dist_1 = 500
dist_2 = 700 


time_way_1 = dist_1 / speed_plain1 # vremy dv puti
time_way_2 = dist_2 / speed_plain1
print('Время в пути: ', time_way_1, city_1)
print('Время в пути: ', time_way_2, city_2)


rast_city = (dist_1 ** 2 + dist_2 ** 2) # rast mejdu gorodami

print( 'Растояние', rast_city)
