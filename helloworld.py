import translators as ts

# Define a function to check if the input contains only text (letters)
def is_text_only(input_string):
    return input_string.isalpha()

# Define a function to translate text to French using the correct function
def translate_to_french(input_text):
    return ts.translate_text(input_text, translator='google', to_language='fr')

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


        # Translate the input to French
        translated_text = translate_to_french(user_input)
        print(f"The translated text in French is: {translated_text}")

        # Exit the loop after processing the text input
        break
    else:
        print("Your input contains non-text characters. Please try again.")