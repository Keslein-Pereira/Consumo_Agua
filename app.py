# Sistema de classificação de consumo de água
# Agenda 7 - Desenvolvimento de Sistemas I

# Entrada de dados
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").lower()
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classificação do consumo
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")  