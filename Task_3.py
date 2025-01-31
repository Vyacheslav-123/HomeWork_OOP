# Задача №3:
with open('1.txt', 'r', encoding='utf-8') as file_1:
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['1.txt'] = count_1
with open('1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.read()

with open('2.txt', 'r', encoding='utf-8') as file_2:
    line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        line_2['2.txt'] = count_2
with open('2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.read()

with open('3.txt', 'r', encoding='utf-8') as file_3:
    line_3 = {}
    count_3 = 0
    for line in file_3.readlines():
        count_3 += 1
        line_3['3.txt'] = count_3
with open('3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.read()

join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])

with open('final_text.txt', 'w', encoding='utf-8') as file_result:
    for line in join:
        file_result.write(f'{join[0][0]}\n {join[0][1]}\n {text_2}\n {join[1][0]}\n {join[1][1]}\n {text_1}\n'
                          f'{join[2][0]}\n {join[2][1]}\n {text_3}\n')