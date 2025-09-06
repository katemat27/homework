"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]


def get_pct_growth(s: list[float]) -> list[float]:
    return []
"""
massiv = [100, 150, 300, 400]
def get_pct_growth(massiv: list[float]) -> list[str]:
    if not massiv:
        return[]
    result = [None]
    for i in range(1, len(massiv)):
        growth = ((massiv[i] - massiv[i - 1]) / massiv[i - 1]) * 100
        result.append(f"{round(growth)}%")
    return result
result = get_pct_growth(massiv)
print(result)
