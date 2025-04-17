""" 
AdventOfCode Day 1 
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

def get_and_remove_smallest_in_place(data_list):
    if not data_list:  # Handle empty list case
        print("Error: List is empty.")
        return data_list

    smallest_element = min(data_list)
    data_list.remove(smallest_element) # Modifies the list in place
    return smallest_element, data_list

if __name__ == "__main__":
    # Example usage
    input_filename = "../input/input.txt"  # Replace with your actual input file name
    list1, list2 = get_input(input_filename)
    print("List 1:", list1[:5], "...")  # Print first 5 elements for brevity
    print("List 2:", list2[:5], "...")

    ## main loop
    steps = len(list1)
    length = 0 
    value1 = 0
    value2 = 0

    for _ in range(steps):
        # Remove the smallest element from list1
        value1, list1 = get_and_remove_smallest_in_place(list1)
        value2, list2 = get_and_remove_smallest_in_place(list2)
        
        length += abs(value1 - value2)
    
    print(f"The length of these two lists is {length}")