#task1------------------------------------------------------------
"""
Умова: Дано два цілих числа. Вивести найменше з них.

Вхідні дані: користувач вводить ціле число

Вихідні дані: вивести ціле число
"""



#
a=int(input())
b=int(input())
if a<b:
    print(a)
else:
    print(b)
#-----------------------------------------------------------------
#task2------------------------------------------------------------
"""
Умова: Вивести результат функції sign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
"""



#
x = int(input())
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)

#-----------------------------------------------------------------
#task3------------------------------------------------------------
"""
Умова: Дано три цілих числа. Вивести найменше з них.

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""



#
a = int(input())#Enter a
b = int(input())#Enter b
c = int(input())#Enter c
if a > c and b > c:
    print(c)#if a>b>c prints c
elif b > a and c > a:
    print(a)#if b>a prints a
else:
    print(b)
#-----------------------------------------------------------------
#task4------------------------------------------------------------
"""
Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".

Рік високосний, якщо виконується хоча б одна з умов:

    рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
    рік завжди високосним, якщо його номер ділиться на 400 без остачі

Вхідні дані: ціле число, що вводить користувач

Вихідні дані: вивести текстовий рядок.
"""



#
year = int(input())
a=year%400
b=year%4
c=year%100
if a == 0:
    print('LEAP')
elif b == 0 and c != 0:
    print('LEAP')
else:
    print('COMMON')

#-----------------------------------------------------------------
#task5------------------------------------------------------------
"""
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""



#
a = int(input())
b = int(input())
c = int(input())
if a==b and b==c:
    print(3)
elif a==b:
    print(2)
elif a==c:
    print(2)
elif c==b:
    print(2)
else:
    print(0)

#-----------------------------------------------------------------
#task6------------------------------------------------------------
"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#
x = int(input())
y = int(input())
r = int(input())
c = int(input())
if x > 8 or y > 8 or r > 8 or c >8:
    print('incorrect input')
elif x==r:
    print('YES')
elif y==c:
    print('YES')
else:
    print('NO')    

#-----------------------------------------------------------------
#task7------------------------------------------------------------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#
x = int(input())
y = int(input())
r = int(input())
c = int(input())
d = (x+y)%2
k = (r+c)%2
if x > 8 or y > 8 or r > 8 or c >8:
    print('incorrect input')
elif d == k:
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------
#task8------------------------------------------------------------
"""
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#
x = int(input())
y = int(input())
t = int(input())
c = int(input())
d = float(x-t)
k = float(y-c)
if x > 8 or y > 8 or t > 8 or c >8:
    print('Incorrect input')
elif -1<=d<=1 and -1<=k<=1:
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------
#task9------------------------------------------------------------
"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.


"""



#
r = int(input())
c = int(input())
d = (x+y)%2
k = (r+c)%2
from math import fabs
l = fabs(x-r)
m = fabs(y-c)
if x > 8 or y > 8 or r > 8 or c >8:
    print('Incorrect input')
elif d == k and l == m:
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------
#task10-----------------------------------------------------------
"""
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#
m = fabs(y-c)
if x > 8 or y > 8 or r > 8 or c >8:
    print('Incorrect input')
elif -1<=d<=1 and -1<=k<=1:
    print('YES')
elif x==r:
    print('YES')
elif y==c:
    print('YES')
elif n == u and l == m:
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------
#task11------------------------------------------------------------
"""
Умова: Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#
x = int(input())
y = int(input())
r = int(input())
c = int(input())
from math import fabs
l = fabs(x-r)
m = fabs(y-c)
if x > 8 or y > 8 or r > 8 or c >8:
    print('Incorrect input')
elif l==2 and m==1:
    print('YES')
elif l==1 and m==2:
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------
#task12-----------------------------------------------------------
"""
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.

Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#
n = int(input())
m = int(input())
k = int(input())
if n*m > k:
    if k%n==0 or k%m==0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
#-----------------------------------------------------------------