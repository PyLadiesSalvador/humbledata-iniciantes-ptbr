df = df.drop("Country", axis=1)

# Obs.: você só pode executar esta célula uma vez! Se tentar executá-la novamente, ocorrerá um erro!
#       Por quê? Porque, se a coluna Country for removida, ela não estará mais no dataframe...
#       então não dá para removê-la uma segunda vez, já que a coluna não está mais lá!