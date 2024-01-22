from cryptography.fernet import Fernet


# Function to read key from file
def read_key_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()


# Function to process the file based on user's choice
def process_file(filename, cipher, operation):
    mode = 'encrypt' if operation == 'E' else 'decrypt'
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()

        if operation == 'E':
            processed_data = cipher.encrypt(file_data)
            output_filename = filename + '.encrypted'
        else:
            processed_data = cipher.decrypt(file_data)
            output_filename = filename + '.decrypted'

        with open(output_filename, 'wb') as output_file:
            output_file.write(processed_data)

        print(f"File successfully {mode}ed: {output_filename}")

    except Exception as e:
        print(f"An error occurred while trying to {mode} the file: {e}")


key = read_key_from_file('key.file')
cipher = Fernet(key)

file_to_process = input('What is the name of the file: ')
action = input('Do you want to encrypt or decrypt? (E/D): ')

if action in ['E', 'D']:
    process_file(file_to_process, cipher, action)
else:
    print("Please input a valid response (E for encrypt, D for decrypt)")
