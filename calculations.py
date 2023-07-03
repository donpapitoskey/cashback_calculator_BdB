import numpy as np

bills = {
    "Juan Valdez": 45000,
    "Ristorante": 25000,
    "los_libros": 23000
}
charges = np.array(list(bills.values()))

cashback = 3500 # aqui pones el valor del cahsback 

numero_de_iteraciones = 2**charges.size

def get_matching_charges(item):
    print(item)
    return item[1] in matching_charges
    

for i in range(numero_de_iteraciones):
    vector_of_combination = ((i & (2**np.arange(charges.size))) != 0).astype(int)
    posible_cashback = np.inner(charges,vector_of_combination)*0.05
    if(posible_cashback == cashback):
        matching_charges = np.multiply(vector_of_combination, charges)

        filtered_charges = dict(filter(get_matching_charges, bills.items()))
        print(f"Los cargos efectuados en su EconoMia son: {filtered_charges}")
