class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        temp_a = a
        temp_b = b

        if a < 0:
            temp_a = -a
        if b < 0:
            temp_b = -b
            
        for i in range(temp_b):
            result = self.add(result, temp_a)

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = -result

        return result

    def divide(self, a, b):
        result = 0
        temp_a = a
        temp_b = b

        if b == 0:
            return "err"
        if a < 0:
            temp_a = -a
        if b < 0:
            temp_b = -b

        while temp_a >= temp_b:
            temp_a = self.subtract(temp_a, temp_b)
            result += 1

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = -result

        return result
    
    def modulo(self, a, b):
        result = 0
        temp_a = a
        temp_b = b

        if b == 0:
            return "err"
        if a < 0:
            temp_a = -a
        if b < 0:
            temp_b = -b
        
        while temp_a >= temp_b:
            temp_a = temp_a - temp_b

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            temp_a = -temp_a

        return temp_a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))