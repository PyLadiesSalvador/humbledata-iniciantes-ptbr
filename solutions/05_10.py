df = df.reset_index()
df.index

# Também poderíamos ter feito o seguinte ao concatenar:
# df = pd.concat(frames, ignore_index=True)