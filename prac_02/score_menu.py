""""
Provides a menu for score.py
Code by: Miss Ghost/April First
"""
import score

def main():
    current_score = 0
    MENU = """
(G)et a score
(P)rint result
(S)how stars
(Q)uit
"""

    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        match choice:
            case "G":
                current_score = int(input("Enter your score: "))
                while current_score < 0 or current_score > 100:
                    print("Score should be between 0 and 100 inclusive")
                    current_score = int(input("Enter your score: "))

            case "P":
                print(score.determine_result(current_score))

            case "S":
                print("*" * current_score)

            case _:
                print("Invalid choice")

        print(MENU)
        choice = input("\nEnter your choice: ").upper()
    print("Farewell")

if __name__ == "__main__":
    main()