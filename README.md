

```python
#first we pickle Rick 
import pickle

rick = """
class Rick:  # Définition de notre classe Personne
    def __init__(self):  # Notre méthode constructeur
        print("Pickle Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiick")
        self.name = "Sanchez"
rick = Rick()
"""
with open('Rick', 'wb') as f:
    pickle.dump(rick,f)
```


```python
#then we load him with pickle and cheat with exec :
import pickle

with open('Rick', 'rb') as f:
    exec(pickle.load(f))

print(rick.name)
```

    Pickle Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiick
    Sanchez


#so we have a pickle Rick now ...
#source here

https://github.com/bussiere/PickleRick


```python

```
