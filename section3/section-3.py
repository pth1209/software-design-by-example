import sys
import hashlib
from hashlib import sha256

CHUNK_SIZE = 8192

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

# Runtime: O(n^2 / g) where n is number of files and g is number of groups
def find_groups(filenames):
    groups = {}
    for file_name in filenames:
        file_data = open(file_name, "rb").read()
        hash_code = naive_hash(file_data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(file_name)

    return groups

# groups = find_groups(sys.argv[1:])
# for filenames in groups.values():
#     duplicates = find_duplicates(list(filenames))
#     for (left, right) in duplicates:
#         print(left, right)

# Section 3.3: Better hashing
# Use SHA-256 algorithm
def find_groups(filenames):
    groups = {}
    for file_name in filenames:
        file_data = open(file_name, "rb").read()
        sha256_hash_code = sha256(file_data).hexdigest()
        if sha256_hash_code not in groups:
            groups[sha256_hash_code] = set()
        groups[sha256_hash_code].add(file_name)

    return groups

# groups = find_groups(sys.argv[1:])
# for filenames in groups.values():
#     print(", ".join(sorted(filenames)))

# Section 3.5: Exericses

# 3.5.1
# The odds of collision occuring when hasing four files:
# 1 - P(none of the files having hash collision) = 1 - (1 * 3/4 * 2/4 * 1/4) = 29/32 (approximately 91%)

# 3.5.2
def hash_file(filename):
    hasher = sha256()
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()

def find_groups(filenames):
    groups = {}
    for file_name in filenames:
        sha256_hash_code = hash_file(file_name)
        if sha256_hash_code not in groups:
            groups[sha256_hash_code] = set()
        groups[sha256_hash_code].add(file_name)

    return groups

groups = find_groups(sys.argv[1:])
for filenames in groups.values():
    print(", ".join(sorted(filenames)))

#3.5.3

# "Rapidly" -> O(n^2) or worse. Often O(2^n) in worst case

#3.5.4

# object.__hash__ is called by the built-in function hash().
# the only required properly for the __hash__ function is that objects which compare equal have the same hash value.
# strings and integers are immutable, while arrays are mutable. 
# the hash value of a unique string or integer will never change.\
