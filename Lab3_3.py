import pickle
import sys


def display_menu():
    print("1. Add file")
    print("2. Calculate")


def cross_reference(files):
    numbers = set()

    for file in files:
        temp = set()

        try:
            file = open(file, "r")
        except:
            print(f"Error: There was a problem with at least one of the files.")
            exit()

        end = False
        # loops until the end of the file
        while not end:
            number = file.readline()
            if not number:
                end = True
            else:
                temp.add(number.replace('\n', ''))

        if len(numbers) == 0:
            numbers = temp
        else:
            numbers = numbers.intersection(temp)

    return numbers


def map_numbers_to_names(numbers, filename):
    names = []

    try:
        file = open(filename, "rb")
        # if it cannot then prints error
    except:
        print(f"An error occurred while trying to read the file.")
        exit()

    dict = pickle.load(file)

    for number in numbers:
        if number in dict:
            names.append(dict[number])
        else:
            names.append(f'Unknown ({number})')
    return names


def display_suspects(names):
    print("The following persons was present on all crime scenes:")
    print("-" * 46)
    print("suspects involved ")
    for name in names:
        print(f'sdskdskdskdks: {name}')


def main():
    filename = sys.argv[1]
    files = []

    choice = '1'
    while choice != '2':
        display_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter a filename (include full path): ")
            files.append(name)
        elif choice == '2':
            numbers = cross_reference(files)
            names = map_numbers_to_names(numbers, filename)
            display_suspects(names)
        else:
            print("Incorrect, try again")


if __name__ == '__main__':
    main()
