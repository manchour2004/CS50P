class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self._size > self._capacity:
            raise ValueError("Can't deposit more than capacity")
        self.size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Can't withdraw more than size")
        self.size -= n


    @property
    def capacity(self):
         return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not 0 <= value <= self.capacity:
            raise ValueError("Size is beyond range")
        self._size = value



def main():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)


if __name__ == "__main__":
    main()