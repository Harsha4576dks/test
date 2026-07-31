quiz = [{
    "question":"what is the capital of india ?",
    "options":["delhi", "hyderabad", "mumbai", "chennai"],
    "correct_answer":"delhi"
},
{"question": "Mutable data type?",
  "options": ["Tuple", "List", "String"],
    "correct_answer": "List"},

    {"question": "Keyword for function?", 
     "options": ["func", "def", "function"],
       "correct_answer": "def"}
]
        
score = 0
for q in quiz:
    print("\n "+ q["question"])
    print("options:", q["options"])

    choice = input("enter your answer:")
    if choice == q["correct_answer"]:
            print("correct answer")
            score += 1
    else:
            print("invalid answer, correct_answer is:",q["correct_answer"])

print("\nFinal Score:", score, "/", len(quiz))