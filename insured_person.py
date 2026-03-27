class InsuredPerson:
    def __init__(self, first_name, last_name, age, phone_number):

        # verification if names are not empty
        valid_first_name = first_name.strip()
        if valid_first_name == "":
            raise ValueError("First name cannot be empty")

        valid_last_name = last_name.strip()
        if valid_last_name == "":
            raise ValueError("Last name cannot be empty")

        # verification if age is a positive number
        if not age.isdigit():
            raise ValueError("Age must be a positive integer")

        valid_age = int(age)
        if valid_age <= 0:
            raise ValueError("Age must be greater than zero")

        # verification if phone number is valid based on our country conditions
        valid_phone_number = phone_number.replace(" ", "").replace("-", "")

        if not valid_phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")

        if len(valid_phone_number) < 9 or len(valid_phone_number) > 12:
            raise ValueError("Phone number length is invalid")

        # if conditions are fulfilled => creating the attributes
        self._first_name = valid_first_name
        self._last_name = valid_last_name
        self._age = valid_age
        self._phone_number = valid_phone_number

    # creating methods via property which enable using the protected attribute in insurance_manager;
    # for finding insured person based on name and surname
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    # setting the display of the data
    def __str__(self):
        return str(f"{self._first_name} \t {self._last_name} \t {self._age} \t {self._phone_number}")

