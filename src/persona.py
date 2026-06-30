from dataclasses import dataclass

@dataclass(frozen=True)
class Persona:
    dni: str
    nombre: str
    apellido: str
    edad: int


    def __post_init__(self) -> None:
        if not isinstance(self.edad, int):
            raise TypeError(f"La edad debe ser un entero, llegó {type(self.edad).__name__}")
        if self.edad < 0:
            raise ValueError(f"La edad no puede ser negativa (DNI {self.dni}): {self.edad}")
        if not self.dni:
            raise ValueError("El DNI no puede estar vacío")

    @classmethod
    def desde_tupla(cls, registro: tuple[str, str, str, int]) -> "Persona":
        dni, nombre, apellido, edad = registro
        return cls(dni=dni, nombre=nombre, apellido=apellido, edad=edad)

    def como_diccionario(self) -> dict[str, tuple[str, str, int]]:
        return {self.dni: (self.nombre, self.apellido, self.edad)}
