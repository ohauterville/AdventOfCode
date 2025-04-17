"""
Advent Of Code Day 2
author: Olivier Hauterville
"""

if __name__ == "__main__":
    input_filename = "input.txt"  # Replace with your actual input file name
    
    max_jump = 3
    nb_safe = 0
    nb_danger = 0
    
    try:
        with open(input_filename, 'r') as f:
            for line in f:
                line = line.strip()
                parts = line.split()
                safe = True

                for i in range(len(parts)-1):
                    jump = abs(int(parts[i])-int(parts[i+1]))
                    
                    if i == 0:
                        slope = 1 if int(parts[i+1]) > int(parts[i]) else -1
                        new_slope = slope
                    else:
                        new_slope = 1 if int(parts[i+1]) > int(parts[i]) else -1

                    if jump > max_jump or new_slope != slope or jump == 0:
                        safe = False
                        break

                if safe:
                    nb_safe += 1
                    print(f"Safe line: {line}")
                else:   
                    nb_danger += 1      

        print(f"Number of safe lines: {nb_safe}")
        print(f"Number of dangerous lines: {nb_danger}")
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
    except ValueError:
        print("Invalid data format in the input file.")


