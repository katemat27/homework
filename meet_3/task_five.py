def test_fill_missed_years():
    """
        Заполнить пропущенные значения средним арифметическим двух соседних значений.
        Например, если в 2015 году значение равно 50, в 2018 - 80, 
        то в 2016 должно быть 60, в 2017 - 70
    """
    yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }

    assert fill_missed_years(yearly_sales) == {
        "2015": 50,
        "2016": 55,
        "2017": 60,
        "2018": 65,
        "2019": 120,
        "2020": 130,
        "2021": 140,
        "2022": 150,
        "2023": 160,
        "2024": 180,
        "2025": 200
    }


_sales_data = [
    {
        "category": "dairy products",
        "product": "milk",
        "price_rub": 100,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "cream",
        "price_rub": 290,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "yogurt",
        "price_rub": 50,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "white_bread",
        "price_rub": 60,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "black_bread",
        "price_rub": 55,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "water",
        "price_rub": 90,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "apple_juice",
        "price_rub": 300,
        "count": 1
    }
]


def test_get_distinct_categories():
    """
        Вернуть множество уникальных категорий товаров
        Воспользоваться set comprehension (по аналогии с list/dict comprehension)
    """

    assert get_distinct_categories(_sales_data) == {
        "dairy products", "bakery", "drinks"}


def test_sum_category_as_tuples():
    """
        Показать сумму покупок по категориями. Отсортировать категории по возрастанию суммы
    """
    actual = get_sorted_category_sum(_sales_data)
    assert actual == [("bakery", 115),
                      ("drinks", 390),
                      ("dairy products", 440),
                      ]
