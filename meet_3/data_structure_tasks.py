
#Соединить два списка в словарь
#def test_to_lists_to_dict():
#    keys = ["USA", "Russia", "France"]
#    income = [100, 10, 25]

#    assert two_lists_to_dict(keys, income) == {
#        "USA": 100,
#        "Russia": 10,
#        "France": 25
 #   }

def merge_dicts():
    keys = ["USA", "Russia", "France"]
    income = [100, 10, 25]
    result_dict =  dict(zip(keys, income))
    assert result_dict == {
        'USA': 100,
        'Russia': 10,
        'France': 25
        }
    return result_dict
result = merge_dicts()
print(result)


