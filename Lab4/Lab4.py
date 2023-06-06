# 1. Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un
# director. Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica)
# a fișierelor din directorul dat ca parametru.
import os


def ex1(path):
    extensions = []
    list_ = os.listdir(path)
    for file_ in list_:
        filename, ext = os.path.splitext(file_)
        extensions.append(ext)
    extensions.sort()
    return extensions


dirpath = "C:/Users/Amalia/Desktop/INFO_ANUL_3/random"
print(ex1(dirpath))

# 2. Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

import os


def ex2(dir, fisier):
    write_file = open(fisier, mode='w')
    for root, directories, files in os.walk(dir):
        for file in files:
            if file.startswith('A'):
                write_file.write(os.path.join(root,file))
                write_file.write("\n")


a = "C:/Users/Amalia/Desktop/INFO_ANUL_3/random"
b = "C:/Users/Amalia/Desktop/INFO_ANUL_3/Python/Lab4/outputEx2.txt"
print(ex2(a, b))

# 3.Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul
# fișierului. Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple
# (extensie, count), sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar
# count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din
# directorul dat ca parametru.

import os


def sort_rule(tuple_):
    return tuple_[1]


def sort_list(input_):
    input_.sort(key=sort_rule, reverse=True)
    return input_

def get_files_extensions_count_from_dir(dir_path):
    # if not os.path.isdir(dir_path):
    #     raise ValueError("Calea directorului nu indica un director existent")
    extensions = dict()
    for (root, dirs, files) in os.walk(dir_path, topdown=True):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension:
                extension = extension[1:]
                if extension in extensions:
                    extensions[extension] += 1
                else:
                    extensions[extension] = 1
    list_ext = list()
    for item in extensions:
        list_ext.append((item, extensions[item]))

    return sort_list(list_ext)


def check_path(my_path):
    if not os.path.exists(my_path):
        raise ValueError("Calea data nu indica un director/fisier existent")
    if os.path.isfile(my_path):
        with open(my_path, 'rt') as f:
            content = f.read()
            return content[-20:]
    if os.path.isdir(my_path):
        return get_files_extensions_count_from_dir(my_path)


path_dir = "C:/Users/Amalia/Desktop/INFO_ANUL_3/Python/Lab4/fisiere_ex3"
path_file = r'C:/Users/Amalia/Desktop/INFO_ANUL_3/Python/Lab4/fisiere_ex3/selena.txt'
print("Ex3:\nPath: {}\nResult: {}".format(path_dir, check_path(path_dir)))
print("Ex3:\nPath: {}\nResult: {}".format(path_file, check_path(path_file)))


# 4. Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat
# ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
import os


def ex4():
    ext_list = []
    directory = input("Enter directory:")
    for root, directories, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension not in ext_list:
                ext_list.append(extension)
    ext_list.sort()
    return ext_list


print(ex4())


# C:\Users\Amalia\Desktop\INFO_ANUL_3\Python\Lab4\fisiere_ex3


# 5. Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
# returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este
# un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate
# fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție
# de tipul ValueError cu un mesaj corespunzator.

import os
def search_text(path, to_search):
    if not os.path.exists(path):
        raise ValueError("Calea data nu indica un director/fisier existent")
    if os.path.isfile(path):
        with open(path, 'rt', encoding="utf-8", errors='ignore') as f:
            content = f.read()
            if to_search in content:
                return "String-ul '{}' se regaseste in fisierul {}.".format(to_search, path)
    elif os.path.isdir(path):
        files_list = list()
        for (root, dirs, files) in os.walk(path, topdown=True):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rt', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if to_search in content:
                        files_list.append(file_path)
        return "String-ul '{}' se regaseste in fisierele {}.".format(to_search, files_list)


path_to_search = r'fisiere_ex3'
string_to_search = 'a'
print("\nEx5:\n{}".format(search_text(path_to_search, string_to_search)))

# 6. Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior,
# cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru,
# iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța
# excepției ca parametru.
import os
def callback(param, path):
    print("Eroare pentru fisierul {}: {}".format(path, param))


def search_text(path, to_search, callback_function):
    if os.path.isfile(path):
        try:
            with open(path, 'rt', encoding="utf-8") as f:
                content = f.read()
                if to_search in content:
                    return "String-ul '{}' se regaseste in fisierul {}.".format(to_search, path)
        except Exception as e:
            callback_function(e, path)

    elif os.path.isdir(path):
        files_list = list()
        for (root, dirs, files) in os.walk(path, topdown=True):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rt', encoding='utf-8') as f:
                        content = f.read()
                        if to_search in content:
                            files_list.append(file_path)
                except Exception as e:
                    callback_function(e, file_path)
        return "String-ul '{}' se regaseste in fisierele {}.".format(to_search, files_list)


path_to_search = "C:/Users/Amalia/Desktop/INFO_ANUL_3/Python/Lab4/fishhiere_ex3"
string_to_search = 'a'
print("\nEx6:\n{}".format(search_text(path_to_search, string_to_search, callback)))


# 7.Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către
# un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.

import os
def get_data(path):
    if not os.path.isfile(path):
        raise ValueError("{} nu este fisier".format(path))
    data = dict()
    data.setdefault('full_path', os.path.abspath(path))
    data.setdefault('file_size', os.path.getsize(path))
    data.setdefault('file_extension', os.path.splitext(path)[1])
    data.setdefault('can_read', os.access(path, os.R_OK))
    data.setdefault('can_write', os.access(path, os.W_OK))

    return data


file_path = r'C:\Users\Amalia\Desktop\INFO_ANUL_3\Python\Lab4\output.txt'
print("\nEx7:\nPentru fisierul {} datele sunt:\n".format(file_path))
print(get_data(file_path))


# 8. Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea
# către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor
# aflate în rădăcina directorului dir_path.

import os
def get_files(path):
    if not os.path.isdir(path):
        raise ValueError("Calea data nu este director!")
    abs_paths = list()
    for item in os.listdir(path):
        abs_path = os.path.join(path, item)
        if os.path.isfile(abs_path):
            abs_paths.append(abs_path)
    return abs_paths


path_dir = "C:/Users/Amalia/Desktop/INFO_ANUL_3/Python/Lab4/fisiere_ex3"
print("\nEx8:\nFisierele din director: {}".format(get_files(path_dir)))

