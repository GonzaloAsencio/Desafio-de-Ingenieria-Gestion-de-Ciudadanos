import dataclasses

import pytest

from src import Persona


def test_construccion_valida():
    p = Persona("10222999", "Gonzalo", "Asencio", 24)
    assert p.dni == "10222999"
    assert p.edad == 24


def test_es_inmutable():
    p = Persona("10222999", "Gonzalo", "Asencio", 24)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.edad = 99


def test_edad_negativa_falla():
    with pytest.raises(ValueError):
        Persona("10222999", "Gonzalo", "Asencio", -1)


def test_dni_vacio_falla():
    with pytest.raises(ValueError):
        Persona("", "Gonzalo", "Asencio", 24)


def test_desde_tupla():
    p = Persona.desde_tupla(("10222999", "Gonzalo", "Asencio", 24))
    assert p == Persona("10222999", "Gonzalo", "Asencio", 24)


def test_como_diccionario():
    p = Persona("10222999", "Gonzalo", "Asencio", 24)
    assert p.como_diccionario() == {"10222999": ("Gonzalo", "Asencio", 24)}
