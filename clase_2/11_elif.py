# Condicionales if - elif - else
# Son estructuras de control que permiten ejecutar bloques de código
# si la evaluación de una expresión es True o False

temperatura = float(input("Ingresa temperatura en grados celsius: "))

# if temperatura > 30:
#     print("Hace mucho calor")
#     print("Tomar agua")
#     if temperatura > 20:
#         print("Hace calor")
#         if temperatura > 10:
#             print("No hace tanto calor")
#             if temperatura > 0:
#                 print("Hace frío")
#             else:
#                 print("Estás congelado")

# if temperatura > 30:
#     print("Hace mucho calor")
#     print("Tomar agua")
# else:
#     if temperatura > 20:
#         print("Hace calor")
#     else:
#         if temperatura > 10:
#             print("No hace tanto calor")
#         else:
#             if temperatura > 0:
#                 print("Hace frío")
#             else:
#                 print("Estás congelado")

if temperatura > 30:
    print("Hace mucho calor")
    print("Tomar agua")
elif temperatura > 20:
    print("Hace calor")
elif temperatura > 10:
    print("No hace tanto calor")
elif temperatura > 0:
    print("Hace frío")
else:
    print("Estás congelado")