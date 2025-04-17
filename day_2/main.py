"""
Advent Of Code Day 2
author: Olivier Hauterville
"""

def is_safe_line(line, max_jump=3):
    """
    Check if a line is safe based on the given maximum jump.
    """
    slope = 1 if int(line[1]) > int(line[0]) else -1
    for i in range(len(line)-1):
        jump = abs(int(line[i])-int(line[i+1]))
        new_slope = 1 if int(line[i+1]) > int(line[i]) else -1
        
        if jump > max_jump or new_slope != slope or jump == 0:
            return False
    return True

def pop(line, i):
    """
    Pop an element from the line at index i.
    """
    return line[:i] + line[i+1:]

if __name__ == "__main__":
    input_filename = "input.txt"  # Replace with your actual input file name
    
    nb_safe = 0
    nb_danger = 0
    
    try:
        with open(input_filename, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.split()

                safe = is_safe_line(line)   
                
                if safe:
                    nb_safe += 1
                else: 
                    a = 0
                    for i in range(len(line)):
                        new_line = line[:i] + line[i+1:]
                        new_safe = is_safe_line(new_line)
                        if new_safe:
                            a += 1

                    if a > 0:
                        nb_safe += 1
                    else:        
                        nb_danger += 1      

        print(f"Number of safe lines: {nb_safe}")
        print(f"Number of dangerous lines: {nb_danger}")
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
    except ValueError:
        print("Invalid data format in the input file.")


