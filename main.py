"""
Simple Calculator CLI
"""
from calculator import add

def main():
    print("Calculator v1.0")
    print("Commands: add, subtract, quit")
    
    # Example usage
    result = add(5, 3)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    main()
