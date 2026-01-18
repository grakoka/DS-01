def to_dictionary():
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

    countries_dict = {}

    for country,value in list_of_tuples:
        if value not in countries_dict:
            countries_dict[value] = []
        countries_dict[value].append(country)    

    for value, countries in countries_dict.items():
        for country in countries:
            print(f"'{value}' : '{country}'")

if __name__  == '__main__':
    to_dictionary()            
