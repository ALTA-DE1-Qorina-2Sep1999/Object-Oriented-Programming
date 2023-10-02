class Add():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def penjumlahan(self):
        return self.a + self.b
    
class Substract():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pengurangan(self):
        return self.a - self.b

class Multiply():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perkalian(self):
        return (round(self.a * self.b))
    
class Divide():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def pembagian(self):
        if self.b == 0:
            return "Tidak bisa melakukan pembagian dengan 0."
        return (round(self.a / self.b))

if __name__ == "__main__":
    add = Add(3,4)
    substract = Substract(15,4)
    multiply = Multiply(10,10)
    divide = Divide(12,3)
    
    print("Penjumlahan:", add.penjumlahan())
    print("Pengurangan:", substract.pengurangan())
    print("Perkalian:", multiply.perkalian())
    print("Pembagian:", divide.pembagian())