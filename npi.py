from collections import deque

# On s'assure que toutes les données sont bien au format string afin qu'elle puisse être prise en compte par le programme
# vals = deque(map(str, ["5", 2, "+", 8, "*"]))

# Objet permettant d'effectuer les opérations en fonction d'un symbole
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

def npi_calculator(data: list) -> int:
    data = deque(map(str, data))
    # On s'assure que les deux premiers éléments de la liste sont bien des entiers
    if not data[0].isdigit() or not data[1].isdigit():
        raise ValueError('Liste invalide.')
    d = deque()
    for x in data:
        if x.isdigit() :
            d.append(int(x))
        elif not x.isdigit() :
            b, a = d.pop(), d.pop()
            d.append(op[x](a,b))
        else:
            raise ValueError("Cette valeur ne peut être prise en compte")
    # On pop une dernière fois afin d'avoir un entier et non une pile
    return d.pop()

# print('final d :', npi_calculator(vals))