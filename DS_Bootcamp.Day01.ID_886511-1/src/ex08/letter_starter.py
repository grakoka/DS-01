import sys

def find_name_by_email(email, employees_file):
    with open(employees_file, 'r') as f:
        f.readline()
        
        for line in f:
            name, surname, email_in_file = line.strip().split('\t')
            if email_in_file == email:
                return name, surname
    return None, None

def generate_letter(email, employees_file):
    name, surname = find_name_by_email(email, employees_file)
    
    if name and surname:
        letter = f"Dear {name}, welcome to our team!"
        print(letter)
    else:
        print(f"Email {email} not found in the employees list.")

def main():
    try:
        if len(sys.argv) != 3:
            raise Exception("Please provide the email and the employees file as arguments.")
        
        email = sys.argv[1]
        employees_file = sys.argv[2]
        
        generate_letter(email, employees_file)
    
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    main()