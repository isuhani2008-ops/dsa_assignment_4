# ==========================================================
# HASH TABLE USING SEPARATE CHAINING
# ==========================================================

# Operations:
# 1. Insert
# 2. Search
# 3. Delete
# 4. Collision Handling


class HashTable:

    def __init__(self, size):

        self.size = size

        self.table = [[] for _ in range(size)]


    # ------------------------------------------------------
    # HASH FUNCTION
    # ------------------------------------------------------

    def hash_function(self, key):

        return key % self.size


    # ------------------------------------------------------
    # INSERT
    # ------------------------------------------------------

    def insert(self, key, value):

        index = self.hash_function(key)

        self.table[index].append((key, value))

        print(f"Inserted ({key}, {value}) at index {index}")


    # ------------------------------------------------------
    # SEARCH
    # ------------------------------------------------------

    def search(self, key):

        index = self.hash_function(key)

        for k, v in self.table[index]:

            if k == key:
                return v

        return "Key not found"


    # ------------------------------------------------------
    # DELETE
    # ------------------------------------------------------

    def delete(self, key):

        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):

            if k == key:
                del self.table[index][i]
                print(f"Deleted key {key}")
                return

        print("Key not found")


    # ------------------------------------------------------
    # DISPLAY
    # ------------------------------------------------------

    def display(self):

        print("\nHash Table:")

        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)



# ==========================================================
# DRIVER CODE
# ==========================================================

ht = HashTable(5)

# Insert values
ht.insert(10, "Apple")
ht.insert(15, "Banana")
ht.insert(20, "Mango")

# Collision example
# 10 % 5 = 0
# 15 % 5 = 0
# 20 % 5 = 0

ht.display()

# Search
print("\nSearch key 15:")
print(ht.search(15))

# Delete
ht.delete(15)

ht.display()