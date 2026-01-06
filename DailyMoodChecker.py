#DailyMoodChecker
# Greeting Mood Program
# This program asks for the user's name and mood
# then prints a friendly greeting message

name = input("Enter your name: ")
mood = input("How are you feeling today? (happy or sad): ")

print("\n--- Greeting Message ---")

if mood == "happy":
    print("Hi", name + "!")
    print("Keep smiling and enjoy your day!")
    print("Stay positive and spread happiness 😊")
else:
    print("Hi", name + "!")
    print("It's okay to feel sad sometimes.")
    print("Keep going and have a better day ahead 💙")


print("\nThank you for using the program!")
