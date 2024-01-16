# Concatenar cadenas de carateres.
# Supongamos que queremos crar una cadena que diga:
# Aprende a programar con ________.

# organización = 'FreeCodeCamp'

# print('Aprende a programar con ' + organización)
# print(f'Aprende a programar con {organización}') #f-string

# Mad Libs (Historias Locas)


adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")


madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"


print(madlib)