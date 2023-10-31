# 1. Write a function that receives as parameters two lists a and b and 
# returns a list of sets containing: (a intersected with b, a reunited with b,
# a - b, b - a)

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
    rez =  [set(intersectie), set(reuniune), set(diferenta_a), set(diferenta_b)]

    return rez
a = [1, 6, 9, 546, 712, 435, 624]
b = [4, 47, 546, 0, 25, 624, 42]  
print(function(a,b))


# 2. Write a function that receives a string as a parameter and returns a 
# dictionary in which the keys are the characters in the character string 
# and the values are the number of occurrences of that character in the given 
# text. Example: For string "Ana has apples." given as a parameter the function 
# will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

def function(s):
    dictionar = {}
    l = len(s)
    for i in s:
        if i in dictionar:
            dictionar[i] += 1
        else:
            dictionar[i] = 1
    return dictionar
s = "Ana has apples."
print(function(s))

# 3. Compare two dictionaries without using the operator "==" returning True
#  or False. (Attention, dictionaries must be recursively covered because 
# they can contain other containers, such as dictionaries, lists, sets, etc.)
def function(dict1, dict2):
    if type(dict1) is not dict or type(dict2) is not dict:
        return False

    if set(dict1.keys()) != set(dict2.keys()):
        return False
    for key in dict1:
        val1 = dict1[key]
        val2 = dict2[key]
        if type(val1) is dict and type(val2) is dict:
            if not function(val1, val2):
                return False
        elif type(val1) is list and type(val2) is list:
            if not compare_lists(val1, val2):
                return False
        elif type(val1) is set and type(val2) is set:
            if not compare_lists(list(val1), list(val2)):
                return False
        elif val1 != val2:
            return False

    return True

def compare_lists(list1, list2):
    if type(list1) is not list or type(list2) is not list:
        return False

    if len(list1) != len(list2):
        return False
    for i1, i2 in zip(list1, list2):
        if type(i1) is dict and type(i2) is dict:
            if not function(i1, i2):
                return False
        elif type(i1) is list and type(i2) is list:
            if not function(i1, i2):
                return False
        elif type(i1) is set and type(i2) is set:
            if not function(list(i1), list(i2)):
                return False
        elif i1 != i2:
            return False
    return True
dict1 = {
    'a': 9,
    'b': [8, 3],
    'c': {'e': 4, 'f': [5, 6]},
    'd': ("cg", 8)
}
dict2 = {
    'a': 9,
    'b': [8, 3],
    'c': {'e': 4, 'f': [5, 6], 'r': []},
    'd': ("cg", 8),
}
print(function(dict1, dict2))

# 4. The build_xml_element function receives the following parameters: tag, 
# content, and key-value elements given as name-parameters. Build and return 
# a string that represents the corresponding XML element. 
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", 
# _class =" my-link ", id= " someid ") 
# returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "

def build_xml_element(tag, content, **kwargs):
    xml = "<" + tag
    for key, value in kwargs.items():
        xml += ' ' + key + '"="' + value + '\ "'
    xml += '> ' + content
    return xml 
print(build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

# 5. The validate_dict function that receives as a parameter a set of tuples 
# ( that represents validation rules for a dictionary that has strings as keys
#  and values) and a dictionary. A rule is defined as follows: 
# (key, "prefix", "middle", "suffix"). A value is considered valid if it starts 
# with "prefix", "middle" is inside the value (not at the beginning or end) 
# and ends with "suffix". The function will return True if the given dictionary 
# matches all the rules, False otherwise. Example: 
# the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} 
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} 
# => False because although the rules are respected for "key1" and "key2" "key3" 
# that does not appear in the rules.
 
def validate_dict(reguli, dictionar):
    for key, prefix, middle, sufix in reguli:
        if key in dictionar:
            value = dictionar[key]
            text = value.split()
            if len(text) > 1:
                prefix_dict = text[0]
                sufix_dict = text[-1]
                if (prefix_dict == prefix or not prefix) and (sufix_dict == sufix or not sufix):
                    for i in text[1:-1]:
                        if i == middle:
                            return True
            else:
                return False
        else:
            return False
    return True
s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(validate_dict(s,d)) 

# 6. Write a function that receives as a parameter a list and returns a tuple
#  (a, b), representing the number of unique elements in the list, 
# and b representing the number of duplicate elements in the list 
# (use sets to achieve this objective).

def function(lista):
    unic = set(lista)
    elem_duplicate = set(filter(lambda x:lista.count(x)>1,unic))
    elem_unic = unic - elem_duplicate
    tuplu = (len(elem_duplicate), len(elem_unic))
    return tuplu

# 7. Write a function that receives a variable number of sets and returns a
# dictionary with the following operations from all sets two by two: reunion,
# intersection, a-b, b-a. The key will have the following form: "a op b", 
# where a and b are two sets, and op is the applied operator: |, &, -. Ex:
#   {1,2}, {2, 3} =>
#   {
#    "{1, 2} | {2, 3}":  {1, 2, 3},
#    "{1, 2} & {2, 3}":  { 2 },
#    "{1, 2} - {2, 3}":  { 1 },
#    ...
#   }

def function(*seturi):
    rez = {}
    for i in range(len(seturi)):
        for j in range(i+1, len(seturi)):
            set1 = set(seturi[i])
            set2 = set(seturi[j])
            reunion = str(set1) + ' | ' + str(set2)
            intersect = str(set1) + ' & ' + str(set2)
            diff_a = str(set1) + ' - ' + str(set2)
            diff_b = str(set2) + ' - ' + str(set1)
            rez[reunion] = set1.union(set2)
            rez[intersect] = set1.intersection(set2)
            rez[diff_a] = set1.difference(set2)
            rez[diff_b] = set2.difference(set1)
    for key, value in rez.items():
        print(key + ' : ', value)
set1 = {1,2} 
set2 = {2,3}
print(function(set1,set2))

# 8. Write a function that receives a single dict parameter named mapping. 
# This dictionary always contains a string key "start". Starting with the 
# value of this key you must obtain a list of objects by iterating over 
# mapping in the following way: the value of the current key is the key for 
# the next value, until you find a loop (a key that was visited before). 
# The function must return the list of objects obtained as previously 
# described. Ex:
# loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']

def loop(mapping):
    viz = []
    rez = []
    key = "start"
    while key not in viz:
        viz.append(key)
        if mapping[key] not in rez:
            rez.append(mapping[key])
        key = mapping[key]
    return rez
print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

# 9. Write a function that receives a variable number of positional arguments
#  and a variable number of keyword arguments adn will return the number of
#  positional arguments whose values can be found among keyword arguments
#  values. Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

def my_function(*args, **kwargs):
    c = 0
    for arg in args:
        for value in kwargs.values():
            if arg == value:
                c += 1 
    return c

func = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(func)
