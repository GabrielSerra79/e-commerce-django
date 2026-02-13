def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')

def cart_qtd_total(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_totals(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in carrinho.values()
        ]
    )

if __name__ == '__main__':
    carrinho = {'6': {'produto_id': 2, 'produto_nome': 'Celular Samsung Galaxy A16', 'variacao_nome': '128 GB', 'variacao_id': '6', 'preco_unitario': 1099.0, 'preco_unitario_promocional': 794.35, 'preco_quantitativo': 1099.0, 'preco_quantitativo_promocional': 794.35, 'quantidade': 1, 'slug': 'celular-samsung-galaxy-a16', 'imagem': '/media/produto_imagens/2026/02/7eb9d706-b8e3-48d0-957e-25f4a722f944.jpg'}, '12': {'produto_id': 6, 'produto_nome': 'O Rei Leão: Contos para Brincar, de Disney', 'variacao_nome': 'Kids', 'variacao_id': '12', 'preco_unitario': 89.0, 'preco_unitario_promocional': 51.72, 'preco_quantitativo': 267.0, 'preco_quantitativo_promocional': 155.16, 'quantidade': 3, 'slug': 'o-rei-leao-contos-para-brincar-de-disney', 'imagem': '/media/produto_imagens/2026/02/fQnjSbW.jpg'}, '13': {'produto_id': 6, 'produto_nome': 'O Rei Leão: Contos para Brincar, de Disney', 'variacao_nome': 'Capa Dura', 'variacao_id': '13', 'preco_unitario': 100.0, 'preco_unitario_promocional': 92.0, 'preco_quantitativo': 100.0, 'preco_quantitativo_promocional': 92.0, 'quantidade': 1, 'slug': 'o-rei-leao-contos-para-brincar-de-disney', 'imagem': '/media/produto_imagens/2026/02/fQnjSbW.jpg'}, '20': {'produto_id': 8, 'produto_nome': 'Windows 11 Pro Físico - Microsoft - Edição 11 Pro', 'variacao_nome': '', 'variacao_id': '20', 'preco_unitario': 1599.0, 'preco_unitario_promocional': 859.33, 'preco_quantitativo': 1599.0, 'preco_quantitativo_promocional': 859.33, 'quantidade': 1, 'slug': 'windows-11-pro-fisico-microsoft-edicao-11-pro', 'imagem': '/media/produto_imagens/2026/02/windows_field_grass_operating_system_74340_1280x720.jpg'}, '14': {'produto_id': 6, 'produto_nome': 'O Rei Leão: Contos para Brincar, de Disney', 'variacao_nome': 'Box Premium', 'variacao_id': '14', 'preco_unitario': 320.0, 'preco_unitario_promocional': 250.0, 'preco_quantitativo': 320.0, 'preco_quantitativo_promocional': 250.0, 'quantidade': 1, 'slug': 'o-rei-leao-contos-para-brincar-de-disney', 'imagem': '/media/produto_imagens/2026/02/fQnjSbW.jpg'}, '1': {'produto_id': 1, 'produto_nome': 'Camiseta Divertida Many Problems', 'variacao_nome': 'P', 'variacao_id': '1', 'preco_unitario': 39.9, 'preco_unitario_promocional': 0.0, 'preco_quantitativo': 39.9, 'preco_quantitativo_promocional': 0.0, 'quantidade': 1, 'slug': 'camiseta-divertida-many-problems', 'imagem': '/media/produto_imagens/2026/02/camiseta-supernatural-nova-01.jpg'}}
    print("Cart totals = ", cart_totals(carrinho))
