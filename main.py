"""
Simple Calculator CLI
"""
from calculator import subtract

def main():
    print("Calculator v1.0")
    print("Commands: add, subtract, quit")
    
    # Example usage
    result = subtract(10, 4)
    print(f"10 - 4 = {result}")

if __name__ == "__main__":
    main()
