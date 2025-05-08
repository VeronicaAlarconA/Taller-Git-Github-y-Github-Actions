from estudiantes.registro import cargar_estudiantes_desde_csv, mostrar_estudiantes_en_tabla, calcular_promedio_general

def main():
    estudiantes = cargar_estudiantes_desde_csv("estudiantes.csv")
    
    if estudiantes:
        mostrar_estudiantes_en_tabla(estudiantes)
        
        calcular_promedio_general(estudiantes)
    else:
        print("No se encontraron estudiantes válidos.")

if __name__ == "__main__":
    main()
