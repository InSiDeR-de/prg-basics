def f(subject):
    max_avg = -1
    max_subject = None
    
    for subject_name, grades in subject.items():
        avg = sum(grades) / len(grades)
        if avg > max_avg:
            max_avg = avg
            max_subject = subject_name
    
    return max_subject



if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))