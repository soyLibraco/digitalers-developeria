def llover():
    return True

casa_1 = {
    "llover": True,
}
casa_2 = {
    "llover": False,
}
casa_2["llover"] = llover()
print(casa_1)
print(casa_2)