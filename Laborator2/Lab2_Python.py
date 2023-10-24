# 1 Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    fib = [0,1]
    if n <= 0:
        return []
    else:
        if n == 1:
            return [1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
print(fibonacci(6))


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def prim(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range (5,n//2):
        if n % i == 0:
            return False
    return True

def lista_prima(lista):
    a = []
    for i in lista:
        if prim(i):
            a.append(i)
    return a

lista = list(range(2,19)) + [51]
prime = lista_prima(lista)
print(prime)
    

# 3. Write a function that receives as parameters two lists a and b
# and returns: (a intersected with b, a reunited with b, a - b, b - a)

def function(a,b):
    intersectie = []
    reuniune = []
    diferenta_a = []
    diferenta_b = []
    a.sort()
    b.sort()
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            intersectie.append(a[i])
            reuniune.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            reuniune.append(a[i])
            diferenta_a.append(a[i])
            i += 1
        else:
            reuniune.append(b[j])
            diferenta_b.append(b[j])
            j += 1
    
    while i < len(a):
        reuniune.append(a[i])
        diferenta_a.append(a[i])
        i += 1
    while j < len(b):
        reuniune.append(b[j])
        diferenta_b.append(b[j])
        j += 1

    return intersectie, reuniune, diferenta_a, diferenta_b  

a = [1, 6, 9, 546, 712, 435, 624]
b = [4, 47, 546, 0, 25, 624, 42]  
print(function(a,b))     

# 4. Write a function that receives as a parameters a list of musical notes (strings), 
# a list of moves (integers) and a start position (integer). The function will return 
# the song composed by going though the musical notes beginning with the start position 
# and following the moves given as parameter. Example :
# compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) 
# will return ["mi", "fa", "do", "sol", "re"]
 
def compose(lista, moves, start):
    song = []
    for i in moves:
        song.append(lista[start])
        start = (start+i)%len(lista)
    song.append(list[start])
    return song
print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# 5. Write a function that receives as parameter a matrix and will 
# return the matrix obtained by replacing all the elements under 
# the main diagonal with 0 (zero).

def replace(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i > j:
                mat[i][j] = 0
    return mat
mat = [[1, 2, 3, 2, 1, 1],
       [2, 4, 4, 3, 7, 2],
       [5, 5, 2, 5, 6, 4],
       [6, 6, 7, 6, 7, 5]]
print(replace(mat))

# 6. Write a function that receives as a parameter a variable number
#  of lists and a whole number x. Return a list containing the items 
# that appear exactly x times in the incoming lists. 
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and
#  x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 
# 1 and 2, 3 is in lists 1 and 2.

def function(x,*liste):
    n = {}
    final =[]
    for i in liste:
        for j in i:
            if j in n:
                n[j] += 1
            else:
                n[j]=1

    for i,c in n.items():
        if c == x:
            final.append(i)
    return final
l1 = [1,2,3]
l2 = [2,3,4] 
l3 = [4,5,6]
l4 = [4,1, "test"]
x=2
print(function(x,l1,l2,l3,l4))

# 7. Write a function that receives as parameter a list of numbers 
# (integers) and will return a tuple with 2 elements. The first 
# element of the tuple will be the number of palindrome numbers 
# found in the list and the second element will be the greatest 
# palindrome number.
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
def function(lista):
    c = 0 # nr de palindroame
    x = 0 # cel mai mare palindrom
    for i in lista:
        if palindrom(i):
            c +=1
        if palindrom(i) and x<i:
            x = i
    return (c,x)
lista = [3, 111, 64182, 64, 676, 5656565]
tuple = function(lista)
print(tuple)

# 8. Write a function that receives a number x, default value equal 
# to 1, a list of strings, and a boolean flag set to True. For each 
# string, generate a list containing the characters that have 
# the ASCII code divisible by x if the flag is set to True, 
# otherwise it should contain characters that have the ASCII code 
# not divisible by x. Example:
# x = 2, ["test", "hello", "lab002"], flag = False 
# will return (["e", "s"], ["e"]) . Note: The function must return 
# list of lists.

def function(lista = [],x = 1, flag = True):
    final = []
    for i in lista:
        filter = []
        for j in i:
            if ord(j)%x == 0 and flag == True:
                filter.append(j)
            if ord(j)%x != 0 and flag == False:
                filter.append(j)
        if filter != []:
            final.append(filter)
    return final
x=2
lista = ["test", "hello", "lab002"]
flag = False
print(function(["test", "hello", "lab002"], 2, False))

# 9. Write a function that receives as paramer a matrix which 
# represents the heights of the spectators in a stadium and will 
# return a list of tuples (line, column) each one representing a 
# seat of a spectator which can't see the game. A spectator can't 
# see the game if there is at least one taller spectator standing 
# in front of him. All the seats are occupied. All the seats are at 
# the same level. Row and column indexing starts from 0, beginning 
# with the closest row from the field. Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7, 6, 7, 5]] 
# Will return : [(2, 2), (3, 4), (2, 4)]

def function(mat):
    final = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            curent = mat[i][j]
            ok = True
            for k in range(i):
                if mat[k][j] >= curent:
                    ok = False
                    break
            if ok == False:
                final.append((i, j))
    return final

mat = [[1, 2, 3, 2, 1, 1],
       [2, 4, 4, 3, 7, 2],
       [5, 5, 2, 5, 6, 4],
       [6, 6, 7, 6, 7, 5]] 
print(function(mat))

# 10. Write a function that receives a variable number of lists and 
# returns a list of tuples as follows: the first tuple contains the 
# first items in the lists, the second element contains the items \
# on the position 2 in the lists, etc. Example: 
# for lists [1,2,3], [5,6,7], ["a", "b", "c"] 
# return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 
# Note: If input lists do not have the same number of items, missing 
# items will be replaced with None to be able to generate 
# max ([len(x) for x in input_lists]) tuples.

def function(*lists):
    lung = max(len(l) for l in lists)
    final =[]
    for i in range(lung):
        a =[]
        for j in lists:
            if i < len(j):
                a.append(j[i])
            else:
                a.append(None)
        final.append(a)
    return final
print(function([1,2,3,9], [5,6,7], ["a", "b", "c"]))

# 11. Write a function that will order a list of string tuples based 
# on the 3rd character of the 2nd element in the tuple. Example:
#[('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def function(lists):
    n = len(lists)
    for i in range(n):
        for j in range(0, n - i - 1): 
            chr1 = lists[j][1][2] # j-pozitia listei, [1]-primul cuv, [2]-caract
            chr2 = lists[j + 1][1][2]
            if ord(chr1) > ord(chr2):
                aux = lists[j]
                lists[j] = lists[j + 1]
                lists[j + 1] = aux
    return lists
print(function([('abc', 'bcd'), ('abc', 'zza'),('aas','htb')]))

# 12. Write a function that will receive a list of words as parameter 
# and will return a list of lists of words, grouped by rhyme. 
# Two words rhyme if both of them end with the same 2 letters. 
# Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) 
# will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

def group_by_rhyme(lists):
    final = {}
    for i in lists:
        a = i[-2:]
        if a in final:
            final[a].append(i)
        else:
            final[a]=[i]
    return final.values()
print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
