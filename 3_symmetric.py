"""
Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад,
 ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, 
 несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.
"""
import colorama

def symmetrically(s: str) -> str:
    "Check if the separators in the string are symmetric"
    stack = []
    matching_pairs = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        # If the character is an opening bracket, add it to the stack
        if c in matching_pairs:
            stack.append(c)
        # If the character is a closing bracket
        elif c in matching_pairs.values():
            if not stack:
                return f"Unexpected closing bracket: {c}"
            # Check if the last opening bracket matches the closing bracket
            last_open = stack.pop()
            # If the brackets don't match, return a mismatch message
            if matching_pairs[last_open] != c:
                return f"Mismatch: {last_open} closed by {c}"

    if stack:
        return f"Unmatched opening brackets: {''.join(stack)}"

    return "Symmetric"

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

            result = symmetrically(command)

            if result == "Symmetric":
                color = colorama.Fore.GREEN
                print(f"Are the separators in {command} symmetric? {color}Yes")
            else:
                color = colorama.Fore.RED
                message_color = colorama.Fore.YELLOW
                print(f"Are the separators in {command} symmetric? {color}No, {message_color}{result}")

            print(colorama.Style.RESET_ALL)
    finally:
        print("Exiting program.")

if __name__ == "__main__":
    main()