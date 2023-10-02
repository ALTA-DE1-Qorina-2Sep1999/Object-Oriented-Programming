import math
class Square():
    def __init__(self, sisi):
        self.sisi = sisi
    
    def calculate_area(self):
        return (round(self.sisi * self.sisi))
    
    def calculate_perimeter(self):
        return (round(4 * self.sisi))
    
class Triangle():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def calculate_area(self):
        return (round(self.alas * self.tinggi / 2))
    
    def calculate_perimeter(self):
        miring = math.sqrt(self.alas ** 2 + self.tinggi ** 2)
        return (round(self.alas + self.tinggi + miring))
    
class Rectangle():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def calculate_area(self):
        return (round(self.panjang * self.lebar))
    
    def calculate_perimeter(self):
        return (round((2 * self.panjang) + (2 * self.lebar)))
    
if __name__ == "__main__":
    square = Square(4)
    triangle = Triangle(3, 4)
    rectangle = Rectangle(7, 8)
    
    print("Luas")
    print("Persegi:", square.calculate_area())
    print("Segitiga:", triangle.calculate_area())
    print("Rectangle:", rectangle.calculate_area())
    
    print("Keliling")
    print("Persegi:", square.calculate_perimeter())
    print("Segitiga:", triangle.calculate_perimeter())
    print("Rectangle:", rectangle.calculate_perimeter())