import pytest

from src import RegistroPersonas

DATOS = [
    ("10222999", "Gonzalo", "Asencio", 24),
    ("30878298", "Pedro", "Antonio", 31),
    ("40002143", "Bruno", "Diaz", 19),
    ("50332555", "Homero", "Simpson", 47),
]


def test_dni_duplicado_falla():
    datos = DATOS + [("10222999", "Otro", "Repetido", 50)]
    with pytest.raises(ValueError):
        RegistroPersonas(datos)


def test_formatear():
    registro = RegistroPersonas(DATOS)
    formato = registro.formatear()
    assert formato["10222999"] == ("Gonzalo", "Asencio", 24)


def test_mayor_edad():
    registro = RegistroPersonas(DATOS)
    assert registro.mayor_edad().nombre == "Homero"


def test_menor_edad():
    registro = RegistroPersonas(DATOS)
    assert registro.menor_edad().nombre == "Bruno"


def test_promedio_edad():
    registro = RegistroPersonas(DATOS)
    assert registro.promedio_edad() == (24 + 31 + 19 + 47) / 4


def test_segmentacion_default():
    registro = RegistroPersonas(DATOS)
    seg = registro.segmentar()
    assert seg.umbral == 25
    assert {p.nombre for p in seg.menores} == {"Gonzalo", "Bruno"}
    assert {p.nombre for p in seg.mayores_o_iguales} == {"Pedro", "Homero"}


def test_segmentacion_umbral_custom():
    registro = RegistroPersonas(DATOS)
    seg = registro.segmentar(umbral=20)
    assert {p.nombre for p in seg.menores} == {"Bruno"}


def test_edad_por_dni():
    registro = RegistroPersonas(DATOS)
    assert registro.edad_por_dni("30878298") == 31


def test_edad_por_dni_inexistente():
    registro = RegistroPersonas(DATOS)
    with pytest.raises(KeyError):
        registro.edad_por_dni("00000000")


def test_registro_vacio_promedio_falla():
    registro = RegistroPersonas([])
    with pytest.raises(ValueError):
        registro.promedio_edad()
