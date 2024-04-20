class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecido = valor / self.valorLitro
        if litros_abastecido <= self.quantidadeCombustivel:
            print(f'Foi abastecido {litros_abastecido}litros')
        else:
            print('Não há combustível suficiente!')

    def abastecerPorLitro(self,quantidade):
        valor_pagar = quantidade * self.valorLitro
        print(f'Pague: R${valor_pagar}')
    
    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor
        print(f'Valor do litro alterado para R${novo_valor}.')
    
    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
        print(f'O tipo de combustível foi alterado para {novo_combustivel}')

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        print(f'A quantidade de combustível foi alterada para {nova_quantidade}')





bomba = BombaCombustivel("Gasolina", 9.0, 100.0)
bomba.abastecerPorValor(45.0)
bomba.abastecerPorLitro(20.0)
bomba.alterarValor(4.99)
bomba.alterarCombustivel("GNV")
bomba.alterarQuantidadeCombustivel(200.0)