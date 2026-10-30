import pytest

from insurance_manager import InsuranceManager
from insured_person import InsuredPerson


@pytest.fixture
def manager():
    """Čistý manažér pre každý test, testy sa navzájom neovplyvňujú."""
    return InsuranceManager()


@pytest.fixture
def anna():
    return InsuredPerson("Anna", "Šťastná", "30", "123456789")


@pytest.fixture
def vojtech():
    return InsuredPerson("Vojtech", "Veselý", "40", "987654321")


# ---------- Pridanie a zobrazenie ----------

def test_new_manager_has_no_insured_people(manager):
    assert manager.get_insured_people() == []


def test_add_insured_person(manager, anna):
    manager.add_insured_person(anna)

    assert manager.get_insured_people() == [anna]


def test_add_multiple_people_keeps_order(manager, anna, vojtech):
    manager.add_insured_person(anna)
    manager.add_insured_person(vojtech)

    assert manager.get_insured_people() == [anna, vojtech]


# ---------- Vyhľadávanie ----------

def test_find_existing_person(manager, anna, vojtech):
    manager.add_insured_person(anna)
    manager.add_insured_person(vojtech)

    assert manager.find_insured_person("Vojtech", "Veselý") == [vojtech]


def test_find_is_case_insensitive(manager, anna):
    manager.add_insured_person(anna)

    assert manager.find_insured_person("anna", "ŠŤASTNÁ") == [anna]


def test_find_returns_empty_list_when_not_found(manager, anna):
    manager.add_insured_person(anna)

    assert manager.find_insured_person("Eva", "Horváthová") == []


def test_find_in_empty_registry_returns_empty_list(manager):
    assert manager.find_insured_person("Anna", "Šťastná") == []


def test_find_requires_both_first_and_last_name_to_match(manager, anna):
    manager.add_insured_person(anna)

    assert manager.find_insured_person("Anna", "Šťast") == []
    assert manager.find_insured_person("Vojtech", "Veselá") == []


def test_find_returns_all_people_with_same_name(manager):
    first = InsuredPerson("Anna", "Šťastná", "30", "123456789")
    second = InsuredPerson("Anna", "Šťastná", "60", "111222333")
    manager.add_insured_person(first)
    manager.add_insured_person(second)

    assert manager.find_insured_person("Anna", "Šťastná") == [first, second]