
def f(array):
    count = 0
    for username in array:
        if 4 <= len(username) <= 12:
            valid = True
            for char in username:
                if not (char.islower() or char.isdigit() or char == '_'):
                    valid = False
                    break
            if valid:
                count += 1
    return count

if __name__ == "__main__":
    print(f(["uex", "water_7_x", "anna.may", "a_b_c_d_e_f"]))
    print(f(["valid_user", "InvalidUser", "user@name", "user_name123", "sh"] ))
