# Nested List Printer: Print all elements in a nested list

def print_all(nested_list):
    for sublist in nested_list:
        for element in sublist:
            print(element)

if __name__ == "__main__":
    sample_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
    print_all(sample_list)
