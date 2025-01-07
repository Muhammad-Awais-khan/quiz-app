# Quiz App
#### Video Demo: https://youtu.be/DG4vYs465l0
#### Description:

The **Quiz App** is a Python-based interactive program designed to test the user's knowledge on various topics through dynamically fetched multiple-choice questions. By utilizing a trivia API, the app ensures that every quiz session offers fresh and diverse questions, enhancing user engagement and challenge.

This project focuses on user-friendly interaction, robust functionality, and modular code design. It employs Python’s capabilities for data retrieval, input validation, and automated testing. The app also includes thorough error handling to provide a seamless user experience.

---

### Files and Their Functions

1. **`project.py`**
   - This is the core file of the program, containing the main logic for the Quiz App. It includes the following key functions:
     - **`main()`**:
       Serves as the entry point, coordinating the entire quiz workflow.
     - **`fetch_quiz_data()`**:
       Connects to an online trivia API to retrieve a set of questions, ensuring dynamic content. Includes error handling for cases like network failures or invalid API responses.
     - **`run_quiz(questions)`**:
       Presents each question to the user, validates their answers, and tracks the score.
     - **`display_score(correct, total)`**:
       Calculates the final score and provides detailed feedback based on user performance.

2. **`test_project.py`**
   - Contains test cases to verify the functionality and reliability of the Quiz App. Using `pytest`, it ensures the correctness of:
     - API data fetching and parsing.
     - Score calculation and feedback generation.
     - Input validation and error handling.

3. **`requirements.txt`**
   - Lists all external dependencies required to run the project, including:
     - `requests`: For fetching questions from the trivia API.
     - `pytest`: For automated testing.

---

### Design Choices

1. **Dynamic Content**
   - By integrating a trivia API, the app avoids static question sets, making each quiz session unique and unpredictable.

2. **User-Centric Design**
   - The app ensures ease of use with clear instructions and intuitive inputs. Feedback at the end of the quiz adds a personalized touch, making it more engaging for users.

3. **Modularity**
   - The code is structured into self-contained functions, enabling easier debugging, testing, and potential feature additions.

4. **Error Handling**
   - Comprehensive error handling is implemented to account for API errors, network issues, and invalid user inputs, ensuring a smooth experience.

---

### Installation and Usage

1. Clone or download the repository.
2. Navigate to the project directory.
3. Install dependencies by running:
   ```bash
   pip install -r requirements.txt
