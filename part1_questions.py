import random

part1_questions = [
    "Do you work or study?",
    "Why did you choose your subject?",
    "What do you usually do in your free time?",
    "Do you like reading books?",
    "How often do you use the internet?",
    "Do you enjoy watching movies?",
    "What kind of music do you like?",
    "Do you prefer morning or evening?",
    "Do you like cooking?",
    "How often do you exercise?",

    # 👉 KEEP ADDING QUESTIONS HERE
    # You can safely paste all 600 questions in this list
]

def get_10_part1_questions():
    return random.sample(part1_questions, 10)
