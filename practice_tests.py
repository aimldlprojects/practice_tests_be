from fastapi import FastAPI, Query
from typing import List
from pydantic import BaseModel
import random, json
from postgres import * 

app = FastAPI()





@app.get("/get_users")
async def get_users():
    users_details = get_users_pg()
    users = [user_data[1] for user_data in users_details]
    return {"users": users}

@app.get("/get_subjects")
async def get_subjects(user: str = Query(..., description="User name")):
    if user in subjects:
        return {"subject": subjects[user]}
    else:
        return {"error": "User not found"}

@app.get("/get_topics")
async def get_topics(user: str = Query(..., description="User name"), subject: str = Query(..., description="Subject name")):
    if user in topics and subject in topics[user]:
        return {"topic": topics[user][subject]}
    else:
        return {"error": "User or subject not found"}

@app.get("/get_questions")
async def get_questions(user: str = Query(..., description="User name"), subject: str = Query(..., description="Subject name"), topic: str = Query(..., description="Topic name")):
    if user in questions and subject in questions[user] and topic in questions[user][subject]:
        # Get a random question from the list
        question_data = random.choice(questions[user][subject][topic])
        question_number = 1  # Replace with actual question number logic
        total_questions = len(questions[user][subject][topic]) 
        return {
            "question": question_data["question"],
            "options": question_data["options"],
            "question_type": question_data["question_type"],
            "question_number": question_number,
            "total_questions": total_questions,
            "test_status": "not_completed" if total_questions > question_number else "completed",
        }
    else:
        return {"error": "User, subject, or topic not found"}

@app.get("/check_answer")
async def check_answer(user: str = Query(..., description="User name"), subject: str = Query(..., description="Subject name"), topic: str = Query(..., description="Topic name"), question: str = Query(..., description="question"), answer: str = Query(..., description="User's answer")):
    if user in questions and subject in questions[user] and topic in questions[user][subject]:
        # # Get the correct answer for the current question (replace with your actual logic)
        # correct_answer = questions[user][subject][topic][0]["answer"] 
        question_data = None
        for q in questions[user][subject][topic]:
            if q["question"] == question:  # Replace with actual question identification logic
                question_data = q
            break
        if question_data:
            correct_answer = question_data["answer"]
        else:
            return {"error": "Question not found"}
        if answer == correct_answer:
            answer_status = "correct"
        else:
            answer_status = "wrong"
        # Calculate score (replace with your actual scoring logic)
        score = "1/1"  # Example: 1 out of 1 question answered correctly
        return {"answer_status": answer_status, "answer": correct_answer, "score": score}
    else:
        return {"error": "User, subject, or topic not found"}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice_tests:app", host="127.0.0.1", port=8000, reload=True)