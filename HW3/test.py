from main import ConsoleUI

#Python's built-in functions, so input() can be swapped while the app runs
BUILTINS = __builtins__ if isinstance(__builtins__, dict) else __builtins__.__dict__
REAL_INPUT = BUILTINS["input"]

FILES = ["HW3/customers.csv", "HW3/vehicle.csv", "HW3/rentals.csv"]

#Each step: what it does, and the answers typed into the menu (11. Exit is added at the end)
STEPS = [
    ("Add 2 vehicles and 2 customers",
     ["1", "7ABC123", "Toyota", "Camry", "2022", "45",
      "1", "8XYZ999", "Honda", "Civic", "2021", "40",
      "3", "Bob", "Smith", "555-222-3333", "D200",
      "3", "Ann", "Adams", "555-444-5555", "D100"]),
    ("Update vehicle 7ABC123: change the daily rate to 50, then Done",
     ["2", "7ABC123", "5", "50", "0"]),
    ("Update customer D100: change the phone number, then Done",
     ["4", "D100", "3", "555-000-9999", "0"]),
    ("Rent 7ABC123 to Ann (D100) from 2026-11-01 to 2026-11-04",
     ["5", "1", "D100", "7ABC123", "2026-11-01", "2026-11-04"]),
    ("Try to rent 7ABC123 again to Bob (D200): it is already rented",
     ["5", "2", "D200", "7ABC123", "2026-11-01", "2026-11-02"]),
    ("Rent 8XYZ999 to Ann (D100) from 2026-11-02 to 2026-11-05",
     ["5", "2", "D100", "8XYZ999", "2026-11-02", "2026-11-05"]),
    ("Return rental 1 two days late (2026-11-06)",
     ["6", "1", "2026-11-06"]),
    ("Search a vehicle by plate, then by make/model",
     ["7", "8XYZ999", "7", "", "toyota", "camry"]),
    ("List all customers alphabetically",
     ["8"]),
    ("Show Ann's (D100) active and past rentals",
     ["9", "D100"]),
    ("Show the rental history of 7ABC123",
     ["10", "7ABC123"]),
]


def run_app(answers: list[str]) -> None:
    '''
    Run the real menu of main.py, with the answers typed for us, then 11. Exit
    '''
    answers = answers + ["11"]

    def fake_input(prompt: str = "") -> str:
        answer = answers.pop(0)
        print(prompt + answer) #Show what was "typed", like in a real terminal
        return answer

    BUILTINS["input"] = fake_input
    try:
        ConsoleUI().execute()
    finally: #Always give back the real input()
        BUILTINS["input"] = REAL_INPUT

def show_data() -> None:
    print("\n----- DATA IN THE CSV FILES -----")
    for filename in FILES:
        print(f"{filename}:")
        with open(filename) as file:
            rows = file.read().splitlines()
        if not rows:
            print("    (empty)")
        for row in rows:
            print(f"    {row}")


def main():
    #Start from empty files, the data of the mock run stays in the files at the end
    for filename in FILES:
        open(filename, "w").close()

    for number, (title, answers) in enumerate(STEPS, 1):
        print(f"\n\n########## STEP {number}: {title} ##########")
        run_app(answers)
        show_data()

if __name__ == "__main__":
    main()
