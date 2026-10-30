import pytest

from insured_person import InsuredPerson


def make_person(first_name="Anna", last_name="Šťastná", age="30", phone_number="123456789"):
    """Pomocná funkcia: vytvorí platného poisteného, v teste mením len to, čo testujem."""
    return InsuredPerson(first_name, last_name, age, phone_number)


# ---------- Platné vstupy ----------

def test_valid_person_is_created():
    person = make_person()

    assert person.first_name == "Anna"
    assert person.last_name == "Šťastná"


def test_names_are_stripped_of_whitespace():
    person = make_person(first_name="  Anna  ", last_name="  Šťastná ")

    assert person.first_name == "Anna"
    assert person.last_name == "Šťastná"


def test_phone_number_spaces_and_dashes_are_removed():
    person = make_person(phone_number="911 123-456")

    assert "911123456" in str(person)


def test_age_is_stored_as_integer_in_output():
    person = make_person(age="42")

    assert "42" in str(person)


def test_str_contains_all_data():
    person = make_person("Anna", "Šťastná", "30", "123456789")

    assert str(person) == "Anna \t Šťastná \t 30 \t 123456789"


# ---------- Neplatné mená ----------

@pytest.mark.parametrize("first_name", ["", "   "])
def test_empty_first_name_raises_error(first_name):
    with pytest.raises(ValueError, match="First name cannot be empty"):
        make_person(first_name=first_name)


@pytest.mark.parametrize("last_name", ["", "   "])
def test_empty_last_name_raises_error(last_name):
    with pytest.raises(ValueError, match="Last name cannot be empty"):
        make_person(last_name=last_name)


# ---------- Neplatný vek ----------

@pytest.mark.parametrize("age", ["abc", "", "-5", "3.5", "12a"])
def test_non_numeric_age_raises_error(age):
    with pytest.raises(ValueError, match="Age must be a positive integer"):
        make_person(age=age)


def test_zero_age_raises_error():
    with pytest.raises(ValueError, match="Age must be greater than zero"):
        make_person(age="0")


def test_age_one_is_accepted_boundary():
    person = make_person(age="1")

    assert "1" in str(person)


# ---------- Neplatný telefón ----------

@pytest.mark.parametrize("phone", ["12345abc9", "abcdefghi", "", "   "])
def test_phone_with_non_digits_raises_error(phone):
    with pytest.raises(ValueError, match="Phone number must contain only digits"):
        make_person(phone_number=phone)


@pytest.mark.parametrize("phone", ["12345678", "1234567890123"])
def test_phone_with_invalid_length_raises_error(phone):
    # 8 číslic je príliš málo, 13 príliš veľa
    with pytest.raises(ValueError, match="Phone number length is invalid"):
        make_person(phone_number=phone)


@pytest.mark.parametrize("phone", ["123456789", "123456789012"])
def test_phone_length_boundaries_are_accepted(phone):
    # 9 a 12 číslic sú hraničné platné hodnoty
    person = make_person(phone_number=phone)

    assert phone in str(person)


def test_phone_with_plus_prefix_is_currently_rejected():
    # Zdokumentované aktuálne správanie: medzinárodný zápis "+421..." validácia odmietne,
    # lebo "+" nie je číslica. Ak by si to chcela podporovať, uprav validáciu aj tento test.
    with pytest.raises(ValueError, match="Phone number must contain only digits"):
        make_person(phone_number="+421 911 123 456")