class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size #keys
        self.data = [None] * self.size  #data

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, key):
        return key // self.size if self.size > 1 else 1

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                rehashvalue = self.rehash(key)
                if self.slots[rehashvalue] is None:
                    self.slots[rehashvalue] = key
                    self.data[rehashvalue] = data
                else:
                    print("Unresolved collisions, data was lost. ")


    def get(self, key):
        start = self.hashfunction(key)
        position = start
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            position = (position + 1) % self.size
            if position == start:
                break
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H = HashTable()
H[69] = 'A'
# Store remaining input data
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# Print the slot values
print(H.slots)

# Print the data values
print(H.data)

# Print the value of the data for key 52
print(H[89])
