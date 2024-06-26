# Quiz Application

## Overview
This quiz application is a simple command-line program that loads questions from a JSON file and quizzes the user, keeping track of their score based on their answers.

## Key Libraries
- **JSON**: Used for loading and parsing the questions from a JSON file.

## Project Structure
```
quiz_app/
│
├── questions.json        # JSON file containing quiz questions and answers
└── quizapp.py            # The main script to run the quiz application
```

## External File Structure
- **questions.json**: This JSON file contains the quiz questions, possible answers, and the correct answer index. Example:
  ```json
  [
      {
          "question_text": "What are dolphins?",
          "alternatives": [
              "Fish",
              "Mammals",
              "Birds",
              "Reptiles"
          ],
          "correct_answer": 2
      },
      ...
  ]
  ```

## Explanation of Key Functions and Methods
- **Loading questions**: The script reads the questions from `questions.json` using the `json` library.
- **Iterating through questions**: It iterates through each question, displays the question text and alternatives, and prompts the user for an answer.
- **Checking answers**: The user's answer is checked against the correct answer, and the score is updated accordingly.

### quizapp.py
This script is responsible for running the quiz application. It loads the questions from the JSON file, iterates through each question to prompt the user for an answer, checks the answer, and updates the score. The final score is displayed at the end of the quiz.

### questions.json
This JSON file contains a list of quiz questions. Each question has the following structure:
- `question_text`: The text of the question.
- `alternatives`: A list of possible answers.
- `correct_answer`: The index (1-based) of the correct answer in the `alternatives` list.

## Final Output
The final output is a command-line quiz that prompts the user with questions, accepts answers, and provides feedback on whether the answers are correct or incorrect. The user's score is displayed at the end of the quiz.
