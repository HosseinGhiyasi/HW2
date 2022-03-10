
users_lst =[]
print("Enter number of users: ")
number_of_users = int(input())
for n in range(number_of_users):
    print("Enter user name:")
    name = input()
    print("Enter user age:")
    age = int(input())
    new_dict = {}
    new_dict['name'] = name
    new_dict['age'] = age
    users_lst.append(new_dict)

found = False
print("Enter a name to search:")
searched_name = input()
for dct in users_lst:
    if searched_name == dct.get('name'):
        print("user age is:", dct.get('age'))
        found = True

if found is False:
    print("user not found")

