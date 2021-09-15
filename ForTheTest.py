#------ search ----
# 1. binary search -- run time O(logn)
def binary_search(lst,num):
    left = 0
    right = len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == num:
            return True
        else:
            if num < lst[mid]:
                right = mid-1
            else:
                left = mid+1
    return False
print(binary_search([1,23,43,56,77,888,5555,34543,0],5556))

def binary_search_recorcia(lst,num):
    mid = lst[len(lst)//2]
    if mid == num:
        return True
    elif len(lst)==1:
        return False
    elif mid < num:
        return binary_search_recorcia(lst[len(lst)//2::],num)
    else:
        return binary_search_recorcia(lst[0:len(lst)//2:],num)
print(binary_search_recorcia([1,2,5,67,89,95,234],1234))

# elinor - binary search
lst1 = [4,78,90,101,120,222]
def binar(lst,number):
    if len(lst) == 1:
        if number == lst[0]:
            return True
        else:
            return False
    else:
        mid = lst[len(lst)//2]
        if mid == number:
            return True
        if number < mid:
           return binar(lst[:len(lst)//2],number)
        else:
            return binar(lst[len(lst)//2::],number)

# 2. normal search ---- run time O(n)
def normal_search(lst,x):
    for num in lst:
        if num == x:
            return True
    return False

#------ sort -----

# 1. bubble sort - if not sorted run time O(n^2) ---- if sorted run time O(n)
def bb_short(lst):
    for index in range(1,len(lst)+1):
        swap = False
        for index2 in range(0,len(lst)-index):
            if lst[index2] > lst[index2+1]:
                lst[index2] , lst[index2+1] = lst[index2+1] , lst[index2]
                swap = True
        if swap == False:
            return lst
    return lst
grades = bb_short([100,23,54,342,53,4,55])
print("Small to big ",grades)

# bubble sort - recursive:
def rec_bubble_sort(myList):
    flag = 0
    for i in range(len(myList)-1):
        if myList[i] > myList[i+1]:
            myList[i], myList[i+1] = myList[i+1], myList[i]
            flag = 1
    if flag==1:
        return rec_bubble_sort(myList[0:len(myList)-1])+myList[-1:]
    else:
        return myList

myList = [2, 6, 4, 0, 5,8,-22,7,-77]
print(rec_bubble_sort(myList))

# 2. selection shot - run time allways O(n^2)
lst = ['zion', 'daniel', 'avi', 'lavi', 'hani', "hen", 'sd', 'dsadsd', 'asdas', 'asdsasasd']
def Selection_sort_string(lst):
    lst2 = []
    for name in range(0,len(lst)):
        min = lst[0]
        for index2 in range(0,len(lst)):
            if len(lst[index2]) <= len(min):
                min = lst[index2]
        lst2.append(min)
        lst.remove(min)
    return lst2
print(Selection_sort_string(lst))

lst = [1,2,9,3,6,4,5,7,8]
def Selection_sort_int(lst):
    sort_list = []
    for i in range(len(lst)):
        min = lst[0]
        for index in range(0,len(lst)):
            if lst[index] < min:
                min = lst[index]
        sort_list.append(min)
        lst.remove(min)
    return  sort_list
print("The sorted list is ",Selection_sort_int(lst))

# ----- good ones ----

def afred_and_mshol_rcorica_max(lst):
    if len(lst) == 1:
        return lst[0]
    left = afred_and_mshol_rcorica_max(lst[0:len(lst)//2])
    right = afred_and_mshol_rcorica_max(lst[len(lst)//2::])
    if left > right:
        return left
    else:
        return right
print(afred_and_mshol_rcorica_max([1,32,65,987,34,4,34,54]))

def afred_and_mshol_rcorica_min(lst):
    if len(lst) == 1:
        return lst[0]
    left = afred_and_mshol_rcorica_min(lst[0:len(lst)//2])
    right = afred_and_mshol_rcorica_min(lst[len(lst)//2::])
    if left > right:
        return left
    else:
        return right
print(afred_and_mshol_rcorica_min([1,32,65,987,34,4,34,54]))

## palindrom rekurssive
def palindrom(string):
    if len(string) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return palindrom(string[1:-1])
string = input('Writhe somthing : ')
##------- kod rashi
if palindrom(string) == True:
    print("This is palindrom")
else:
    print('This is not palindrom')

def azeret(N):
    if N > 0:
        N_azeret = 1
        for index in range(1, N + 1):
            N_azeret = index * N_azeret
        return N_azeret
    else:
        return 'There i so azeret for negative'
print(azeret(10))

def azeret_rcorcia(N):
    if N == 0:
        return 1
    elif N > 0:
        return N * azeret_rcorcia(N - 1)
    else:
        return 'There i so azeret for negative'
print(azeret_rcorcia(-1))

# ----- azeret all the elements
N = int(input("Enter number : "))
if N >= 0:
    if N > 0:
        azeret = 1
        for i in range(1, N + 1):
            azeret = i * azeret
            print("The factorial of ", i, " is ", azeret)
    else:
        print("the factorial number for 0 is 1")
else:
    print("there is no factorial for negative number")

# ----- fibo lst until n ---- runtime O(n)
def fibo_lst(n):
    fibo = [1,1]
    index = 0
    while fibo[index] + fibo[index + 1] <= n:
        fibo.append(fibo[index] + fibo[index + 1])
        index += 1
    return fibo
print(fibo_lst(13))

# ----- fibo lst until n  runtime O(n)
def fibo(number):
    if number >= 0:
        if number > 0:
            first = 1
            second = 1
            third = 1
            print(first,second,sep="\n")
            while third < number:
                third = second + first
                first = second
                second = third
                if third <= number:
                    print(third)
        else: print(1)
    else:
        print("The number must to be positive")
fibo(100)

# ----- fibo lst until index n start in 1 1 2 3 ..... runtime O(n)
def fibo_recocia(number):
    if number < 2:
        return 1
    else:
        return fibo_recocia(number-1) + fibo_recocia(number-2)
print(fibo_recocia(5))

def perfect_num(n):
    number = 0
    for index in range(1,n):
        if n%index == 0:
            number = number + index
    if number == n:
        return True
    else:
        return False
print(perfect_num(15))

def sum_series(first_nember,differ,length):
    An = first_nember+(length-1)*differ
    return An
print(sum_series(0,2,10))

def mishva_riboait(a,b,c):
    import math
    if b*b-4*a*c >= 0:
        sqrt = math.sqrt(b * b - 4 * a * c)
        x1 = (-b + sqrt) / (2 * a)
        x2 = (-b - sqrt) / (2 * a)
        return x1, x2
    else:
        return "there is no sqrt for this numbers"
print(mishva_riboait(3,5,2))

# ----- hibor sifrat asarot ve yehidon
count = 0
for index in range(10,100):
    num1 = index%10 # yehidot
    num2 = (index-num1)//10 # asarot
    sum_num = num1 + num2
    if sum_num > 15:
        count += 1
        print(index , sum_num)
print('There is',count,'numbers')

def loah_akefel(n):
    for line in range(1,n+1):
        print()
        for colum in range(1,n+1):
            print(line*colum,end=' ')
loah_akefel(5)

# loah akefel only for 3
n = int (input ("Enter a number:\n"))
if n > 0:
 print ("Multiplication table up", n, "that fulfills the condition:")
for row in range (1, n+1):
    for line in range (1, n+1):
        if ((row * line) %3 == 0):
            print (row * line, end = "\t")
        else:
            print("*", end="\t")
    print ()
else:
 print("The number is NOT positive")

def terth_tow_one(number):
    for line in range(0,number):
        print()
        for culoum in range(number,line,-1):
            print(culoum,end=' ')
terth_tow_one(3)

# --- loto_ball
sum_year = 0
for year in range(1,53):
    sum_week = 0
    for week in range(1,7):
        bull = int(input("Enter bull number "))
        if bull // 10 == 3:
            sum_week += 1
        if bull% 10 == 3:
            sum_week +=1
    print("This week number 3 was ",sum_week," Times")
    sum_year = sum_week + sum_year
print("This year number 3 was ",sum_year," times")

# --- find_min_max - enter the length and number find the min and max
length = int(input('enter the length '))
if length > 0:
    max_num  = int(input('enter number '))
    min_num = max_num
    for index in range(length-1):
        number = int(input('enter number '))
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
    print('max = '+str(max_num)+' min = '+str(min_num))

# ---sum one to hundread
sum = 1
count = 0
while sum <= 100:
        count += 1
        sum = sum + count
print(count)

def one_to_handred_recorcia(sum=1,count=0):
    if sum >= 100:
        return count-1
    else:
        sum = sum + count
        return one_to_handred_recorcia(sum,count+1)
print(one_to_handred_recorcia())

#--- print to N (negative or psotive) with while
N = int(input('Enter number '))
counter = 0
print(counter)
while counter != N:
    if N < 0:
        counter -= 1
        print(counter)
    else:
        counter += 1
        print(counter)

#--- print to N (negative or psotive) with for
num = int(input("Enter number : "))
if num >= 0:
    n = 1
else:
    n = -1
for num in range(0,num+n,n):
    print(num)

# mithalek im 0 or 15 or 35
lst = []
for i in range(1,101):
    if (i%6 == 0 or i%15 == 0 or i%35 == 0):
        lst.append(i)
print ("The numbers that fulfill the condition:\n",lst)
print ("There are", len(lst), "numbers that fulfill the condition")
lst0, lst1 = [], []
for i in lst:
    if (i%2 == 0):
        lst0.append(i)
    else:
        lst1.append(i)
print()
print ("There are", len(lst0), "even numbers:")
print (lst0)
print ("There are", len(lst1), "odd numbers:")
print (lst1)

#---- random

import random
rand = random.randint(1,100)
num = int(input("num"))
while num != rand:
    if num < rand:
        num = int(input("the munber is low"))
    else:
        num = int(input("the number is high "))
print( "fuck ya !")

# --- prime numbers
def isprime (n):
    if (n == 1):
       return False
    for i in range(2, n, 1):
        if (n % i == 0):
            return False
    return True
num = int(input("Enter a number:\n"))
if (num > 0):
    if (isprime(num) == True):
        print("The number is prime")
    else:
        print("The number is NOT prime")
    count = 0
    for j in range(1, num+1):
        if (isprime(j) == True):
            count += 1
    print ("There are", count, "primes numbers between 1 and ", num)
else:
    print("The number is NOT positive")
## ----- rishonim rekursia

def is_rishon(value, nextNum=0):
    if value == 1:
        return False
    if nextNum == 0:
        nextNum = value - 1
    else:
        nextNum -= 1
    return True if nextNum == 1 else value % nextNum != 0 and is_rishon(value, nextNum)

print(is_rishon(6))

def NumOption(num,op='3'):
    if op == '1':
        return len(num)
    elif op == '2':
        sum = 0
        for n in num:
            sum = sum + int(n)
        return sum
    elif op == '3':
        sum = 0
        for n in num:
            sum = sum + int(n)
        return sum , len(num)

# ---- undo_word
lst = []
while True:
    action = input("Do somthing ")
    if action == "undo":
        lst.pop()
        print(lst)
    else:
        lst.append(action)
        print(lst)
    if lst == []:
        break

# ------ bdikat sograim stack
number = '(5*((3-4)-5*(6+8)))'
stack = []
cheack = 0
for letter in number:
    stack.append(letter)
    if letter == '(':
        cheack += 1
    elif letter == ')':
        cheack -= 1
if cheack == 0:
    print("This exercise is good !")
else:
    print("This exercise wrong !")


# ---- stack
def deque():
    from collections import deque
    stack = deque()
    stack.append('a')
    print(stack)
    stack.append('b')
    print(stack)
    stack.append('c')
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
deque()

# ----- tor
def queue():
    import queue
    q = queue.Queue(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    print(q.queue)
    q.get()
    q.get()
    print(q.queue)
    q.put(5)
    q.put(6)
    print(q.queue)
    q.get()
    print(q.queue)
queue()



# ----- rishima mekoseret
lst = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None],
}
def fun9(lst):
    lst[7] = [None]
    lst[4].append(7)
    lst[6].append(7)
    lst[4].remove(5)
    p = []
    for key in lst.items():
        if len(key[1]) == 1:
            print(key[0])
    max = lst[1]
    for key in lst.items():
        if len(key[1]) >= len(max):
            max = key[1]
            p.append(key[0])
    print(p)
fun9(lst)

# --- linked list
lst = {
    1:2,
    2:3,
    3:4,
    4:6,
    6:8
}
# find how many times x in list
def find_x_in_linked_list(lst,x):
    count = 0
    for key in lst.items():
        if key[0] == x:
            count += 1
        elif key[1] == x:
            count += 1
    return count
print(find_x_in_linked_list(lst,3))

#--- dictionary ---

# - hourse in the bar

bar_menu = {
    'alcholic' : [['taqila',30],['shendy',40]],
    'alchol_free' : [['water',10],['orange',20]]
}
hourse = [int(input('What is you age ? ')),input('waht you want to drink ? ')]
if hourse[1] == 'taqila' or hourse[1] == 'shendy':
    if hourse[0] >= 18:
        print(
            "----- REASIPT -----",
            '\nYour drink : ',hourse[1],
        )
        if hourse[1] in bar_menu['alcholic'][0]:
            print('The price : ', bar_menu['alcholic'][0][1])
        else:
            print('The price : ', bar_menu['alcholic'][1][1])
    else:
        print('you cant order alcholic in your age')
elif hourse[1] == 'water' or hourse[1] == 'orange':
    print(
        "----- REASIPT -----",
        '\nYour drink : ', hourse[1],
    )
    if hourse[1] in bar_menu['alchol_free'][0]:
        print('The price : ', bar_menu['alchol_free'][0][1])
    else:
        print('The price : ', bar_menu['alchol_free'][1][1])
else:
    print("We dont have this drink !")

# targil kita 7
dict = {
    'Day':['sun','the','fri'],
    'Teaching_Hours':[6,6,4],
    'Assignments':[2,3,0]
}
print('The complete dataThe complete data: ')
for Keys in dict.items():
    print(Keys[0],Keys[1])
print('Days of studying : ',dict['Day'])
print('Total hours of studying : ',sum(dict['Teaching_Hours']))
print('Number of assignments in second day : ',dict['Assignments'][1])
print('Total number of assignments : ',sum(dict['Assignments']))

#---- 7 -- guss the word
word = input("Enter some word : ")
digits = ""
count = 0
while count != len(word):
    digit = input('Enter digit ')
    if digit not in digits:
        digit_count = word.count(digit)
        if digit_count == 1:
            count += 1
            digits = digits + digit
            print("Nice this digit is in the string go for the next one !")
        if digit_count == 0:
            digits = digits + digit
            print("This digit is not in the string go for the next one !")
        elif digit_count > 1:
            count = count + digit_count
            digits = digits + digit
            print("Nice this digit is ", digit_count, "times in the string go for the next one !")
    else:
        print('You already try this digit')
print(word)

# --- targil kita 12

def suf_vol(L,W,H,op='SV'):
    if op == 'S':
        return 2*(L*W+L*H+W*H)
    if op == 'V':
        return  L*W*H
    if op == 'SV':
        return 2*(L*W+L*H+W*H),L*W*H
L = int(input('Enter the length '))
W = int(input('Enter the with '))
H = int(input('Enter the higth '))
op = input('enter the op ')
if op == 'S':
    print('the surface area is ',suf_vol(L,W,H,op))
if op == 'V':
    print('the volume is ',suf_vol(L,W,H,op))
if op == 'SV':
    m1 , m2 = suf_vol(L,W,H,op)
    print('the ratio is ',m1/m2)

# ---- targil 13
Trys = False
count = 0
while Trys != True:
    num_grades = int(input("For how many grades you want calculate the average :"))
    if num_grades > 0:
        Trys = True
    else:
        print('you must to enter integer number that bigger then zero !')
        count += 1
        if count == 3:
            print('Your input is wrong !')
            break
num_grades_ok = []
num_success = []
print('Please enter you grades ')
for index in range(1, num_grades + 1):
    grade = float(input('Grade number ' + str(index) + ' :'))
    if grade < 1 or grade > 100:
        print('This Grade is illegal and not calculate in you average')
    else:
        num_grades_ok.append(grade)
        if grade > 59:
            num_success.append(grade)
def average(grades):
    average = sum(num_success) / len(num_success)
    return average
#סטיית תקן
def pvariance(grades):
    import statistics
    pvariance = statistics.variance(grades)
    return pvariance

print("You enter ",len(num_grades_ok),' legal grades')
print("Form the ",len(num_grades_ok),'grades your enter only ',len(num_success),' is calculate in your average')
print('The average for the ',len(num_success),' grades is ',average(num_success))
print('The variance is',pvariance(num_success))
print('The highest grade is ',max(num_grades_ok))
print('The smallest grade is ',min(num_grades_ok))
for grade in num_success:
    count = 0
    if grade < average(num_success):
        count+=1
print(count," grades are better then you average the others are under ")
if num_success != []:
    print("You didn't pass  ",len(num_grades_ok)-len(num_success)," exams")

# ----- targil 16

def NumOption(num,op="3"):
    sum_digits =0
    for sum in str(num):
        sum_digits = sum_digits + int(sum)
    if op == "1":
        return len(str(num))
    elif op == "2":
        return sum_digits
    elif op== "3":
        return len(str(num)),sum_digits

num = int(input("please enter positive number: "))
if num < 0:
    num = int(input("please enter positive number: "))
op = input("please enter an option 1/2/3")
if num > 0:
    if op == "1":
        print("the length of the number is: ",NumOption(num, op))
    elif op == "2":
        print("the sum of digits of number",num," is: ",NumOption(num, op))
    elif op =="3":
        length, sum1 = NumOption(num,op)
        print("the length is: ", length, " the sum of digits is: ", sum1)
    else:
        length, sum1 = NumOption(num)
        print("the length is: ", length, " the sum of digits is: ", sum1)

# ---- targil 17
def sum_factorial(number,op='sumfact'):
    sum = 0
    if number >= 0:
        n = 1
        factorial = 1
        for temp in range(1,number+1):
            factorial = factorial * temp
    else:
        n = -1
        factorial = 'there s nor factorial for negative number'
    for num in range(1,number+n,n):
        sum = sum + num
    if op == 'sum':
        return  sum
    if op == 'fact':
        return factorial
    if op == 'sumfact':
        return sum,factorial
num = int(input('Enter intiger number : '))
op = input('Enter an option sum/fact/sumfact : ')
if op == 'sum':
    print('The sum of numbers from 1 to ',num,' is :',sum_factorial(num,op))
elif op == 'fact':
    print('The factorial of ',num,' is : ',sum_factorial(num,op))
else:
    sum,fact = sum_factorial(num)
    print('The sum of numbers from 1 to ',num,' is :',sum,'\n the factorial of ',num,' is : ',fact)
    print('Is the sum of numbers from 1 to ', num, ' greater than ', num, ': ', sum > num)
    if type(fact) != str:
        print('Is the factorial ', num, ' greater than ', num * 100, ' : ', fact > num * 100)
