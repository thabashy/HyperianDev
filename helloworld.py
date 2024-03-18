import translators as ts

# Define a function to check if the input contains only text (letters)
def is_text_only(input_string):
    return input_string.isalpha()

# Loop to continuously accept input until the user enters text only
while True:
    # Accept input from the user
    user_input = input("Please enter some text (or type 'exit' to stop): ")

    # Check if the user wants to exit the loop
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Check if the input is text only
    if is_text_only(user_input):
        print("You entered text only.")

        # print inputted text
        print(f"The input is: {user_input}")

        # Exit the loop after processing the text input
        break
    else:
        print("Your input contains non-text characters. Please try again.")