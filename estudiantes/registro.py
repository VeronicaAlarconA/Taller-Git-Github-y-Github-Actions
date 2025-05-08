import csv

def cargar_estudiantes_desde_csv(ruta_csv):
    estudiantes_validos = []

    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre = fila.get("Nombre")
                nota_str = fila.get("Nota")

                try:
                    nota = float(nota_str)
                    if 0.0 <= nota <= 5.0:
                        estudiantes_validos.append({
                            "nombre": nombre,
                            "nota": nota
                        })
                    else:
                        print(f"Nota fuera de rango (0.0–5.0) para {nombre}: {nota}")
                except (ValueError, TypeError):
                    print(f"Nota inválida para {nombre}: {nota_str}")

    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_csv}")

    return estudiantes_validos
