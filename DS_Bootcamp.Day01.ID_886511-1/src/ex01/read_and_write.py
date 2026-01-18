def convert_csv_to_tsv(input_file, output_file):

    def parse_line(line):
        result = []
        field = ''
        in_quotes = False

        for char in line:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                result.append(field)
                field = ''
            else:
                field += char

        result.append(field)
        return result

    with open(input_file, 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()

    with open(output_file, 'w', encoding='utf-8') as tsv_file:
        for line in lines:
            parsed_line = parse_line(line.strip())
            tsv_line = '\t'.join(parsed_line)
            tsv_file.write(tsv_line + '\n')

if __name__ == "__main__":
    input_csv = "ds.csv"
    output_tsv = "ds.tsv"

    convert_csv_to_tsv(input_csv, output_tsv)
