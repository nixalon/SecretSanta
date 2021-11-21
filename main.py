from random import *
people = []
#while True:
#    person = input("Enter a person participating.(end to exit):\n")
#    if person == "end": break
#    people.append(person)
people = ["Emil", "Alexandra", "Birte", "Johan", "Ebba", "Jonas", "CJ",
"Linn", "Joakim", "Maria"]

shuffle(people)
for i in range(len(people)):
    print(people[i],"buys for",people[(i+1)%(len(people))])



