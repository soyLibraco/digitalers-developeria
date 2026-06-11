# Orden de precedencia de operadores.

# Orden de precedencia de operadores


# 1. Paréntesis
# 2. Operaciones aritméticas
#    a) Paréntesis
#    b) Potencias y raíces
#    c) Multiplicaciones o divisiones
#    d) Sumas y restas
# 3. Operaciones de comparación
# 4. Operaciones lógicas
#    a) not
#    b) or, and

ejemplo = 2**3 > 4 or 3 == 3 and 20 > 3 + 1 * 2
        #    8 > 4 or 3 == 3 and 20 > 3 + 1 * 2
        #    8 > 4 or 3 == 3 and 20 > 3 + 2
        #    8 > 4 or 3 == 3 and 20 > 5
        #    True  or True   and True
        #             True   and True
        #                        True



print(ejemplo)