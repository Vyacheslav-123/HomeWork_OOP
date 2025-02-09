import glob

def counting_lines(file_list, lines_len):
    lines_len = {}
    for file in file_list:
        with open(file, 'r', encoding = 'utf-8') as text:  
            count = 0
            for line in text.readlines():
                count += 1
                lines_len[file] = count
    return lines_len


def sorting_text(some_dict):
    file_list_2 = []
    sorted_lines_len = sorted(some_dict.items(), key=lambda x: x[1])               
    for i, y in sorted_lines_len:
          file_list_2.append(i)
    return file_list_2, sorted_lines_len
       
       
def final_file_print():
    file_count = []
    i_count = []
    my_lines_len = {}
    files2, sorted_lines_len = sorting_text(counting_lines(glob.glob('*txt'), my_lines_len))
    with open('output-file.txt', 'w', encoding='utf-8') as output_file:
        for file in files2:
                    for i in sorted_lines_len:
                            with open(file, 'r', encoding='utf-8') as input_file:
                                 if file not in file_count and i not in i_count:
                                    file_count.append(file)
                                    i_count.append(i)
                                    output_file.write(f'{i[0]}\n{i[1]}\n{input_file.read()}')

final_file_print()

 
            