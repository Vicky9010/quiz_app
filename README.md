
🎓 Quiz-App 📝
This is a console-based Quiz Application built with Python. The app allows users to register, log in, take quizzes, and view their scores. User data, including login credentials and quiz scores, are stored in a JSON file (users_data.json) for persistence.

✨ Features
👤 User Registration:

Users can create a new account with a unique username and password.
The app checks if the username already exists to avoid duplicates.
User data is stored in a users_data.json file.
🔒 User Login:

Users log in by entering their username and password.
Valid credentials allow access to the quiz and other features.
📚 Take Quiz:

Users can choose from three topics:
📂 DBMS
⚙️ DSA
🐍 Python
Each topic consists of multiple-choice questions.
Correct answers are scored, and users are notified about correct and wrong answers.
📊 View Score:

After completing the quiz, users can view their most recent quiz score for the selected topic.
💾 Data Persistence:

User data, including passwords and quiz scores, is saved and loaded from a JSON file (users_data.json).
🚀 Usage
1. Run the App
Execute the Python script to start the application:

bash
Copy code
python quiz_file.py
2. Options:
Register: Create a new user account.
Login: Access the quiz after logging in.
Exit: Close the application.
3. Quiz Flow:
After logging in, you can choose a topic for the quiz.
Answer the multiple-choice questions by typing the option letter (A, B, C, D).
Your score will be shown at the end of the quiz.
4. View Results:
Users can see their most recent score using the "Show Result" option.
📜 Topics and Questions
📂 DBMS: Questions related to Database Management Systems.
⚙️ DSA: Questions related to Data Structures and Algorithms.
🐍 Python: Questions related to Python programming.
💡 Example Output
plaintext
Copy code
1. Register
2. Login
3. Exit
Choose an option: 2
Enter username: John
Enter password:
Welcome, John!

1. Take Quiz
2. Show Result
3. Logout
Choose an option: 1

Choose a topic for quiz:
1. DBMS
2. DSA
3. Python
Enter the number of your chosen topic: 3

--- Python Quiz ---
What is the output of 'print(2 ** 3)'?
A) 5
B) 6
C) 8
D) 9
Your answer (A, B, C, D): C
Correct!

...

You scored 4/5 in Python quiz.
📈 How to Extend
➕ Add More Topics:
Add new topics and their respective questions in the questions dictionary.
🔒 Enhance Security:
Use password hashing libraries like bcrypt for more secure password storage.
💾 Save Data Persistently:
The current implementation saves user data to a JSON file. You can switch to a database like SQLite or MongoDB for scalability.
🛠 Requirements
🐍 Python 3.x
No additional libraries are required to run the app.
📂 Files
quiz_file.py: Main Python script to run the application.
users_data.json: JSON file that stores user data (usernames, passwords, and scores).
🎉 License
This project is open-source. Feel free to fork, modify, or contribute to improve it!
