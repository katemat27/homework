"""
    Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
    Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
    "Иsвtrан Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"

def clean_name(fio: str) -> str:
    return """

name = 'Иsвtrан Ив^%ан Ива?но)вич'
def clean_name(fio: str) -> str: # fio = иsвtrан ив^%ан ива?но)вич'
    r = [s for s in fio if s in "абвгдежзвылоаджыводалывд"]
    s = ""
    s.join()
    join("", r)
    return "".join(r)



    cleaned = ''
    for char in fio:
        if s in "абвгдежзвылоаджыводалывд":
            cleaned += char  
    return cleaned

if __name__ == "__main__":    
    result= clean_name(name)
    print(f'До: {name}')
    print(f'После: {result}')

test_cases = ['Матуbbb@сеb$$вичx ЕкаTrf@ntтерина', 'Серг@ей Серге!евич','!@#$%^&*()']

for test in test_cases:
    cleaned = clean_name(test)
    print(f'{test} -> {cleaned}')