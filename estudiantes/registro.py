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

def mostrar_estudiantes_en_tabla(estudiantes):
    """
    Ordena la lista de estudiantes alfabéticamente por nombre
    y los muestra en una tabla alineada.
    """
    estudiantes_ordenados = sorted(estudiantes, key=lambda est: est["nombre"])

    print("\nListado de Estudiantes".center(40, "-"))
    print(f"{'Nombre':<25} {'Nota':>5}")
    print("-" * 40)

    for est in estudiantes_ordenados:
        print(f"{est['nombre']:<25} {est['nota']:>5.1f}")

    print("-" * 40)

