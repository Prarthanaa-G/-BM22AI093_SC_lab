#Mean of maximum method
def mean_of_maximum(fuzzy_set):
    # Find the maximum membership value
    max_membership = max(fuzzy_set.values())

    # Get all x values where membership is maximum
    max_x_values = [x for x, mu in fuzzy_set.items() if mu == max_membership]

    # Compute the mean of these x values
    return sum(max_x_values) / len(max_x_values)

# Example fuzzy set (dictionary format: {x: membership_value})
fuzzy_set = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0, 5: 1.0, 6: 0.7, 7: 0.3}

# Compute MOM defuzzification
result = mean_of_maximum(fuzzy_set)

# Output the result
print(f"Mean of Maximum (MOM) defuzzified value: {result}")


def center_of_gravity(fuzzy_set):
    # Compute the numerator (sum of x * μ(x))
    numerator = sum(x * mu for x, mu in fuzzy_set.items())

    # Compute the denominator (sum of μ(x))
    denominator = sum(fuzzy_set.values())

    # Avoid division by zero
    return numerator / denominator if denominator != 0 else 0

# Example fuzzy set (dictionary format: {x: membership_value})
fuzzy_set = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0, 5: 0.7}

# Compute COG defuzzification
result = center_of_gravity(fuzzy_set)

# Output the result
print(f"Center of Gravity (COG) defuzzified value: {result}")

