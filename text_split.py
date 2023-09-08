import os

def split_file(file_path, lines_per_file):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # Create /split directory if it doesn't exist
    if not os.path.exists('split'):
        os.makedirs('split')
        
    for i in range(0, len(lines), lines_per_file):
        file_name = f"split/acnh_{str(i//lines_per_file).zfill(4)}.txt"
        with open(file_name, 'w') as new_file:
            new_file.writelines(lines[i:i+lines_per_file])

split_file('Animal Crossing New Horizons.txt', 10)
