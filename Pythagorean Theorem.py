import math

def pythagorean_calculator(vector1, vector2):
    """
    Calculate the resultant magnitude of two perpendicular vectors.
    
    Args:
        vector1: First vector magnitude (float)
        vector2: Second vector magnitude (float)
    
    Returns:
        Resultant magnitude (float)
    """
    resultant = math.sqrt(vector1**2 + vector2**2)
    return resultant


if __name__ == "__main__":
    print("Pythagorean Theorem Calculator for Physics")
    print("-" * 40)
    
    try:
        v1 = float(input("Enter first vector magnitude: "))
        v2 = float(input("Enter second vector magnitude: "))
        
        result = pythagorean_calculator(v1, v2)
        print(f"\nResultant Speed: {result:.2f} m/s")
    
    except ValueError:
        print("Error: Please enter valid numbers")