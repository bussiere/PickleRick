import pickle

with open('Rick', 'rb') as f:
    exec(pickle.load(f))

print(rick.name)

