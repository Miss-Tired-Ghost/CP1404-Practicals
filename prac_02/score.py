"""
Determine the quality of a given score
Code by: Miss Ghost/April First
"""
def main():
    import random
    score = float(input("Enter score: "))
    print(determine_result(score))
    score = random.uniform(0,100)
    print(determine_result(score))

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"

    elif score < 50:
        return "Bad"

    elif score < 90:
        return "Passable"

    else:
        return "Excellent"

if __name__ == "__main__":
    main()