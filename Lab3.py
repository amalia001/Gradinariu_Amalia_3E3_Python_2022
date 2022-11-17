# 1. Write a function that receives as parameters two lists a and b and returns a list of sets
# containing: (a intersected with b, a reunited with b, a - b, b - a)

def ex1(list1, list2):
    l1 = set(list1)
    l2 = set(list2)
    print("Intersection: ", l1.intersection(l2))
    print("Union: ", l1.union(l2))
    print("l1-l2: ", l1.difference(l2))
    print("l2-l1: ", l2.difference(l1))


x = [1, 1, 3, 4, 5, 5, 3, 8]
y = [7, 7, 4, 33, 9, 0, 0]
ex1(x, y)


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys
# are the characters in the character string and the values are the number of occurrences of that
# character in the given text.

def ex2(text):
    dictionar = dict()
    for character in text:
        if character in dictionar.keys():
            dictionar[character] += 1
        else:
            dictionar[character] = 1
    return dictionar


print(ex2("Ana has apples."))


# 3. Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def ex3(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for key in dict1:
        if key not in dict2:
            return False
        if type(dict1[key]) is dict:
            if not ex3(dict1[key], dict2[key]):
                return False
        elif dict1[key] != dict2[key]:
            return False
    return True


a = {1:{"a": [1, 2], "b": [6, 7]}}
b = {1:{"a": [1, 2], "b": [6, 7]}}
print(ex3(a, b))

# 4.The build_xml_element function receives the following parameters: tag, content, and key-value
# elements given as name-parameters. Build and return a string that represents the corresponding XML
# element.

def build_xml_element(tag, content, **keyValue):
    string = '<' + tag
    for key, value in keyValue.items():
        string += ' ' + key + '=\\\"' + value.strip() + '\\\"'
    string += '> ' + content + ' </' + tag + '>'
    return string


print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))


# 5.  The validate_dict function that receives as a parameter a set of tuples ( that represents
# validation rules for a dictionary that has strings as keys and values) and a dictionary. A rule
# is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it
# starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.

def ex5(tupleSet, mydict):
    for tp in tupleSet:
        prefix = tp[1]
        middle = tp[2]
        sufix = tp[3]
        ok = 0
        for key in mydict:
            ok = 1
            if int(tp[0]) == int(key):
                pref_len = len(prefix)
                suf_len = len(sufix)
                if mydict[key][0:pref_len] == prefix and mydict[key][-suf_len:] == sufix:
                    rest = mydict[key][pref_len:len(mydict[key]) - suf_len:1]
                    if middle in rest:
                        ok = 1
                    else:
                        ok = 0
                else:
                    ok = 0
            if ok == 0:
                return False
    return True


d = {'1': 'bunaziua', '2': 'cefacitu', '3': 'suntbine'}
s = {(1, "bu", "az", "ua")}
t2 = (2, "ce", "ac", "tu")
t3 = (3, "su", "tb", "ne")

s.add(t2)
s.add(t3)
print(ex5(s, d))


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing
# the number of unique elements in the list, and b representing the number of duplicate elements
# in the list.

def ex6(myList):
    mydict = dict()
    for element in myList:
        if element in mydict.keys():
            mydict[element] += 1
        else:
            mydict[element] = 1
    count_uniques = 0
    count_dup = 0
    for each_item in mydict:
        if mydict[each_item] > 1:
            count_dup += 1
        elif mydict[each_item] == 1:
            count_uniques += 1
    my_tuple = (count_uniques, count_dup)
    return my_tuple


mylist = [1, 2, 3, 4, 1, 3, 6]  # 2 4 6 / 1, 3
print(ex6(mylist))


# 7. Write a function that receives a variable number of sets and returns a dictionary with the
# following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have
# the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.

def ex7(*sets):
    my_dict = dict()
    for i in range(len(sets) - 1):
        a = sets[i]
        b = sets[i + 1]
        operators = ["|", "&", "-"]
        a_string = str(a)
        b_string = str(b)
        for operator in operators:
            final_key = a_string + " " + operator + " " + b_string
            if operator == "|":
                my_dict[final_key] = a.union(b)
            if operator == "&":
                my_dict[final_key] = a.intersection(b)
            if operator == "-":
                my_dict[final_key] = a.difference(b)
                final_key2 = b_string + " " + operator + " " + a_string
                my_dict[final_key2] = b.difference(a)
        # my_dict[final_key] = b.difference(a)
    return my_dict


print(ex7({1, 2}, {2, 3}))


# 8. Write a function that receives a single dict parameter named mapping. This dictionary always
# contains a string key "start". Starting with the value of this key you must obtain a list of objects
# by iterating over mapping in the following way: the value of the current key is the key for the next
# value, until you find a loop (a key that was visited before). The function must return the list of
# objects obtained as previously described.
#
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
# will return ['a', '6', 'z', '2']

def get_list(mapping):
    visited_keys = ['start']
    result = [mapping['start']]
    key = mapping['start']
    while True:
        if mapping[key] not in visited_keys:
            visited_keys.append(mapping[key])
        else:
            break
        result.append(mapping[key])
        key = mapping[key]
    return result


input_dict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print('Result:{}'.format(get_list(input_dict)))


# myDict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
# ex8(myDict)

# 9. Write a function that receives a variable number of positional arguments and a variable number of
# keyword arguments adn will return the number of positional arguments whose values can be found among
# keyword arguments values.
#
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3

def ex9(*values, **keywords):
    n = 0
    for value in values:
        if value in keywords.values():
            n += 1
    return n


print('Result: {}'.format(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5)))
