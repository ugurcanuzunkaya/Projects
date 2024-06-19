import json

with open(r'/Users/ugurcanuzunkaya/Documents/GitHub/Projects/udemy/arditsulce/pythonmega/module1/questions.json', 'r') as file:
    questions = json.load(file)

score = 0

for question in questions:
    print(question['question_text'])
    for i, option in enumerate(question['alternatives']):
        print(f"{i + 1}. {option}")
    answer = int(input("Enter your answer (in number): "))
    if question['correct_answer'] == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {question['correct_answer']}")
        print()
        score -= 1

print(f"Your final score is {score}")