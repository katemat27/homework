 #Соединить два словаря
def test_merge_two_dicts():
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }

    assert concat_dicts(developed_markets, emerging_markets) == {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }

def merge_dicts():
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    merged = {**developed_markets, **emerging_markets}
    assert merged == {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
        }
    return merged
    

result = merge_dicts()
print(result)