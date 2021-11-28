import glob
import math


def write_files():
    with open('file1.txt', 'w') as f:
        for i in range(10):
            f.write("{}\n".format(i ** 2))

    with open('file2.txt', 'w') as f:
        f.write("{}\n{}\n{}\n".format("red", "green", "blue"))


def read_files():
    filenames = glob.glob("*.txt")
    dico = {}
    for file in filenames:
        with open(file, 'r') as f:
           dico[file] = f.read().splitlines()
        print(dico)


def write_read_file():
    with open("triple.txt", 'w') as f:
        for i in range(10):
            f.write("{}\n".format(i**3))

    liste = [int(i.strip()) for i in open('triple.txt', 'r')]
    print(liste)





