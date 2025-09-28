class Fraction:
    #constructor Method
    def __init__(self, n, d):
        self.num=n
        self.den=d
    
    #Magic Method called automatically    
    def __str__(self):
        return f"{self.num} / {self.den}"
    
    

x= Fraction(3,5)
print(x)