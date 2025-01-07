import requests
import random
import html

def main():
    """Main function to execute the quiz app."""
    print("Welcome to the Quiz App!")
    questions = fetch_quiz_data()

    if not questions:
        print("Sorry, we couldn't load the quiz questions. Please try again later.")
        return

    score = run_quiz(questions)
    display_score(score, len(questions))

    while True:
        retry = input("\nWould you like to try again? (yes/no): ").strip().lower()
        if retry == "yes":
            main()
        elif retry == "no":
            print("Thank you for playing the Quiz App! Goodbye!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def fetch_quiz_data():
    """Fetch quiz data from the Open Trivia Database API."""
    while True:
        get_difficulty_level = int(input("Choose a difficulty level \n1. Easy\n2. Medium\n3. Hard \nEnter your choice (1-3): "))
        if get_difficulty_level == 1:
            difficulty_level = "easy"
            break

        elif get_difficulty_level == 2:
            difficulty_level = "medium"
            break
        elif get_difficulty_level == 3:
            difficulty_level = "har"
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 3.\n")
    while True:
        number_of_questions = int(input("How many questions would you like the quiz to have? (1-50): "))
        if 1 <= number_of_questions <= 50:
            break
        else:
             print("Invalid choice. Please choose a number between 1 and 50.\n")

    url = f"https://opentdb.com/api.php?amount={number_of_questions}&difficulty={difficulty_level}&type=multiple"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        questions = data.get("results", [])
        # Decode HTML entities in the questions and answers
        for question in questions:
            question["question"] = html.unescape(question["question"])
            question["correct_answer"] = html.unescape(question["correct_answer"])
            question["incorrect_answers"] = [html.unescape(ans) for ans in question["incorrect_answers"]]
        return questions
    except requests.RequestException as e:
        print(f"Error fetching quiz data: {e}")
        return []

def run_quiz(questions):
    """Run the quiz by presenting questions to the user and collecting answers."""
    score = 0
    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")
        all_answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(all_answers)

        for i, answer in enumerate(all_answers, start=1):
            print(f"{i}. {answer}")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        selected_answer = all_answers[choice - 1]
        if selected_answer == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['correct_answer']}")

    return score

def display_score(score, total):
    """Display the user's score and provide feedback."""
    percentage = (score / total) * 100
    print("\nQuiz Completed!")
    print(f"You answered {score} out of {total} questions correctly.")
    print(f"Your score: {percentage:.2f}%")

    if percentage == 100:
        print("Outstanding! You're a quiz master!")
    elif percentage >= 70:
        print("Great job! You're doing very well.")
    elif percentage >= 40:
        print("Good effort! Keep practicing.")
    else:
        print("Don't worry! Try again and you'll do better next time.")


if __name__ == "__main__":
    main()
