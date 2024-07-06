
"""
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
а також бути нечутливою до регістру та пробілів.
"""
from collections import deque
import colorama

def is_palindrome(string: str) -> bool:
    "Check if a string is a palindrome"
    string = string.lower().replace(" ", "")
    queue = deque(string)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True


def main():
    "Main function of the program"
    try:
        while True:
            try:
                command = input("Enter a string to check: ")
            except KeyboardInterrupt:
                # User interrupted the program with ctrl+c
                print("\nProgram interrupted by user (ctrl+c). Exiting...")
                break
            except EOFError:
                # User interrupted the program with ctrl+d
                print("\nProgram interrupted by user (ctrl+d). Exiting...")
                break

            if command == "exit":
                break

            result = is_palindrome(command)

            color = colorama.Fore.GREEN if result else colorama.Fore.RED

            print(f"Is {command} a palindrome? {color}{'Yes' if result else 'No'}")
            print(colorama.Style.RESET_ALL)
    finally:
        print("Exiting program.")

if __name__ == "__main__":
    main()
