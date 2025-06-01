"""
Provide utility functions for obtaining and classifying numeric scores
Code by: Miss Ghost/April First
"""
def main():
    import random
    score = float(input("Enter score: "))
    print(determine_result(score))
    score = random.uniform(0,100)
    print(determine_result(score))

def get_score():
    """Gets a score from a user, ensuring it is within the range 0 to 100 (inclusive)."""
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Score should be between 0 and 100 inclusive")
        score = int(input("Enter your score: "))

def determine_result(score):
    """Determines whether a given score is 'Bad/Passable/Excellent'"""
    if score < 50:
        return "Bad"

    elif score < 90:
        return "Passable"

    else:
        return "Excellent"

if __name__ == "__main__":
    main()