import sys

def extract_names(input_file, output_file):
    with open(input_file, 'r') as f:
        emails = f.readlines()

    with open(output_file, 'w') as f:
        f.write("Name\tSurname\tE-mail\n")
        
        for email in emails:
            email = email.strip()
            if email:
                try:
                    name, domain = email.split('@')[0], email.split('@')[1]
                    surname = name.split('.')[1]
                    name = name.split('.')[0]
                    name = name.capitalize()
                    surname = surname.capitalize()
                    f.write(f"{name}\t{surname}\t{email}\n")
                except ValueError:
                    print(f"Warning: Skipping invalid email: {email}")

    print(f"Файл '{output_file}' успешно создан!")

def main():
    try:
        if len(sys.argv) != 3:
            raise Exception("Please provide the input file and output file as arguments.")
        
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        
        extract_names(input_file, output_file)

    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    main()
