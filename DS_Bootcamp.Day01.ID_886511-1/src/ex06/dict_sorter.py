list_of_tuples = [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
]

def create_country_dict():
    country_dict = {}
    for country, number in list_of_tuples:
        try:
            country_dict[country] = int(number)
        except ValueError:
            print(f"Warning: Invalid number '{number}' for country '{country}', skipping...")
    return country_dict

def main():
    country_dict = create_country_dict()
    
    if not country_dict:
        print("Error: No valid data to process.")
        return

    sorted_countries = sorted(country_dict.items(), key=lambda x: (-x[1], x[0]))
    for country, _ in sorted_countries:
        print(country)

if __name__ == "__main__":
    main()
