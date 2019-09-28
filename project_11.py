#Задача: какое количесвто батареек  понадобится что-бы зарядить теслу новейшей модели
#Высчитать массу  цену батареек, учитывая их вес, в зависимости от мощности
import math
Tpower=250 #кВт*ч
print('Введите мощность батарейки, учитывая, что средняя мощность пальчиковой батарейки не превышает 3000мАч')
batteryP1=int(input())
while batteryP1>3000:
    print('Введите новую мощность')
    batteryP1=int(input())
print('введите напряжение батарейки, учитывая, что среднее напряжение в пальчиковых батарейках не превышает 4 В')
U=float(input())
while U>4:
    print('Введите новoe напряжение')
    U=int(input())
batteryP2=batteryP1/1000 #перевод из МАЧ в АЧ
batteryP2=U*batteryP2/1000 #перевод из АЧ в кВт*ч
quantity=math.ceil(Tpower/batteryP2)
print('Для заряда теслы понадобится' ,quantity, 'батареек')
weightT=200 #кг
if batteryP1<=1000:
    weightB1=15/1000
    weight1 = weightB1 * quantity
    print('Вес батареек будет равняться', weight1, 'кг')
    r=weight1-weightT
    print('Разница между весом аккумулятора и батареек равна' ,r, 'кг')
else:
    if batteryP1<=2000:
        weightB2=20/1000
        weight2 = weightB2*quantity
        print('Вес батареек будет равняться', weight2, 'кг')
        r = weight2 - weightT
        print('Разница между весом аккумулятора и батареек равна', r, 'кг')
    else:
        if batteryP1<=2500:
            weightB3=25/1000
            weight3=weightB3*quantity
            print('Вес батареек будет равняться', weight3, 'кг')
            r = weight3 - weightT
            print('Разница между весом аккумулятора и батареек равна', r, 'кг')
        else:
            if batteryP1<=3000:
                weightB4 = 30/1000
                weight4 = weightB4 * quantity
                print('Вес батареек будет равняться', weight4, 'кг')
                r = weight4 - weightT
                print('Разница между весом аккумулятора и батареек равна', r, 'кг')
if batteryP1<=1000:
    priceB1=28
    price1 =priceB1* quantity
    print('Цена батареек будет равняться', price1, 'руб.')
else:
    if batteryP1<=2000:
        priceB1 = 32
        price1 = priceB1 * quantity
        print('Цена батареек будет равняться', price1, 'руб.')
    else:
        if batteryP1<=2500:
            priceB1 = 34
            price1 = priceB1 * quantity
            print('Цена батареек будет равняться', price1, 'руб.')
        else:
            if batteryP1<=3000:
                priceB1 = 36
                price1 = priceB1 * quantity
                print('Цена батареек будет равняться', price1, 'руб.')

