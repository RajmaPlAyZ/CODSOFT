import random

# List of questions and answers
qa_list = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the smallest country in the world?", "Vatican City"),
    ("What is the highest mountain in the world?", "Mount Everest"),
    ("What is the largest ocean in the world?", "Pacific Ocean")
]

# Shuffle the list
random.shuffle(qa_list)

# Initialize score
score = 0

# Loop through each question
for question, answer in qa_list:
    # Display question and get user's answer
    user_answer = input(question + " ")
    
    # Check if answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", answer)
        
# Display final score
print("Your final score is", score)