import random

famousPeople = {
    "Albert Einstein": 1879,      
    "Isaac Newton": 1643,         
    "Marie Curie": 1867,          
    "Leonardo da Vinci": 1452,                 
    "William Shakespeare": 1564,         
}

def startQuiz():
    correctAnswers = 0

    for person, birthYear in famousPeople.items():
        answer = int(input(f"What is the birth year of {person}? "))

        if answer == birthYear:
            correctAnswers += 1
        else:
            print(f"Incorrect! The correct year is {birthYear}.")

    totalQuestions = len(famousPeople)
    incorrectAnswers = totalQuestions - correctAnswers
    correctPercentage = (correctAnswers * 100) / totalQuestions
    incorrectPercentage = 100 - correctPercentage

    print(f"\nResults:")
    print(f"Correct answers: {correctAnswers}")
    print(f"Incorrect answers: {incorrectAnswers}")
    print(f"Percentage of correct answers: {correctPercentage:.2f}%")
    print(f"Percentage of incorrect answers: {incorrectPercentage:.2f}%")

while True:
    startQuiz()
    playAgain = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if playAgain != "yes":
        break