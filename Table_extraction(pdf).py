import camelot

tables = camelot.read_pdf('Nombre_archivo.pdf', pages = 1)
print(tables)

format.export("Nombre_archivo.csv", format = "csv", compress = True)
tables[0].to_csv("Nombre_archivo.csv")