import json

with open("files/questions.json", "r") as file:
    content = file.read()

print(type(content))
print(content)


data = json.loads(content)
print(type(data))
print(data)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index +1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["given_answer"] = user_choice


print(data)


score = 0
for index, question in enumerate(data):
    if question["given_answer"] == question['correct_answer']:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = (f"{index + 1} - {result} - Your answer is {question['given_answer']}, "
               f"Correct answer is {question['correct_answer']}")
    print(message)

print("Score is",score, "/",len(data))

