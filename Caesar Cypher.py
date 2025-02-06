import tkinter as tk

# Function to apply the Caesar Cipher
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    
    # Loop through each character in the input message
    for char in message.lower():
        if char == ' ':
            encrypted_text += char  # Preserve spaces
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

# Function to handle encryption on button click
def encrypt_text():
    text = text_entry.get()  # Get the input text from the entry field
    shift = int(shift_entry.get())  # Get the shift value from the entry field
    encrypted_text = caesar(text, shift)  # Call the caesar function
    result_label.config(text=f"Encrypted text: {encrypted_text}")  # Display the result

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption")

# Create and place the input labels and entry fields
text_label = tk.Label(root, text="Enter text to encrypt:")
text_label.pack()

text_entry = tk.Entry(root, width=40)
text_entry.pack()

shift_label = tk.Label(root, text="Enter shift value:")
shift_label.pack()

shift_entry = tk.Entry(root, width=10)
shift_entry.pack()

# Create the Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

# Create the result label
result_label = tk.Label(root, text="Encrypted text will appear here")
result_label.pack()

# Run the application
root.mainloop()