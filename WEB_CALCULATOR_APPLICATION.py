
def sum_numbers(x, y): 
    return x + y

def difference(x, y):
    return x - y

def product(x, y):
    return x * y

def quotient(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Example usage
print("Sum:", sum_numbers(5, 9))
print("Difference:", difference(3, 3))
print("Product:", product(7, 2))
print("Quotient:", quotient(10, 5))