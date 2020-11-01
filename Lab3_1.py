import sys
import pickle


def read_file(filename):
    # tries to open the file
    try:
        file = open(filename, "rb")
    # if it cannot then prints error
    except:
        print(f'Error: The files given as arguments are not valid.')
        exit()
    # returns file contents as dictionary
    return pickle.load(file)


def map_to_int(measurements):
    # a for loop to go through the dictionary
    for key, value in measurements.items():
        # slices last character of value and turns in to an int
        measurements[key] = int(value[:-1])

    return measurements


def find_faulty(primary, secondary, threshold):
    faulty_sensors = set()
    for key, value in primary.items():
        secondaryValue = secondary.get(key)
        if abs(value - secondaryValue) > threshold:
            faulty_sensors.add(key)

    return faulty_sensors


def display_warnings(faulty_sensors):
    print("Analyzis of the provided files is complete.")
    print('-' * 43)

    print("\nThe following sensors differ more than 2°:")
    # looping through the list to get the value of each item in the list
    for faulty_sensor in faulty_sensors:
        print(faulty_sensor)


def main():
    filename = sys.argv[1]
    filename1 = sys.argv[2]
    measurements = read_file(filename)
    primary = map_to_int(measurements)
    measurement2nd = read_file(filename1)
    secondary = map_to_int(measurement2nd)
    threshold = 2
    faulty_sensors = find_faulty(primary, secondary, threshold)
    display_warnings(faulty_sensors)


if __name__ == '__main__':
    main()
