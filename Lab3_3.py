import pickle
import sys


def display_menu():
    print("1. Add file")
    print("2. Calculate")


# an empty set that will hold the phone numbers
def cross_reference(files):
    # all the numbers in all the list
    numbers = set()

    for file in files:
        # holds numbers from a specific file
        numbers_in_file = set()
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
                numbers_in_file.add(number.replace('\n', ''))
        # if this is the first file -- no comparing is needed
        if len(numbers) == 0:
            numbers = numbers_in_file
        else:
            # it checks what numbers are in both files
            numbers = numbers.intersection(numbers_in_file)
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
    # if there are common vcalues
    print("The following persons was present on all crime scenes:")
    print("-" * 54)
    if len(names) == 0:
        print("No matches")
    else:
        for name in names:
            print(f'{name}')


def main():
    filename = sys.argv[1]
    files = []

    choice = '1'
    while choice != '2':
        display_menu()
        choice = input("Enter choice: ")
        # if user enters 1
        if choice == '1':
            name = input("Enter a filename (include full path): ")
            # adds to the file list
            files.append(name)
        elif choice == '2':

            numbers = cross_reference(files)
            names = map_numbers_to_names(numbers, filename)
            display_suspects(names)
        else:
            print("Incorrect, try again")


if __name__ == '__main__':
    main()
