def get_student_info(fullname, group, grades):
    sred = sum(grades) / len(grades) if grades else 0
    simvol = '+++' if len(grades) >= 7 and sred >= 3.0 else '---'
    print(f'''{simvol} {fullname[:1]}. {fullname.split()[1]}, группа {{{group}}} 
Выполнено лабораторных работ: {len(grades)}
Средний балл: {sred:.1f}''')