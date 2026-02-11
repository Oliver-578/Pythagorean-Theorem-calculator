import math


class PythagoreanCalculator:
    """Advanced Pythagorean theorem calculator for physics and geometry."""
    
    def __init__(self):
        self.history = []
    
    @staticmethod
    def validate_input(value, name):
        """
        Validate and convert input to float.
        
        Args:
            value: Input value to validate
            name: Name of the input for error messages
        
        Returns:
            Float value if valid
        
        Raises:
            ValueError: If input is invalid or negative
        """
        try:
            num = float(value)
            if num < 0:
                raise ValueError(f"{name} cannot be negative")
            if num == 0:
                raise ValueError(f"{name} cannot be zero")
            return num
        except ValueError as e:
            raise ValueError(f"Invalid input for {name}: {e}")
    
    def find_resultant(self, vector1, vector2):
        """
        Calculate resultant magnitude of two perpendicular vectors.
        
        Args:
            vector1: First vector magnitude (float)
            vector2: Second vector magnitude (float)
        
        Returns:
            Resultant magnitude (float)
        """
        resultant = math.sqrt(vector1**2 + vector2**2)
        return resultant
    
    def find_side_a(self, hypotenuse, side_b):
        """Calculate side A given hypotenuse and side B."""
        if side_b >= hypotenuse:
            raise ValueError("Side B must be less than hypotenuse")
        return math.sqrt(hypotenuse**2 - side_b**2)
    
    def find_side_b(self, hypotenuse, side_a):
        """Calculate side B given hypotenuse and side A."""
        if side_a >= hypotenuse:
            raise ValueError("Side A must be less than hypotenuse")
        return math.sqrt(hypotenuse**2 - side_a**2)
    
    def calculate_angle(self, opposite, adjacent):
        """Calculate angle in degrees given opposite and adjacent sides."""
        angle_rad = math.atan(opposite / adjacent)
        return math.degrees(angle_rad)
    
    def calculate_perimeter(self, side_a, side_b):
        """Calculate perimeter of a right triangle."""
        hypotenuse = self.find_resultant(side_a, side_b)
        return side_a + side_b + hypotenuse
    
    def calculate_area(self, side_a, side_b):
        """Calculate area of a right triangle."""
        return 0.5 * side_a * side_b
    
    def add_to_history(self, operation, inputs, result):
        """Store calculation in history."""
        self.history.append({
            'operation': operation,
            'inputs': inputs,
            'result': result
        })
    
    def display_history(self):
        """Display all previous calculations."""
        if not self.history:
            print("\nNo calculations in history.")
            return
        
        print("\n" + "=" * 50)
        print("CALCULATION HISTORY")
        print("=" * 50)
        for i, calc in enumerate(self.history, 1):
            print(f"\n{i}. {calc['operation']}")
            print(f"   Inputs: {calc['inputs']}")
            print(f"   Result: {calc['result']:.4f}")


def display_menu():
    """Display main menu options."""
    print("\n" + "=" * 50)
    print("PYTHAGOREAN THEOREM CALCULATOR")
    print("=" * 50)
    print("1. Find Resultant (given two sides)")
    print("2. Find Side A (given hypotenuse and side B)")
    print("3. Find Side B (given hypotenuse and side A)")
    print("4. Calculate Angle (in degrees)")
    print("5. Calculate Perimeter")
    print("6. Calculate Area")
    print("7. View History")
    print("8. Exit")
    print("-" * 50)


def main():
    """Main application loop."""
    calculator = PythagoreanCalculator()
    
    print("\nWelcome to the Advanced Pythagorean Theorem Calculator!")
    
    while True:
        display_menu()
        choice = input("Select an option (1-8): ").strip()
        
        try:
            if choice == '1':
                v1 = calculator.validate_input(
                    input("Enter first vector/side magnitude: "),
                    "Vector 1"
                )
                v2 = calculator.validate_input(
                    input("Enter second vector/side magnitude: "),
                    "Vector 2"
                )
                result = calculator.find_resultant(v1, v2)
                print(f"\n✓ Resultant: {result:.4f}")
                calculator.add_to_history("Find Resultant", f"({v1}, {v2})", result)
            
            elif choice == '2':
                h = calculator.validate_input(input("Enter hypotenuse: "), "Hypotenuse")
                b = calculator.validate_input(input("Enter side B: "), "Side B")
                result = calculator.find_side_a(h, b)
                print(f"\n✓ Side A: {result:.4f}")
                calculator.add_to_history("Find Side A", f"(h={h}, b={b})", result)
            
            elif choice == '3':
                h = calculator.validate_input(input("Enter hypotenuse: "), "Hypotenuse")
                a = calculator.validate_input(input("Enter side A: "), "Side A")
                result = calculator.find_side_b(h, a)
                print(f"\n✓ Side B: {result:.4f}")
                calculator.add_to_history("Find Side B", f"(h={h}, a={a})", result)
            
            elif choice == '4':
                opp = calculator.validate_input(
                    input("Enter opposite side: "),
                    "Opposite"
                )
                adj = calculator.validate_input(
                    input("Enter adjacent side: "),
                    "Adjacent"
                )
                result = calculator.calculate_angle(opp, adj)
                print(f"\n✓ Angle: {result:.2f}°")
                calculator.add_to_history("Calculate Angle", f"(opp={opp}, adj={adj})", result)
            
            elif choice == '5':
                a = calculator.validate_input(input("Enter side A: "), "Side A")
                b = calculator.validate_input(input("Enter side B: "), "Side B")
                result = calculator.calculate_perimeter(a, b)
                hyp = calculator.find_resultant(a, b)
                print(f"\n✓ Perimeter: {result:.4f}")
                print(f"  (Sides: {a:.4f} + {b:.4f} + {hyp:.4f})")
                calculator.add_to_history("Calculate Perimeter", f"({a}, {b})", result)
            
            elif choice == '6':
                a = calculator.validate_input(input("Enter side A: "), "Side A")
                b = calculator.validate_input(input("Enter side B: "), "Side B")
                result = calculator.calculate_area(a, b)
                print(f"\n✓ Area: {result:.4f} square units")
                calculator.add_to_history("Calculate Area", f"({a}, {b})", result)
            
            elif choice == '7':
                calculator.display_history()
            
            elif choice == '8':
                print("\nThank you for using the Pythagorean Theorem Calculator!")
                break
            
            else:
                print("Invalid option. Please select 1-8.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero. Please check your inputs.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()