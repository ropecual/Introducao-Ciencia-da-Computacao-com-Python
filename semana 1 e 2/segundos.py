# A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

a = entrada // (24*3600)
dias_resto = entrada % (24*3600)
b = dias_resto // 3600
horas_resto = entrada % 3600
c = horas_resto // 60
d = horas_resto % 60


print(a,"dias,",b,"horas",c,"minutos e",d,"segundos.")
