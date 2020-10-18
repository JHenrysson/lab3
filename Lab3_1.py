import sys


def read_file(filename):
    try:
        log_file = open(filename, 'r')
    except:
        # if the file is not valid then this message will be printed
        print(f"Error: The file '{filename}' could not be found.")
        exit()

def map_to_int(measurements):


def find_faulty(primary, secondary, threshold):


def display_warnings(faulty_sensors):
    pass


def main():
    filename = sys.argvs[1]
    filename1 = sys.argvs[2]
    measurements = read_file(filename)
    primary = map_to_int(measurements)
    measurement2nd = read_file(filename1)
    secondary = map_to_int(measurement2nd)
    threshold = 2
    faulty_sensors = find_faulty(primary, secondary, threshold)
    display_warnings(faulty_sensors)


if __name__ == '__main__':
    main()
