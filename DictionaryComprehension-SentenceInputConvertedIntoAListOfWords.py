# sentence = input()
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Built in Functions to use:
# len()
# split()

# new_dict = {new_key: new_value for (key, value) in dict.item()}
result = {word: len(word) for word in sentence.split()}
print(result)
