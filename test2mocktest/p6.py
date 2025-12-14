import json

def f(age, course, average_grade):
    count = 0
    with open("data.json", "r", encoding='UTF-8') as file:
        data = json.load(file)
        for student in data:
            student_age = student["age"]
            if student_age >= age:
                courses = student["studies"]["courses"]
                for c in courses:
                    if c["name"] == course:
                        grades = c["grades"]
                        avg = round(sum(grades) / len(grades),2)
                        if avg >= average_grade:
                            count += 1
                        break
    return count

if __name__ == "__main__":
    print(f(21, "statistics", 4))
    print(f(20, "mathematics", 3.5))
    print(f(22, "physics", 4.5))
