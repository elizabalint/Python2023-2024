
# 1. Find The greatest common divisor of multiple numbers read 
# from the console.
import sys
def functie(numbers):
    if not numbers:
        return None
    cmmdc = numbers[0]
    for i in numbers[1:]:
        a = cmmdc
        b = i
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        cmmdc = a
    return cmmdc

args = sys.argv[1:]
numbers = [int(arg) for arg in args] #citirea mai multor argumente
rez = functie(numbers)
if rez is not None:
    print("cmmdc este: ", rez)
else: 
    print("Nu exista cmmdc.")

# 2. Write a script that calculates how many vowels are in a string.

s = "aaapppOnUiMrEyup Uji"
voc = "AEIOUaeiou"
nr = 0
for i in s:
    if i in voc:
        nr += 1

print(nr)

# 3. Write a script that receives two strings and prints the number 
# of occurrences of the first string in the second.

nr = 0
string1 = "se"      #asta e ala care se cauta
string2 = "asta se e ala in care seceseta se cauta se se "

i = 0
while i < len(string2):
    a = string2.find(string1,i) #cauta sting2 in string1 incepand cu pozitia lui i
    if a == -1:                 #daca sirul nu mai exista atunci se iese din while
        break 
    nr +=1
    i = a + len(string1)        #daca gasim stringul, trecem peste el 
           
print(nr)    

# 4. Write a script that converts a string of characters written in 
# UpperCamelCase into lowercase_with_underscores.
string = "UpperCamelCase"
string_nou = ""
for i in range(len(string)):
    upper = string[i].isupper()
    if i == 0 and upper:
        string_nou = string[i].lower()
    elif upper:
        string_nou = string_nou + "_" + string[i].lower()
    else:
        string_nou = string_nou + string[i]
print(string_nou)



""" 5. Given a square matrix of characters write a script that prints 
the string obtained by going through the matrix in spiral order 
(as in the example):
firs      1  2  3  4    =>   first_python_lab
n_lt      12 13 14 5
oba_      11 16 15 6
htyp      10 9  8  7  """

mat = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]
top = 0
bottom = len(mat) - 1
right = len(mat[0]) - 1
left = 0
string = ""
while top <= bottom and left <= right: #pentru a ne asigura ca se iau toate elem pana ajungem in centrul matricei
    for i in range(left, right + 1):   #elem de pe prima linie
        string = string + mat[top][i]
    top += 1
    if top <= bottom and left <= right:  #fiecare if verifica daca mai exista elemente de adaugat in strinf pe linia/coloana respectiva
        for i in range(top, bottom + 1): #elem de pe ultima coloana
            string = string + mat[i][right] 
        right = right - 1
    if top <= bottom and left <= right:
        for i in range(right, left - 1, -1): #elem de pe ultima linie in ordine inversa
            string = string + mat[bottom][i]
        bottom = bottom - 1
    if top <= bottom and left <= right:
         for i in range(bottom, top - 1, -1): # elem de pe prima linie in ordine inversa
            string = string + mat[i][left]
         left += 1
print(string)

# 6. Write a function that validates if a number is a palindrome.
 
def palindrom (nr):
    nr1 = nr
    oglindit=0
    while nr > 0:
        c = nr % 10
        oglindit = (oglindit * 10) + c
        nr = nr // 10
    if nr1 == oglindit:
        return True
    else:
        return False
nr = 1232
if palindrom (nr):
    print(nr, "este palondrom")
else:
    print(nr, "nu este palindrom")


# 7. Write a function that extract a number from a text 
# (for example if the text is "An apple is 123 USD", this 
# function will return 123, or if the text is "abc123abc" 
# the function will extract 123). The function will extract 
# only the first number that is found.

def primul_numar(string):
    numar = ""
    for i in string:
        if i.isdigit():
            numar = numar + i
        elif numar:
            break
    return numar

string= "An apple is 123 USD 13"
nr = primul_numar(string)
print(nr)


# 8. Write a function that counts how many bits with value 1 
# a number has. For example for number 24, the binary format
# is 00011000, meaning 2 bits with value "1"

def count(nr):
    binar = bin(nr)
    c = 0
    for i in range(len(binar)):
        if binar[i] == '1':
            c +=1
    return c

f = count(42)
print(f)

# 9. Write a functions that determine the most common letter in a 
# string. For example if the string is "an apple is not a tomato", 
# then the most common character is "a" (4 times). Only letters 
# (A-Z or a-z) are to be considered. Casing should not be considered
# "A" and "a" represent the same character.

def common_letter(string):
    string= string.lower()
    litere={}
    for i in string:
        if i.isalpha():
            if i in litere:
                litere[i]= litere[i]+1
            else:
                litere[i]=1
    maxim = max(litere, key = litere.get)
    return maxim

string = "an apple is not a tomato"
rezultat = common_letter(string)
print(rezultat)


# 10. Write a function that counts how many words exists in a text. 
# A text is considered to be form out of words that are separated 
# by only ONE space. For example: "I have Python exam" has 4 words.

def words(string):
    nr=1
    for i in range(2, len(string)):
        if ' ' in string[i-1]:
           nr +=1
    return nr

string = "I have Python exam uifyudtb dgt tdc ghc"
rezultat = words(string)
print(rezultat)
