#TASK1
# L=list(map(int,input().split()))
# e=[]
# o=[]
# for i in L:
#   if i%2==0:
#     e.append(i)
#   else:
#     o.append(i)
# print("Even numbers : ",sum(e))
# print("Odd numbers : ",sum(o))
#AI
# # def calculate_even_odd_sums(numbers):
#   even_sum = sum(num for num in numbers if num % 2 == 0)
#   odd_sum = sum(num for num in numbers if num % 2 != 0)
#   return even_sum, odd_sum

# L = list(map(int, input().split()))
# even_sum, odd_sum = calculate_even_odd_sums(L)

# print("Even numbers : ", even_sum)
# print("Odd numbers : ", odd_sum)
#TASK2
# import math

# def calculate_area(shape, **kwargs):
#     """
#     Calculates the area of different shapes.

#     Args:
#         shape (str): The type of shape ('circle', 'rectangle', 'triangle').
#         **kwargs: Keyword arguments specific to each shape:
#             - For 'circle': radius (float)
#             - For 'rectangle': length (float), width (float)
#             - For 'triangle': base (float), height (float)

#     Returns:
#         float: The calculated area of the shape.
#         str: An error message if the shape is not recognized or arguments are missing.
#     """
#     if shape.lower() == 'circle':
#         if 'radius' in kwargs:
#             radius = kwargs['radius']
#             return math.pi * (radius ** 2)
#         else:
#             return "Error: Missing 'radius' argument for circle."
#     elif shape.lower() == 'rectangle':
#         if 'length' in kwargs and 'width' in kwargs:
#             length = kwargs['length']
#             width = kwargs['width']
#             return length * width
#         else:
#             return "Error: Missing 'length' or 'width' argument for rectangle."
#     elif shape.lower() == 'triangle':
#         if 'base' in kwargs and 'height' in kwargs:
#             base = kwargs['base']
#             height = kwargs['height']
#             return 0.5 * base * height
#         else:
#             return "Error: Missing 'base' or 'height' argument for triangle."
#     else:
#         return "Error: Unknown shape type."

# # Examples of using the function
# circle_area = calculate_area('circle', radius=5)
# print(f"Area of circle with radius 5: {circle_area:.2f}")

# rectangle_area = calculate_area('rectangle', length=10, width=4)
# print(f"Area of rectangle with length 10 and width 4: {rectangle_area}")

# triangle_area = calculate_area('triangle', base=6, height=8)
# print(f"Area of triangle with base 6 and height 8: {triangle_area}")

# # Example with missing arguments
# error_message_circle = calculate_area('circle', length=5)
# print(error_message_circle)

# # Example with unknown shape
# error_message_unknown = calculate_area('hexagon', side=5)
# print(error_message_unknown)
#TASK3
# """
# Function to calculate the area of different shapes
# """

# def calculate_area(shape, **kwargs):
#     """
#     Calculate the area of different geometric shapes.
    
#     Parameters:
#     -----------
#     shape : str
#         The type of shape ('circle', 'rectangle', 'triangle', 'square', 'trapezoid')
#     **kwargs : dict
#         Shape-specific parameters:
#         - For circle: 'radius' (required)
#         - For rectangle: 'length' and 'width' (both required)
#         - For triangle: 'base' and 'height' (both required)
#         - For square: 'side' (required)
#         - For trapezoid: 'base1', 'base2', and 'height' (all required)
    
#     Returns:
#     --------
#     float
#         The calculated area of the shape
    
#     Raises:
#     -------
#     ValueError
#         If shape is not recognized or required parameters are missing
#     """
    
#     shape = shape.lower()  # Convert to lowercase for case-insensitive matching
    
#     if shape == 'circle':
#         # Area of circle: π * r²
#         if 'radius' not in kwargs:
#             raise ValueError("Circle requires 'radius' parameter")
#         radius = kwargs['radius']
#         if radius < 0:
#             raise ValueError("Radius cannot be negative")
#         return 3.14159 * radius ** 2
    
#     elif shape == 'rectangle':
#         # Area of rectangle: length * width
#         if 'length' not in kwargs or 'width' not in kwargs:
#             raise ValueError("Rectangle requires both 'length' and 'width' parameters")
#         length = kwargs['length']
#         width = kwargs['width']
#         if length < 0 or width < 0:
#             raise ValueError("Length and width cannot be negative")
#         return length * width
    
#     elif shape == 'triangle':
#         # Area of triangle: (base * height) / 2
#         if 'base' not in kwargs or 'height' not in kwargs:
#             raise ValueError("Triangle requires both 'base' and 'height' parameters")
#         base = kwargs['base']
#         height = kwargs['height']
#         if base < 0 or height < 0:
#             raise ValueError("Base and height cannot be negative")
#         return 0.5 * base * height
    
#     elif shape == 'square':
#         # Area of square: side²
#         if 'side' not in kwargs:
#             raise ValueError("Square requires 'side' parameter")
#         side = kwargs['side']
#         if side < 0:
#             raise ValueError("Side cannot be negative")
#         return side ** 2
    
#     elif shape == 'trapezoid':
#         # Area of trapezoid: ((base1 + base2) / 2) * height
#         if 'base1' not in kwargs or 'base2' not in kwargs or 'height' not in kwargs:
#             raise ValueError("Trapezoid requires 'base1', 'base2', and 'height' parameters")
#         base1 = kwargs['base1']
#         base2 = kwargs['base2']
#         height = kwargs['height']
#         if base1 < 0 or base2 < 0 or height < 0:
#             raise ValueError("Bases and height cannot be negative")
#         return 0.5 * (base1 + base2) * height
    
#     else:
#         raise ValueError(f"Unsupported shape: {shape}. Supported shapes: circle, rectangle, triangle, square, trapezoid")


# # Example usage and demonstration
# if __name__ == "__main__":
#     print("Area Calculator Examples:")
#     print("=" * 50)
    
#     # Circle example
#     circle_area = calculate_area('circle', radius=5)
#     print(f"Circle (radius=5): {circle_area:.2f} square units")
    
#     # Rectangle example
#     rect_area = calculate_area('rectangle', length=10, width=6)
#     print(f"Rectangle (length=10, width=6): {rect_area:.2f} square units")
    
#     # Triangle example
#     triangle_area = calculate_area('triangle', base=8, height=5)
#     print(f"Triangle (base=8, height=5): {triangle_area:.2f} square units")
    
#     # Square example
#     square_area = calculate_area('square', side=7)
#     print(f"Square (side=7): {square_area:.2f} square units")
    
#     # Trapezoid example
#     trapezoid_area = calculate_area('trapezoid', base1=6, base2=10, height=4)
#     print(f"Trapezoid (base1=6, base2=10, height=4): {trapezoid_area:.2f} square units")

