# Gestión de Ciudadanos

Sistema que procesa un lote crudo de datos de ciudadanos (tuplas de Python
provenientes de un sistema legacy), los limpia, los estructura y expone
métricas para un reporte administrativo.

## Estructura

```
gestion-ciudadanos/
├── src/
│   ├── persona.py            # Modelo de dominio inmutable (Persona)
│   └── registro_personas.py  # Procesamiento y consultas (RegistroPersonas)
├── tests/                    # Pruebas con pytest
├── main.py                   # Demostración ejecutable
└── README.md
```

## Decisiones de diseño

- **`Persona` es inmutable** (`@dataclass(frozen=True)`): un objeto de valor.
  Valida sus propias invariantes al construirse (edad no negativa, DNI no vacío).
- **La unicidad de DNI vive en `RegistroPersonas`**, no en `Persona`: es una
  regla del conjunto, no del individuo.
- **Índice interno `{dni: Persona}`**: detecta duplicados al construir y da
  acceso **O(1)** por DNI (requisito de "acceso eficiente").

## Requisitos

- Python 3.10+ (usa type hints modernos como `list[...]`)
- `pytest` para correr las pruebas

## Cómo ejecutar el script

```bash
python main.py
```

## Cómo correr las pruebas

```bash
pip install pytest
python -m pytest
```
