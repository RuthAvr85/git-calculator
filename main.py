"""
Simple Calculator CLI
"""
from calculator import add, subtract

def main():
    print("Calculator v1.0")
    print("Commands: add, subtract, quit")
    
    # Example usage
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")

if __name__ == "__main__":
    main()
