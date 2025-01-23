import statistics, csv

# Variables
monthly_sales = {}

# Lectura de datos

with open('sales.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = float(row['sales'])
        monthly_sales[month] = sales

# Generamos lista de ventas
sales = list(monthly_sales.values())

# Calculamos la media
mean = statistics.mean(sales)

# Calculamos la mediana
median = statistics.median(sales)

# Calculamos la desviación estándar
std_dev = statistics.stdev(sales)

# Calculamos la varianza
variance = statistics.variance(sales)

# Imprimimos resultados
print(f'Media: {mean}')
print(f'Mediana: {median}')
print(f'Desviación estándar: {std_dev}')
print(f'Varianza: {variance}')
