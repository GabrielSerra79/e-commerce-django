def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')

def cart_qtd_total(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])
