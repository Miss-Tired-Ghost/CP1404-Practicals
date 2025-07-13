"""
Demonstrate programming language class usage
Goaltime: 10 min
Worktime: 5 min
Code by: Miss Ghost/April First
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create and filter a list of programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
