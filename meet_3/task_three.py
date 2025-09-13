#Отсортировать словарь по убыванию

#def test_sort_dict_values():
#    d = {
#        "USA": 100,
#       "Japan": 90,
 #       "France": 25,
 #       "China": 80,
  #      "India": 50,
#        "Russia": 5
  #  }
#   assert sort_dict_values(d) == {
 #       "USA": 100,
 #       "Japan": 90,
 #       "China": 80,
  #      "India": 50,
  #      "France": 25,
 #       "Russia": 5
 #   }

def sort_dict_values():
    d = {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    sorted_country = sorted(d.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_country)
    assert sorted_dict  == {
        "USA": 100,
        "Japan": 90,
        "China": 80,
        "India": 50,
        "France": 25,
        "Russia": 5
    }
    return sorted_dict

result = sort_dict_values()
print(result)
