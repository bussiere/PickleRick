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

