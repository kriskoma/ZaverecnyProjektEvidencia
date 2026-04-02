class InsuranceManager:
    def __init__(self):
        self._insured_people = [] # creating an empty list of insured people

    # adding the insured person to the database/list of insured people
    def add_insured_person(self, insured_person):
        self._insured_people.append(insured_person)

    # finding insured person based on first and last name
    def find_insured_person(self, first_name, last_name):
        list_of_insured_people = []
        for insured_person in self._insured_people:
            if (insured_person.first_name.lower() == first_name.lower() and
                insured_person.last_name.lower() == last_name.lower()):
                list_of_insured_people.append(insured_person)
        return list_of_insured_people  # if not found

    # display of all insured people
    def get_insured_people(self):
        return self._insured_people
