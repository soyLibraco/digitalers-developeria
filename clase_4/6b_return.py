def subrayar(texto):
    subrayado = "=" * len(texto)
    # print(texto)
    # print(subrayado)
    # print(f"{texto}\n{subrayado}")
    return f"{texto}\n{subrayado}"

texto_subrayado = subrayar("Prueba de subrayado")
print(subrayar("Aca ahora lo hice distinto"))
print(texto_subrayado)