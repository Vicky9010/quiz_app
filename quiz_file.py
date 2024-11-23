import getpass
import json

USER_DATA_FILE = "users_data.json"

def load_users():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user data to a file
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)

# Quiz questions for different topics
questions = {
    "DBMS": [
        {"question": "What does DBMS stand for?", "choices": ["A) Database Management System", "B) Data Management System", "C) Database Manipulation System", "D) Data Manipulation System"], "answer": "A"},
        {"question": "Which of the following is a NoSQL database?", "choices": ["A) MySQL", "B) MongoDB", "C) PostgreSQL", "D) Oracle"], "answer": "B"},
        {"question": "What is a primary key?", "choices": ["A) A unique identifier", "B) A duplicate value", "C) A type of query", "D) An SQL command"], "answer": "A"},
        {"question": "Which command is used to fetch data from a database?", "choices": ["A) INSERT", "B) UPDATE", "C) DELETE", "D) SELECT"], "answer": "D"},
        {"question": "Which normal form removes transitive dependency?", "choices": ["A) 1NF", "B) 2NF", "C) 3NF", "D) BCNF"], "answer": "C"},
    ],
    "DSA": [
        {"question": "What is the time complexity of binary search?", "choices": ["A) O(n)", "B) O(log n)", "C) O(n^2)", "D) O(1)"], "answer": "B"},
        {"question": "Which data structure uses LIFO order?", "choices": ["A) Queue", "B) Stack", "C) Array", "D) Tree"], "answer": "B"},
        {"question": "What is a linked list?", "choices": ["A) A sequence of nodes", "B) A type of array", "C) A tree structure", "D) A type of graph"], "answer": "A"},
        {"question": "What is the best case time complexity of bubble sort?", "choices": ["A) O(n^2)", "B) O(log n)", "C) O(n)", "D) O(1)"], "answer": "C"},
        {"question": "Which data structure uses FIFO order?", "choices": ["A) Queue", "B) Stack", "C) Array", "D) Graph"], "answer": "A"},
    ],
    "Python": [
        {"question": "What is the output of 'print(2 ** 3)'?", "choices": ["A) 5", "B) 6", "C) 8", "D) 9"], "answer": "C"},
        {"question": "Which of the following is used to define a function?", "choices": ["A) def", "B) function", "C) func", "D) define"], "answer": "A"},
        {"question": "What data type is used to store True or False?", "choices": ["A) int", "B) str", "C) bool", "D) float"], "answer": "C"},
        {"question": "What is the output of 'print(type(42))'?", "choices": ["A) str", "B) int", "C) float", "D) bool"], "answer": "B"},
        {"question": "Which of these is a mutable data type?", "choices": ["A) tuple", "B) list", "C) string", "D) int"], "answer": "B"},
    ]
}

def register(users):
    """Registers a new user."""
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
    else:
        password = getpass.getpass("Enter password: ")
        users[username] = {"password": password, "score": 0}
        save_users(users)  
        print("Registration successful.")

def login(users):
    """Logs in a user."""
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if users.get(username, {}).get("password") == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid credentials.")
        return None

def take_quiz(username, users):
    """Takes the quiz for the selected topic."""
    print("\nChoose a topic for quiz:")
    print("1. DBMS")
    print("2. DSA")
    print("3. Python")
    topic_choice = input("Enter the number of your chosen topic: ")

    topics = {"1": "DBMS", "2": "DSA", "3": "Python"}
    topic = topics.get(topic_choice)

    if topic is None:
        print("Invalid choice.")
        return

    print(f"\n--- {topic} Quiz ---")
    score = 0
    for q in questions[topic]:
        print(f"{q['question']}")
        for choice in q["choices"]:
            print(choice)
        answer = input("Your answer (A, B, C, D): ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
    users[username]["score"] = score
    save_users(users)  
    print(f"You scored {score}/{len(questions[topic])} in {topic} quiz.")

def show_result(username, users):
    """Shows the user's last quiz score."""
    print(f"Your last score: {users[username]['score']}")

def main():
    """Main function to handle app flow."""
    users = load_users()  

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register(users)
        elif choice == "2":
            username = login(users)
            if username:
                while True:
                    print("\n1. Take Quiz\n2. Show Result\n3. Logout")
                    option = input("Choose an option: ")
    
                    if option == "1":
                        take_quiz(username, users)
                    elif option == "2":
                        show_result(username, users)
                    elif option == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
