def test2var():
    a = 5
    b = 3
    return a, b

#print(type(test2var()))
temp = test2var()
#print(temp[0])

# Conclusion : quand on renvoie plusieurs éléments, on renvoie un tuple de ces éléments


# Afficher les informations d'un dictionnaire
equipe1 = {"a":1, "b":2}

# Ajouter des éléments dans un dictionnaire
equipe1["c"]=3
equipe1["d"]=4

# Supprimer des éléments dans un dictionnaire
del equipe1["d"]

# Clés (Keys)
for key in equipe1.keys():
    print(key)

# Valeurs (Values)
for value in equipe1.values():
    print(value)

# Items
for key, value in equipe1.items():
    print(key,":",value)