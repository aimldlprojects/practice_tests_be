import psycopg2
from psycopg2 import sql

# Database connection URL
DATABASE_URL = "postgresql://postgres:password123@localhost:5432/tests"

# Function to execute a query
def execute_query(query):
    try:
        # Connect to the database
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

        # Commit the transaction
        connection.commit()

        print("Query executed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Function to create a table
def create_table(table_name, schema):
    query = f"CREATE TABLE IF NOT EXISTS {table_name} {schema};"
    execute_query(query)

# Function to delete (drop) a table
def delete_table(table_name):
    query = f"DROP TABLE IF EXISTS {table_name};"
    execute_query(query)

# Function to insert a new user
def insert_user(username, email):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(query, (username, email))
        connection.commit()
        print("User inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to delete a user
def delete_user(username):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        connection.commit()
        print("User deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to insert a new subject
def insert_subject(subject_name):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "INSERT INTO subjects (subject_name) VALUES (%s)"
        cursor.execute(query, (subject_name,))
        connection.commit()
        print("Subject inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to delete a subject
def delete_subject(subject_name):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "DELETE FROM subjects WHERE subject_name = %s"
        cursor.execute(query, (subject_name,))
        connection.commit()
        print("Subject deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to insert a new topic
def insert_topic(topic_name, subject_id):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "INSERT INTO topics (topic_name, subject_id) VALUES (%s, %s)"
        cursor.execute(query, (topic_name, subject_id))
        connection.commit()
        print("Topic inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to delete a topic
def delete_topic(topic_name):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "DELETE FROM topics WHERE topic_name = %s"
        cursor.execute(query, (topic_name,))
        connection.commit()
        print("Topic deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to insert a new question
def insert_question(question_text, options, question_type, answer, topic_id):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "INSERT INTO questions (question_text, options, question_type, answer, topic_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (question_text, options, question_type, answer, topic_id))
        connection.commit()
        print("Question inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
# Function to update a question
def update_question_status(question_id, current_attempt_status):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        if current_attempt_status == "correct":
            query = """
            UPDATE questions
            SET 
                previous_attempt_status = current_attempt_status,
                total_no_of_attempts = total_no_of_attempts + 1,
                total_no_of_correct_attempts = total_no_of_correct_attempts + 1,
                score = round((total_no_of_correct_attempts) / (total_no_of_attempts), 2),
                last_attempted_datetime = NOW()
            WHERE question_id = %s;
            """
        else:
            query = """
            UPDATE questions
            SET 
                previous_attempt_status = current_attempt_status,
                total_no_of_attempts = total_no_of_attempts + 1,
                total_no_of_incorrect_attempts = total_no_of_incorrect_attempts + 1,
                score = round(total_no_of_correct_attempts / total_no_of_attempts, 2),
                last_attempted_datetime = NOW()
            WHERE question_id = %s;
            """
        cursor.execute(query, (question_id,))
        connection.commit()
        print("Question status updated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to delete a question
def delete_question(question_text):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "DELETE FROM questions WHERE question_text = %s"
        cursor.execute(query, (question_text,))
        connection.commit()
        print("Question deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to get all users
def get_users_pg():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to get all subjects
def get_subjects_pg():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "SELECT * FROM subjects"
        cursor.execute(query)
        subjects = cursor.fetchall()
        return subjects
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to get all Related Subjects for User
def get_related_subjects_pg(username):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = """
        SELECT s.subject_id, s.subject_name
        FROM subjects s
        JOIN user_subjects us ON s.subject_id = us.subject_id
        JOIN users u ON us.user_id = u.user_id
        WHERE u.username = %s;
        """
        cursor.execute(query, (username,))
        subjects = cursor.fetchall()
        return subjects
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to get all Related Topics for User and Subject
def get_related_topics_pg(username, subject_name):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = """
        SELECT t.topic_id, t.topic_name
        FROM topics t
        JOIN subjects s ON t.subject_id = s.subject_id
        JOIN user_topics ut ON t.topic_id = ut.topic_id
        JOIN users u ON ut.user_id = u.user_id
        WHERE u.username = %s AND s.subject_name = %s;
        """
        cursor.execute(query, (username, subject_name))
        topics = cursor.fetchall()
        return topics
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
# Function to get all questions for a topic of the selected subject and user
def get_releated_questions_pg(username, subject_name, topic_name):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = """
        SELECT q.question_id, q.question_text, q.options, q.question_type, q.answer
        FROM questions q
        JOIN topics t ON q.topic_id = t.topic_id
        JOIN subjects s ON t.subject_id = s.subject_id
        JOIN user_topics ut ON t.topic_id = ut.topic_id
        JOIN users u ON ut.user_id = u.user_id
        WHERE u.username = %s AND s.subject_name = %s AND t.topic_name = %s;
        """
        cursor.execute(query, (username, subject_name, topic_name))
        questions = cursor.fetchall()
        return questions
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to get all topics
def get_topics_pg():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "SELECT * FROM topics"
        cursor.execute(query)
        topics = cursor.fetchall()
        return topics
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to get all questions
def get_questions_pg():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "SELECT * FROM questions"
        cursor.execute(query)
        questions = cursor.fetchall()
        return questions
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


# Examples:
# user_schema = """(
#                     user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
#                     username VARCHAR(255) NOT NULL UNIQUE,
#                     email VARCHAR(255) UNIQUE,
#                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                 );"""
# subjects_schema = """(
#                     subject_id SERIAL PRIMARY KEY, -- Unique identifier for each subject
#                     subject_name VARCHAR(255) NOT NULL UNIQUE,
#                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                 );"""
# topics_schema = """(
#                     topic_id SERIAL PRIMARY KEY, -- Unique identifier for each topic
#                     topic_name VARCHAR(255) NOT NULL,
#                     subject_id INT NOT NULL REFERENCES subjects(subject_id) ON DELETE CASCADE,
#                     UNIQUE(topic_name, subject_id) -- Ensures topics are unique within a subject
#                 );"""
# questions_schema = """(
#                         question_id SERIAL PRIMARY KEY,               -- Unique identifier for each question
#                         question_text TEXT NOT NULL,                 -- The text of the question
#                         options JSONB NOT NULL,                      -- Array of options, stored as JSONB
#                         question_type VARCHAR(50) NOT NULL,          -- Type of question (e.g., "mcq")
#                         answer TEXT NOT NULL,                        -- Correct answer to the question
#                         previous_attempt_status VARCHAR(50),         -- Status of the last attempt (e.g., "correct", "incorrect")
#                         total_no_of_attempts INT DEFAULT 0,          -- Total number of attempts
#                         total_no_of_correct_attempts INT DEFAULT 0,  -- Total number of correct attempts
#                         total_no_of_incorrect_attempts INT DEFAULT 0,-- Total number of incorrect attempts
#                         score DECIMAL(5, 2) DEFAULT 0.0,             -- Score for the question (e.g., 0.50)
#                         last_attempted_datetime TIMESTAMP,           -- Timestamp of the last attempt
#                         topic_id INT NOT NULL REFERENCES topics(topic_id) ON DELETE CASCADE, -- Foreign key to topics table
#                         difficulty_level INT CHECK (difficulty_level BETWEEN 1 AND 5), -- Difficulty level of the question
#                         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the question was created
#                     );"""

# user_subjects_schema = """(
#                     user_subject_id SERIAL PRIMARY KEY, -- Unique identifier for each user-subject relationship
#                     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
#                     subject_id INT NOT NULL REFERENCES subjects(subject_id) ON DELETE CASCADE,
#                     UNIQUE(user_id, subject_id) -- Ensures a user cannot have duplicate entries for the same subject
#                 );"""
# user_topics_schema = """(
#                     user_topic_id SERIAL PRIMARY KEY, -- Unique identifier for each user-topic relationship
#                     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
#                     topic_id INT NOT NULL REFERENCES topics(topic_id) ON DELETE CASCADE,
#                     UNIQUE(user_id, topic_id) -- Ensures a user cannot have duplicate entries for the same topic
#                 );"""

# create_table(table_name="users", schema=user_schema)
# create_table(table_name="subjects", schema=subjects_schema)
# create_table(table_name="topics", schema=topics_schema)
# create_table(table_name="questions", schema=questions_schema)
# create_table(table_name="user_subjects", schema=user_subjects_schema)
# create_table(table_name="user_topics", schema=user_topics_schema)
## delete_table(table_name="test")

# insert_user(username="bhavi", email="poluribhavyesh@gmail.com")
# insert_user(username="madhu", email="polurimadhurya@gmail.com")
# insert_user(username="user", email="testuser@gmail.com")
# insert_user(username='testuser1', email='testuser1@gmail.com')
## delete_user(username="testuser1")

# subjects = ["Math", "English", "Science", "Computer Science", "Social", "GK", "French", "Telugu"]
# for subject in subjects:
#     insert_subject(subject_name=subject)

# topics = ["Additions", "Subtractions", "Multiplications", "Divisions", "Grammar", "Vocabulary", "Spellings", "Verbs", "Nouns", "Pronouns", "Prepositions", "Physics", "Chemistry", "History", "Geography", "Programming", "Algorithms", "Current Affairs", "Famous Personalities", "World Leaders", "French Grammar", "French Vocabulary", "Telugu Grammar", "Telugu Vocabulary"]
# subject_ids = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7]
# for topic, subject_id in zip(topics, subject_ids):
#     insert_topic(topic_name=topic, subject_id=subject_id)

# questions = ["2 + 3 = ?", "5 - 2 = ?", "2 * 3 = ?", "6 / 2 = ?", "What is the capital of France?", "Who wrote 'Romeo and Juliet'?", "What is the past tense of 'run'?", "What is a noun?", "What is a pronoun?", "What is a verb?", "What is a preposition?", "What is the formula for force?", "What is the atomic number of Hydrogen?", "Who was the first President of the United States?", "What is the largest continent in the world?", "What is the difference between 'while' and 'for' loop?", "Who is known as the 'Father of the computer'?", "Who is known as the 'Father of the Nation'?", "What is the French word for 'hello'?", "What is the French word for 'goodbye'?", "What is the Telugu word for 'book'?", "What is the Telugu word for 'pen'?"]
# options = ['[5,4,6,7]', "[3,2,4,5]", "[6,4,8,9]", "[3,2,4,5]", '["Paris", "London", "Berlin", "Rome"]', '["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"]', '["ran", "runned", "running", "runs"]', '["A person, place, or thing", "An action word", "A describing word", "A joining word"]', '["A word that takes the place of a noun", "A word that describes a noun", "A word that shows action", "A word that shows a state of being"]', '["A word that shows action", "A word that describes a noun", "A word that takes the place of a noun", "A word that shows a state of being"]', '["A word that shows action", "A word that describes a noun", "A word that takes the place of a noun", "A word that shows a state of being"]', '["F = ma", "F = mv", "F = m/a", "F = m^2"]', "[1, 2, 3, 4]", '["George Washington", "Thomas Jefferson", "John Adams", "Abraham Lincoln"]', '["Asia", "Africa", "Europe", "North America"]', '["while loop is entry-controlled and for loop is exit-controlled", "for loop is entry-controlled and while loop is exit-controlled", "while loop is used for iteration and for loop is used for decision-making", "for loop is used for iteration and while loop is used for decision-making"]', '["Charles Babbage", "Alan Turing", "John von Neumann", "Tim Berners-Lee"]', '["Mahatma Gandhi", "Nelson Mandela", "Abraham Lincoln", "Martin Luther King Jr."]', '["Bonjour", "Salut", "Merci", "Oui"]', '["Au revoir", "Salut", "Merci", "Oui"]', '["Pustakam", "Pustak", "Pustakamu", "Pustakalu"]', '["Kalam", "Kalamu", "Kalamu", "Kalamalu"]']

# question_types = ["MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ", "MCQ"]
# answers = [5, 3, 6, 3, "Paris", "William Shakespeare", "ran", "A person, place, or thing", "A word that takes the place of a noun", "A word that shows action", "A word that shows action", "F = ma", 1, "George Washington", "Asia", "'while' loop is entry-controlled and 'for' loop is exit-controlled", "Charles Babbage", "Mahatma Gandhi", "Bonjour", "Au revoir", "Pustakam", "Kalam"]
# topic_ids = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7]
# for question, option, question_type, answer, topic_id in zip(questions, options, question_types, answers, topic_ids):
#     insert_question(question_text=question, options=option, question_type=question_type, answer=answer, topic_id=topic_id)

# # insert user_subjects
# user_subjects = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
# for user_id, subject_id in user_subjects:
#     try:
#         connection = psycopg2.connect(DATABASE_URL)
#         cursor = connection.cursor()
#         query = "INSERT INTO user_subjects (user_id, subject_id) VALUES (%s, %s)"
#         cursor.execute(query, (user_id, subject_id))
#         connection.commit()
#         print("User-Subject relationship inserted successfully!")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()

# # insert user_topics
# user_topics = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4), (2, 5), (3, 3), (3, 6), (3, 7)]
# for user_id, topic_id in user_topics:
#     try:
#         connection = psycopg2.connect(DATABASE_URL)
#         cursor = connection.cursor()
#         query = "INSERT INTO user_topics (user_id, topic_id) VALUES (%s, %s)"
#         cursor.execute(query, (user_id, topic_id))
#         connection.commit()
#         print("User-Topic relationship inserted successfully!")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
    