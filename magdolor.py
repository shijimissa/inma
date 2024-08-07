def my_generator():
    yield [12, 1, 0.0027616701489254743]

# Using the generator
for value in my_generator():
    print(value)
