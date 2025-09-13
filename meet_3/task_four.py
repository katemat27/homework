#def test_sum_value_of_the_same_key_kinds():
 ####monthly_sales = {
     #   "Jan_2020": 100,
      #  "Feb_2020": 90,
       # "Mar_2020": 15,
        #"Jan_2021": 10,
       ###Oct_2023": 12
  #  }
   # assert to_yearly_sales(monthly_sales) == {
    #    "2020": 205,
     #   "2021": 60,
      #  "2022": 5,
       # "2023": 24
    #}

def to_yeaerly_sales(monthly_sales):
    yearly_sales = {}
    for month_key, sales in monthly_sales.items():
        year = month_key.split('_')[-1]
        if year in yearly_sales:
            yearly_sales[year] += sales
        else:
            yearly_sales[year] = sales
        return yearly_sales

def sum_value():
    monthly_sales = {
        "Jan_2020": 100,
        "Feb_2020": 90,
        "Mar_2020": 15,
        "Jan_2021": 10,
        "Feb_2021": 50,
        "Mar_2022": 5,
        "Sep_2023": 12,
        "Oct_2023": 12
        }
    yearly_sales = to_yeaerly_sales(monthly_sales)
    assert  yearly_sales == {
        "2020": 205,
        "2021": 60,
        "2022": 5,
        "2023": 24
    }
    return yearly_sales

result = sum_value()
print(result)
    
