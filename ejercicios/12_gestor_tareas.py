"""Ejercicio 12: pequeño gestor de tareas en memoria."""
tareas = []
while True:
    print("\n--- Gestor de tareas ---")
    print("1. Añadir tarea\n2. Ver tareas\n3. Completar tarea\n4. Salir")
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        texto = input("Describe la tarea: ").strip()
        if texto:
            tareas.append({"texto": texto, "hecha": False})
            print("Tarea añadida.")
        else:
            print("La tarea no puede estar vacía.")
    elif opcion == "2":
        if not tareas:
            print("Todavía no hay tareas.")
        for indice, tarea in enumerate(tareas, start=1):
            estado = "✓" if tarea["hecha"] else " "
            print(f"{indice}. [{estado}] {tarea['texto']}")
    elif opcion == "3":
        try:
            indice = int(input("Número de tarea completada: ")) - 1
            if 0 <= indice < len(tareas):
                tareas[indice]["hecha"] = True
                print("Tarea marcada como completada.")
            else:
                print("Ese número de tarea no existe.")
        except ValueError:
            print("Introduce un número válido.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Elige del 1 al 4.")
