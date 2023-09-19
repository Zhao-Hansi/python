list_a = [1, 3, 4, 2]
list_b = ["北京", "上海", "广州", "深圳"]
temp_list = list(zip(list_a, list_b))
temp_list = sorted(temp_list, reverse=True)
result_dict = dict(temp_list)
print(result_dict)