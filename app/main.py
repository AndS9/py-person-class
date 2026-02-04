class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person in people:
        person_instances.append(Person(person["name"], person["age"]))

    name_of_partner = ""
    partner = ""
    for person in people:
        partner = list(person.keys())[2]
        if person.get(partner, None):
            name_of_partner = person.get(partner)
            if partner == "husband":
                Person.people[person["name"]].husband \
                    = Person.people[name_of_partner]
            elif partner == "wife":
                Person.people[person["name"]].wife \
                    = Person.people[name_of_partner]

    return person_instances
