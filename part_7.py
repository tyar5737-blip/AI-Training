def greet():
    print("Hello Phoung")
    print("UCS")
greet()


def greet_student(name):
    print(f"Hello {name}")
    
greet_student("Ma Ma")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores
                        )
marks=[70,80,90]
result=calculate_average(marks)
print("Average:", result)



def count_passed(scores):
    passing = 0
    for score in scores:
        if score >= 40:
            passing += 1
    return passing

print("Passed:", count_passed([40, 50, 60, 70, 80]))

def classify_score(score):
  if score < 0 or score > 100:
    return "Invalid"
  elif score >= 80:
   return "Excellent"
  elif score >= 60:
   return "Good"
  elif score >= 40:
   return "Pass"
  else:
   return "Fail"
print(classify_score(90))
print(classify_score(55))
print(classify_score(25))


student_scores = [70, 85, 90, 65, 78]
print(student_scores)
print(student_scores[0])
print(student_scores[2])

scores = [70,85,90]

scores.append(95)
print(scores)

scores[0] = 75
print(scores)

scores.remove(85)
print(scores)

print("Count:", len(scores))
print('Highest:', max(scores))
print("Lowest:", min(scores))


location = (16.8, 96.15)

print("Lattitude:", location[0])
print("Longtidude:", location[1])

print("Number of values:", len(location))


student = {
    "name" : "Su Su",
    "age": 20,
    "score": 88,
    "passeed": True
    
}
print(student["name"])
print(student["score"])


student = {
    "name": "Su Su",
    "score": 88
    
}

student["course"] = "Python for AI"
student["score"] = 92

print(student.get("name"))
print(student.get("grade", "Not assigned"))
print(student)

students = [
    {"name": "Aung Aung", "score" :85},
     {"name": "Su", "score" :92},
     {"name": "Mg", "score" :35},
         
]
for student in students:
    print(student["name"], student["score"])



    