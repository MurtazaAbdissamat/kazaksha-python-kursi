x = 6
result = 10 < x > 5

# and және

result = x > 5 and x < 10 # True True = True
result = x > 4 and x < 5 # True False = False
result = x > 7 and x < 10 # False True = False
result = x > 7 and x < 6 # False False = False

# or немесе

result = x > 5 or x < 10 # True True = True
result = x > 5 or x < 4 # True False = True
result = x > 7 or x < 10 # False True = True
result = x > 7 or x < 4 # False False = False

# not емес

result = not(x < 0) # True = False
                    # False = True


print(result)