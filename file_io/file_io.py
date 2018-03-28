def read_from_file_1(file_name):
    counter_dict = {}
    with open(file_name) as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()
    return counter_dict

def read_from_file_2(file_name, start_index, end_index):
    counter_dict = {}
    with open(file_name) as f:
        line = f.readline()
        while line:
            line = line[start_index:end_index]
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()
    return counter_dict

def read_from_file_3(file_name):
    counter_dict = {}
    with open(file_name) as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()
    return counter_dict

def main():
    print(read_from_file_1('nameslist.txt'))
    print(read_from_file_2('Training_01.txt', 3, -26))

if(__name__ == "__main__"):
    main()

