#10.Write a function that takes a list of integers as input and returns the product of all the elements.

def product_of_list(numbers):
    product = 1  # Initialize product as 1
    for num in numbers:
        product *= num  # Multiply each element with product
    return product

# Example usage
nums = [2, 3, 4, 5]
print("Product of list:", product_of_list(nums))  # Output: 120
