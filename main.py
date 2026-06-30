from src import RegistroPersonas

DATOS = [
    ("10222999", "Gonzalo", "Asencio", 24),
    ("30878298", "Pedro", "Antonio", 31),
    ("40002143", "Bruno", "Diaz", 19),
    ("50332555", "Homero", "Simpson", 47),
    ("37523987", "Sofia", "Lopez", 25),
]


def main() -> None:
    registro = RegistroPersonas(DATOS)

    print(f"Total de personas procesadas: {len(registro)}\n")

    print("Registro formateado {DNI: (nombre, apellido, edad)}:")
    for dni, datos in registro.formatear().items():
        print(f"  {dni}: {datos}")

    print(f"\nMayor edad: {registro.mayor_edad()}")
    print(f"Menor edad: {registro.menor_edad()}")
    print(f"Promedio de edad: {registro.promedio_edad():.2f}")

    seg = registro.segmentar()
    print(f"\nSegmentación (umbral {seg.umbral}):")
    print(f"  Menores de {seg.umbral}: {[p.nombre for p in seg.menores]}")
    print(f"  {seg.umbral} o más:      {[p.nombre for p in seg.mayores_o_iguales]}")

    print(f"\nEdad del DNI 10222999: {registro.edad_por_dni('10222999')}")


if __name__ == "__main__":
    main()
