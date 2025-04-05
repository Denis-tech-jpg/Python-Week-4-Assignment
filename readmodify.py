-- Question 1
# This script reads a text file, modifies its content, and writes the modified content to a new file.
def modify_text(text):

    return text.upper()

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        modified_content = modify_text(content)
        
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to '{output_file}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = 'input.txt'
output_filename = 'output.txt'

process_file(input_filename, output_filename)

-- Question 2

def read_user_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_user_file()

