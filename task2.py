list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for element in list_1:
    if element.isdigit():
        new_list.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+') or element.startswith('-')) and element[1:].isdigit():
        new_list.extend(['"', f'{element[0]}{int(element[1:]):02}', '"'])
    else:
        new_list.append(element)
list_2 = " ".join(new_list)
print(list_2)
