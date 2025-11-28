import sys

# 3.1
# Inefficient N^2 approach to find duplicates

def same_bytes(left_name, right_name):
    # read file in binary mode, which returns bytes
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()

    return left_bytes == right_bytes

def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left_filename = filenames[i_left]
        for i_right in range(i_left):
            right_filename = filenames[i_right]
            if same_bytes(left_filename, right_filename):
                matches.append((left_filename, right_filename))

    return matches

# duplicates = find_duplicates(sys.argv[1:])
# for (left, right) in duplicates:
#     print(left, right)

# 3.2 Hashing files
# Instead of comparing every file against every other
# process each file and produce a short identifier 
# that depends on file's content and then compare that identifier

def naive_hash(data):
    return sum(data) % 13

def find_groups(filenames):
    groups = {}
    for file_name in filenames:
        file_data = open(file_name, "rb").read()
        hash_code = naive_hash(file_data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(file_name)

    return groups

groups = find_groups(sys.argv[1:])
for filenames in groups.values():
    duplicates = find_duplicates(list(filenames))
    for (left, right) in duplicates:
        print(left, right)
