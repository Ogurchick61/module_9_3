first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first) - len(second) for first, second in
                zip(first, second))

second_result = (len(first[i]) == len(second[i]) for i in
                 range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
