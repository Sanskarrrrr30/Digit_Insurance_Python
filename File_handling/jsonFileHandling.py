# import json

# # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# #     data = json.load(file)
# #     print(data)

# # # changing json to dictionary
# # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# #     data = json.load(file)
# #     print(type(data))  # <class 'list'>
# #     first_row = data[0]
# #     print(first_row)
# #     print(type(first_row))  # <class 'dict'>

# # #changing dictionary to json
# person_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# with open("person.json", "w") as file:
#     json.dump(person_dict, file)
#     print("Dictionary has been written to person.json file.")
#     print(type(person_dict))  # <class 'dict'>
#     print(person_dict)

#saving as json file

import json
person_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open("person.json", "w") as file:
    json.dump(person_dict, file)
    print("Dictionary has been written to person.json file.")
    print(type(person_dict))  # <class 'dict'>
    print(person_dict)