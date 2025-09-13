"""Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.

def get_views_count(n: int) -> str:
    return """


def get_views_count(n: int) -> str:
    if n == 1 and n % 10 == 1 and n % 100 != 11 : # для 1, 21, 31... (кроме 11, 111)
        return f'{n} просмотр'
    if 2 <= n <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return f'{n} просмотра' 
    else:
        return f'{n} просмотров'

print(get_views_count(0)) 
print(get_views_count(5))   
print(get_views_count(11))  
print(get_views_count(12))  
print(get_views_count(2))
print(get_views_count(5))
print(get_views_count(111))
print(get_views_count(1))

#второй способ с any для объединения условий

def get_views_count_v2(n: int)-> str:
    b1 = n % 10 == 1 and n % 100 != 11
    b2 = 2 <= n % 10 <= 4 and (n % 100 < 12 or n % 100 > 14)

    if b1 or b2:
        return f'{n} просмотр' if n % 10 == 1 else f'{n} просмотра'
    return f'{n} просмотров'

print(get_views_count_v2(15))
print(get_views_count_v2(12))
print(get_views_count_v2(1))