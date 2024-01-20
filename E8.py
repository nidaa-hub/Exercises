from collections import defaultdict


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = defaultdict(list)

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value
        return None

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
        if not self.table[index]:
            self.table[index] = None

    def printHash(self):
        result = ""
        for index, entries in self.table.items():
            result += f"{entries}\n"
        print(result)

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None


hash_table = HashTable(size=10)
hash_table.insert("name", "John")
hash_table.insert("age", 26)
hash_table.insert("city", "New York")
hash_table.insert("name", "Jane")
hash_table.printHash()
hash_table.delete("city")
hash_table.printHash()
print("The age is :", hash_table.search("age"))