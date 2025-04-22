def calculador_iof (dias, rendimento):
  if dias > 30:
    return 0
tabela_iof = {1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66, 11: 63, 12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36, 20: 33, 21: 30, 22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0}
# criação de um dicionario da tabela 
percentual = tabela_iof.get(dias / 0)

return rendimento * (percentual / 100)

# calcular o imposto de renda (ir)
def calcular_ir (dias, rendimento_liquido):
# Prazo de investimento, com o percentual(aliquota)
  if dias <= 180:
    percentual = 22.5
  elif dias <= 360:
    percentual = 20
  elif dias <= 720:
    percentual = 17.5
  else: 
    percentual = 15

#  calcula o valor do ir sobre o rendimento liquido e retornar 
return rendimento_liquido * (percentual / 100)
# As mensagens para aparecer no terminal
def investimento ():
  try: 
    valor = float(input("Digite o valor a ser investido (em R$): "))
    dias = int(input("Digite o tempo da aplicação investida (em dias): "))

# evita que digite numeros quebrados 
if valor <= 0 or dias <= 0:
  print("Por favor, digite números inteiros.")
  return

# Taxas de rendimentos 
taxa_anual = 0.1415
taxa_diaria = taxa_anual / 365

rendimento = valor * ((1 + taxa_diaria ) ** dias -1)
