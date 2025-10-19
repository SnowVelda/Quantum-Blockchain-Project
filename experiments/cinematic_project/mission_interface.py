class TimeMachine:
    def __init__(self):
        self.year = 2023
        self.location = "Present"

    def travel(self, year):
        self.year = year
        print(f"Time Machine has traveled to {year}")

    def get_location(self):
        return self.location

class EchoPrime:
    def __init__(self):
        self.voice = "Default Voice"
        self.time_machine = TimeMachine()

    def speak(self, message):
        print(f"Echo Prime ({self.voice}): {message}")

    def set_voice(self, voice):
        self.voice = voice
        print(f"Voice set to {voice}")

class Dashboard:
    def __init__(self, echo_prime):
        self.echo_prime = echo_prime

    def display(self):
        print("Time Machine Dashboard")
        print(f"Year: {self.echo_prime.time_machine.year}")
        print(f"Location: {self.echo_prime.time_machine.get_location()}")
        print(f"Voice: {self.echo_prime.voice}")

def main():
    echo_prime = EchoPrime()
    dashboard = Dashboard(echo_prime)

    while True:
        print("\nOptions Menu:")
        print("1. Travel through time")
        print("2. Change voice")
        print("3. Display dashboard")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            year = int(input("Enter year to travel to: "))
            echo_prime.time_machine.travel(year)
        elif choice == "2":
            voice = input("Enter voice (e.g., Dean, Tamera, Deanna): ")
            echo_prime.set_voice(voice)
        elif choice == "3":
            dashboard.display()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

        echo_prime.speak("Ready for next command.")

if __name__ == "__main__":
    main()
