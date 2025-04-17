""" 
AdventOfCode Day 2 
author: Olivier Hauterville
"""
def get_input(input_filename:str):
    # List to store the lines read from the file
    list1 = []
    list2 = []

    try:
        with open(input_filename, 'r') as f:
            for line in f:
                line = line.strip()
                parts = line.split()

                list1.append(int(parts[0]))
                list2.append(int(parts[1]))
                
        print(f"Successfully read lines from {input_filename}.")
        return list1, list2
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        print("Make sure it's in the same directory as the Python script, or provide the full path.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def get_occurrences(lst, number):
    """
    Returns the number of occurrences of a given number in a list.
    """
    return lst.count(number)


if __name__ == "__main__":
    # Read input from the file
    list1, list2 = get_input("../input/input.txt")

    similitude = 0

    for i in range(len(list1)):
        number = list1[i]
        similitude += number * get_occurrences(list2, number)

    print(f"Similitude: {similitude}")