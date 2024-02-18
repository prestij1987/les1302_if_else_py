
# if None:
#     print('None истинен')
# else:
#     print('None в Python расценивается как ложь')


# height = int(input('Какой у Вас рост?'))
# if height > 175:
#     print('Осторожно, Вы можете удариться о верхний косяк двери!')
# elif height == 175:
#     print('Если без кепки, то войдёте')
# else:
#     print('Вы легко войдёте в любой вагон. Счастливого пути!')


hour = int(input('Сколько сейчас времени (в часах)?'))
if hour < 8:
    print('Как насчёт утренней пробежки?')
if hour < 11:
    print('Тебя ждёт завтрак')
if hour < 16:
    print('Впереди обед')
if hour < 18:
    print('На полдник пирожные')
if hour < 21:
    print('На ужин гречка') 


# weather = int(input('Введите погоду '))

# weather_good = 'teplo'

# weather_bad = 'cold'

# weather_norm = 'norm'

# if weather == weather_good:
#     print('mojno razdetsy')
# if weather < weather_bad:
#     print('nuzno odetsy')  
# elif weather < weather_norm:    
#     print('Vse horosho')

#написать код, который по часам определяет утро 
#(4-11), день (12-16) вечер (17-22) и ночь (23-3)
    
time_sytok = int(input('Введите время суток: '))

if time_sytok >= 4 and time_sytok <= 11 or time_sytok <= 12 and time_sytok <= 23:
    print('Время суток утро')
if time_sytok >= 12 and time_sytok <= 16 or time_sytok <= 13 and time_sytok <= 22:
    print('Время суток день')  
if time_sytok <= 17 and time_sytok <= 22:
    print('Время суток вечер ')      
if time_sytok <= 23 and time_sytok <= 3:
    print('Время суток: ночь')    
else:
    print('Вы ввели не коректое время ') 

    
       