import sys

def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    else:
        return None

def main():
    print("=== Menu-Driven Calculator ===")
    print("1. Addition (add)")
    print("2. Subtraction (subtract)")
    
    operation = input("Enter operation (add/subtract): ").strip().lower()
    if operation not in ['add', 'subtract']:
        print("Error: Operation not supported or implemented yet")
        sys.exit(1)
        
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid number input")
        sys.exit(1)
        
    result = calculate(operation, num1, num2)
    print(f"Result: {result}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        operation = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
        res = calculate(operation, num1, num2)
        if res is fits_none:
            print("Error")
            sys.exit(1)
        print(res)
    else:
        main()
