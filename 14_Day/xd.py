from countries_data import countries

# Ordenar países por nombre
countries_sorted_by_name = sorted(countries, key=lambda x: x['name'])

# Ordenar países por capital
countries_sorted_by_capital = sorted(countries, key=lambda x: x.get('capital', ''))

# Ordenar países por población (de mayor a menor)
countries_sorted_by_population = sorted(countries, key=lambda x: x['population'], reverse=True)

# Obtener los diez países más poblados
top_10_most_populated = countries_sorted_by_population[:10]

# Contar la cantidad de países donde se habla cada idioma
from collections import defaultdict

language_count = defaultdict(int)
for country in countries:
    for language in country.get('languages', []):
        language_count[language] += 1

# Obtener los diez idiomas más hablados
most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

# Imprimir resultados
print("Países ordenados por nombre:", [country['name'] for country in countries_sorted_by_name])
print("\nPaíses ordenados por capital:", [country['name'] for country in countries_sorted_by_capital])
print("\nPaíses ordenados por población:", [(country['name'], country['population']) for country in countries_sorted_by_population])
print("\nDiez países más poblados:", [(country['name'], country['population']) for country in top_10_most_populated])
print("\nDiez idiomas más hablados por ubicación:", most_spoken_languages)