from dataclasses import dataclass

from .persona import Persona

class RegistroPersonas:
    def __init__(self, registros: list[tuple[str, str, str, int]]) -> None:
        self._por_dni: dict[str, Persona] = {}
        for registro in registros:
            persona = Persona.desde_tupla(registro)
            if persona.dni in self._por_dni:
                raise ValueError(f"DNI duplicado: {persona.dni}")
            self._por_dni[persona.dni] = persona

    @property
    def personas(self) -> list[Persona]:
        return list(self._por_dni.values())

    def __len__(self) -> int:
        return len(self._por_dni)
    
    def formatear(self) -> dict[str, tuple[str, str, int]]:
        return {dni: (p.nombre, p.apellido, p.edad) for dni, p in self._por_dni.items()}

    def mayor_edad(self) -> Persona:
        self._exigir_no_vacio()
        return max(self._por_dni.values(), key=lambda p: p.edad)

    def menor_edad(self) -> Persona:
        self._exigir_no_vacio()
        return min(self._por_dni.values(), key=lambda p: p.edad)

    def segmentar(self, umbral: int = 25) -> Segmentacion:
        menores = [p for p in self._por_dni.values() if p.edad < umbral]
        mayores_o_iguales = [p for p in self._por_dni.values() if p.edad >= umbral]
        return Segmentacion(umbral=umbral, menores=menores, mayores_o_iguales=mayores_o_iguales)

    def promedio_edad(self) -> float:
        self._exigir_no_vacio()
        edades = [p.edad for p in self._por_dni.values()]
        return sum(edades) / len(edades)

    def edad_por_dni(self, dni: str) -> int:
        persona = self._por_dni.get(dni)
        if persona is None:
            raise KeyError(f"No existe persona con DNI {dni}")
        return persona.edad

    def _exigir_no_vacio(self) -> None:
        if not self._por_dni:
            raise ValueError("El registro está vacío")


@dataclass(frozen=True)
class Segmentacion:
    umbral: int
    menores: list[Persona]
    mayores_o_iguales: list[Persona]