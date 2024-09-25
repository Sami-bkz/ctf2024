import requests

i = 1
while(True):
    print(f"Question {i}")
    ans = input("Enter answer (or 'skip' to skip the question): ").strip()
    
    if ans.lower() == "skip":
        choice = input("Do you want to go to a specific question? (y/n): ").strip().lower()
        if choice == "y":
            question_num = int(input("Enter the question number: "))
            i = question_num
        print("Question skipped.")
        if choice == "n":
             i += 1
        continue
    
    data = {
        "number": str(i),
        "answer": ans,
        "user": "s.mahrez"
    }

    r = requests.post("http://34.163.57.143/", data=data)
    r.raise_for_status()  # Vérifier si la requête a échoué
    response = r.json()
    
    if response["response"]:
        print("Correct answer!")
        i = i + 1
    else:
        print("Incorrect answer. Try again.")