with open('resources/parse.txt', 'r', encoding='utf-8') as f:
    lines: str = f.readlines()

for line in lines:
    splitted_line = line.replace('\n', '').split(';')
    print(f'add(new TaxBaseInfo("{splitted_line[0]}", AIRPORT_INFO_TJM, {splitted_line[2].replace(" ", "").replace(",", ".")}f));')
    print(f'add(new TaxBaseInfo("{splitted_line[0]}", AIRPORT_INFO_LED, {splitted_line[3].replace(" ", "").replace(",", ".")}f));')
    print(f'add(new TaxBaseInfo("{splitted_line[0]}", AIRPORT_INFO_NOJ, {splitted_line[4].replace(" ", "").replace(",", ".")}f));')

