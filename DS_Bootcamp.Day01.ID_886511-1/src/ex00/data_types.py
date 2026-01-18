def data_types():
    int_var = 42
    str_var = 'Hello, world!'
    float_var = 3.14
    bool_var = True
    list_var = [1, 2, 3]
    dict_var = {'key': 'value'}
    tuple_var = (1, 2, 3)
    set_var = {1, 2, 3}

    print(f'[{int.__name__}, {str.__name__}, {float.__name__}, {bool.__name__},'
          f'{list.__name__}, {dict.__name__}, {tuple.__name__}, {set.__name__}]')

if __name__ == '__main__':
     data_types()   
           
  