from oop_lutz_01 import Person, Manager
import shelve


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay = 100000)
tom = Manager('Tom Jones', 80000)


with shelve.open('content/persondb') as db:
    for obj in (bob, sue, tom):
        db[obj.name] = obj


if __name__ == "__main__":

    """Change and save for example value of exemplar of class
    in shelve session"""
    
    with shelve.open('content/persondb') as db:
        sue = db['Sue Jones']
        sue.giveRise(.1)
        sue.giveRise(.1)
        db['Sue Jones'] = sue
        print(db['Sue Jones'])