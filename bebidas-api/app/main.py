bebidas = []

def adicionar_bebida(nome, tipo, preco, quantidade):
    bebida = {"nome": nome, "tipo": tipo, "preco": preco, "quantidade": quantidade}
    bebidas.append(bebida)

def listar_bebidas():
    return bebidas

def filtrar_por_tipo(tipo):
    return [b for b in bebidas if b["tipo"].lower() == tipo.lower()]

def ordenar_por_preco(desc=False):
    return sorted(bebidas, key=lambda b: b["preco"], reverse=desc)

# Teste rápido:
if __name__ == "__main__":
    adicionar_bebida("Heineken", "Cerveja", 6.5, 10)
    adicionar_bebida("Coca-Cola", "Refrigerante", 5.0, 15)
    print(listar_bebidas())
    print(filtrar_por_tipo("Cerveja"))
    print(ordenar_por_preco())



