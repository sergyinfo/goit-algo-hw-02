"""
Потрібно розробити програму, яка імітує приймання й обробку заявок: 
програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером 
або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги 
для "обробки", імітуючи таким чином роботу сервісного центру.
"""
import random
import time
import uuid
from sys import exit
from queue import Queue
import colorama

q = Queue()

class Request:
    """
    Request class with unique id
    """
    def __init__(self):
        "Create a request with unique id"
        self.id = uuid.uuid4()
        # highlight with yellow color using colorama
        print(colorama.Fore.YELLOW, end="")
        print(f"Request {self.id} created")

    def process(self):
        "Process the request"
        print(colorama.Fore.GREEN, end="")
        print(f"Request {self.id} processed")

def generate_request():
    "Generate a request and add it to the queue"
    request = Request()

    # Add the request to the queue
    q.put(request)

def process_request():
    "Process the request from the queue"
    if not q.empty():
        request = q.get()
        request.process()
    else:
        print(colorama.Fore.RED, end="")
        print("Queue is empty")

def fake_queue_process():
    "Immitate the queue processing"
    while True:
        # choose a random action
        action = random.choice([generate_request, process_request])

        #choose a random delay
        delay = random.randint(1, 5)
        time.sleep(delay)

        #perform the action
        action()


def main():
    "Main function of the program"
    try:
        while True:
            try:
                command = input("Enter command: ")
                command = command.strip().lower()
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

            match command:
                case "generate":
                    generate_request()
                case "process":
                    process_request()
                case "immitate":
                    fake_queue_process()
                case _:
                    print("Unknown command")
    finally:
        print("Exiting program.")

if __name__ == "__main__":
    main()
