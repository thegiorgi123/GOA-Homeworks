# print("მოგესალმებით ჩვენს ბანკში!")
# print("დასაწყებად გაიარეთ რეგისტრაცია!")
# register = input("რეგისტრაციის დასაწყებად შემოიტანეთ სიტყვა: Registration               😊")
# register2 = "Registration"
# while register != register2:
#     register = input("რეგისტრაციის დაწყება ვერ მოხერხდა, სცადეთ ახლიდან!")
# print("რეგისტრაცია წარმატებით დაიწყო!")

# name = input("შემოიტანეთ თქვენი სახელი!:                            ")
# surname = input("შემოიტანეთ თქვენი გვარი!:                          ")


# email = input("შემოიტანეთ თქვენი ელ-ფოსტა!:                        ")
# password1 = input("შექმენით პაროლი!:      ")
# password2 = input("გაიმეორეთ თქვენი პაროლი!:      ")

# while password1 != password2:
#     password2 = input("პაროლი არასწორია, ცადეთ თავიდან!")
# print("რეგისტრაცია წარმატებით დასრულდა!")

# cards = ["Mastercard", "Amex"]
# choose_a_card = input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard, Amex!:          ")
# card1 = 1
# card2 = 2
# if choose_a_card == card1:
#     print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
#     print("შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)")

# if choose_a_card == card2:
#     print("თქვენი ანგარიშია:", "Amex", "400 GEL")
#     print("შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)")
    

# cards = input("აირჩიეთ სასურველი ბარათი: BOG(1), TBC(2), LibertyBank(3):    ")
# first = 1
# second = 2
# third = 3


# while cards > 3:
#     cards = int(input("აირჩიეთ სასურველი ბარათი ახლიდან!: BOG(1), TBC(2), LibertyBank(3):    "))

# while cards != first:
#     cards = input("შეტანილი ინფორმაცია არასწორია, სცადეთ ახლიდან!: BOG(1), TBC(2), BOL(3):    ")
# first = print("თქვენ აირჩიეთ Bank Of Georgia!")
# while cards != second:
#     cards = input("შეტანილი ინფორმაცია არასწორია, სცადეთ ახლიდან!: BOG(1), TBC(2), BOL(3):    ")
# second = print("თქვენ აირჩიეთ TBC - ბანკი")
# while cards != third:
#     cards = input("შეტანილი ინფორმაცია არასწორია, სცადეთ ახლიდან!: BOG(1), TBC(2), BOL(3):    ")
# third = print("თქვენ აირჩიეთ Bank Of Liberty!")

# while True:
#     user_input = input("გთხოვთ, შეიყვანეთ თვე (1-12): ")

#     if user_input.isdigit():
#         month = int(user_input)
#         if 1 <= month <= 12:
#             print(f"თქვენი არჩეული თვეა: {month}")
#             break 
#         else:
#             print("არასწორი თვე. გთხოვთ, შეიყვანეთ თვე 1-დან 12-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")


# cards = ["Mastercard", "Amex"]
# card1 = ["Aastercard", 40, "Dollar"]
# card2 = ["Amex", 1, "Gel"]

# chosen_card = (input("აირჩიეთ სასურველი ბარათი: Mastercard -1 , Amex - 2:     "))

# while chosen_card == 1:
#         print("ცადეთ ახლიდან!")
# print("თქვენ აირჩიეთ Mastercard")
# print("თქვენს ანგარიშზეა: ", card1[1], card1[2])

# while chosen_card == 2:
#     print("ცადეთ ახლიდან")
# print("თქვენ აირჩიეთ Amex")
# print("თქვენს ანგარიშზეა: ", card2[1], card2[2])

# while chosen_card > str(2):
#     print("ცადეთ ახლიდან")




# if choose_a_card == 1:
#     print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
#     balance1 = 450
#     print("შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)")
# elif choose_a_card == 2:
#     print("თქვენი ანგარიშია:", "Amex", "400 GEL")
#     balance2 = 400
#     print("შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)")
#     choose_next = input("აირჩიე შემდეგი მოქმედება: ")
#     if choose_next == '3': 
#         print("აირჩიე ვალუტა: Euro(1) USD(2)")
#         value = int(input("აირჩიე: ")) 
#         if value == 1:
#             new_balance2 = balance2 * 0.35
#         elif value == 2:
#             new_balance2 = balance2 * 0.36
#         print(f"თქვენი ახალი ბალანსია: {new_balance2} ვალუტაში")







# cards = ["Mastercard", "Amex"]
# card1 = ["Mastercard", 40, "Dollar"]
# card2 = ["Amex", 1, "Gel"]

# chosen_card = (input("აირჩიეთ სასურველი ბარათი: Mastercard -1 , Amex - 2:     "))

# def card_1(first):
#     while chosen_card == 1:
#         print("1")
#     print("თქვენ აირჩიეთ Mastercard, თქვენს ანგარიშზეა: ", card1[1], card1[2])










# choose_a_card = int(input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard(1), Amex(2)!: "))

# if choose_a_card == 1:
#     print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
#     balance1 = 450
#     while True:
#         print("შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)")
#         choose_next = input("აირჩიე შემდეგი მოქმედება: ")
#         if choose_next == '1':
#             print("შეთანხმების შემოსავალი!")
#         elif choose_next == '2':
#             print("გამოტანა განხორციელდა!")
#         elif choose_next == '3':
#             print("აირჩიე ვალუტა: Euro(1) USD(2)")
#             value = int(input("აირჩიე: "))
#             if value == 1:
#                 new_balance1 = balance1 * 0.9 
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} Euro")
#             elif value == 2:
#                 new_balance1 = balance1 * 0.85  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} USD")
#         else:
#             print("არასწორი არჩევანი! გთხოვთ, სცადეთ ისევ.")
#         continue_choice = input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ")
#         if continue_choice.lower() != 'კი':
#             break
# elif choose_a_card == 2:
#     print("თქვენი ანგარიშია:", "Amex", "400 GEL")
#     balance2 = 400
#     while True:
#         print("შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)")
#         choose_next = input("აირჩიე შემდეგი მოქმედება: ")
#         if choose_next == '1':
#             print("შეთანხმების შემოსავალი!")
#         elif choose_next == '2':
#             print("გამოტანა განხორციელდა!")
#         elif choose_next == '3':
#             print("აირჩიე ვალუტა: Euro(1) USD(2)")
#             value = int(input("აირჩიე: "))
#             if value == 1:
#                 new_balance2 = balance2 * 0.35 
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} Euro")
#             elif value == 2:
#                 new_balance2 = balance2 * 0.36  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} USD")
#         else:
#             print("არასწორი არჩევანი! გთხოვთ, სცადეთ ისევ.")
#         continue_choice = input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ")
#         if continue_choice.lower() != 'კი':
#             break
# else:
#     print("არასწორი ბარათის ტიპი აირჩიეთ.")




    
# while choose_a_card > 3:
#     print("")
# choose_a_card = input("ცადეთ ახლიდან!:   ")





# print("მოგესალმებით ჩვენს ბანკში!")
# print("დასაწყებად გაიარეთ რეგისტრაცია!")
# register = input("რეგისტრაციის დასაწყებად შემოიტანეთ სიტყვა: Registration               😊")
# register2 = "Registration"
# while register != register2:
#     register = input("რეგისტრაციის დაწყება ვერ მოხერხდა, სცადეთ ახლიდან!")
# print("რეგისტრაცია წარმატებით დაიწყო!")

# name = input("შემოიტანეთ თქვენი სახელი!:                            ")
# surname = input("შემოიტანეთ თქვენი გვარი!: ")
# while True:
#     user_input = input("გთხოვთ, შეიყვანეთ თვე (1-12): ")

#     if user_input.isdigit():
#         month = int(user_input)
#         if 1 <= month <= 12:
#             print(f"თქვენი არჩეული თვეა: {month}")
#             break 
#         else:
#             print("არასწორი თვე. გთხოვთ, შეიყვანეთ თვე 1-დან 12-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")
        

# while True:
#         user_input = input("გთხოვთ, შეიყვანეთ დაბადების დღე (01-31): ")
    
#         if user_input.isdigit() and len(user_input) == 2:
#             day = int(user_input)
#             if 1 <= day <= 31: 
#                 print(f"თქვენი არჩეული დაბადების დღეა: {user_input}")
#                 break
#             else:
#                 print("არასწორი დღე. გთხოვთ, შეიყვანეთ დღე 01-დან 31-მდე.")
#         else:
#             print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ ორი ციფრი (01-31).")
        
# import datetime

# while True:
#     user_input = input("შემოიტანეთ დაბადების წელი! (მაგ. 1900-2025): ")

#     if user_input.isdigit():
#         year = int(user_input)

#         current_year = datetime.datetime.now().year

#         if 1900 <= year <= current_year:
#             print(f"თქვენი არჩეული დაბადების წელი არის: {year}")
#             break 
#         else:
#             print(f"არასწორი წელი. გთხოვთ, შეიყვანოთ წელი 1900-დან {current_year}-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")

# email = input("შემოიტანეთ თქვენი ელ-ფოსტა!:                        ")
# password1 = input("შექმენით პაროლი!:      ")
# password2 = input("გაიმეორეთ თქვენი პაროლი!:      ")

# while password1 != password2:
#     password2 = input("პაროლი არასწორია, ცადეთ თავიდან!")
# print("რეგისტრაცია წარმატებით დასრულდა!")

# cards = ["Mastercard", "Amex"]
# choose_a_card = int(input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard(1), Amex(2)!:          "))

# def get_valid_input(prompt, valid_options):
#     while True:
#         choice = input(prompt)
#         if choice in valid_options:
#             return choice
#         else:
#             print("არასწორი არჩევანი! გთხოვთ, სცადეთ ისევ.")

# choose_a_card = get_valid_input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard(1), Amex(2)!: ", ['1', '2'])

# if choose_a_card == '1':
#     print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
#     balance1 = 450
#     while True:
#         choose_next = get_valid_input(
#             "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)\nაირჩიე შემდეგი მოქმედება: ",
#             ['1', '2', '3']
#         )
        
#         if choose_next == '1':
#             print
            
            
            
            
            
            
#         elif choose_next == '2':
#             print("გამოტანა განხორციელდა!")
#         elif choose_next == '3':
#             value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
#             if value == '1':
#                 new_balance1 = balance1 * 0.9  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} Euro")
#             elif value == '2':
#                 new_balance1 = balance1 * 0.85  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} USD")
        
#         continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
#         if continue_choice.lower() != 'კი':
#             break

# elif choose_a_card == '2':
#     print("თქვენი ანგარიშია:", "Amex", "400 GEL")
#     balance2 = 400
#     while True:
#         choose_next = get_valid_input(
#             "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3)\nაირჩიე შემდეგი მოქმედება: ",
#             ['1', '2', '3']
#         )
        
#         if choose_next == '1':
#             print("შეთანხმების შემოსავალი!")
#         elif choose_next == '2':
#             print("გამოტანა განხორციელდა!")
#         elif choose_next == '3':
#             value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
#             if value == '1':
#                 new_balance2 = balance2 * 0.35  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} Euro")
#             elif value == '2':
#                 new_balance2 = balance2 * 0.36  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} USD")
        
#         continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
#         if continue_choice.lower() != 'კი':
#             break

# else:
#     print("არასწორი ბარათის ტიპი აირჩიეთ.")






# print("მოგესალმებით ჩვენს ბანკში!")
# print("დასაწყებად გაიარეთ რეგისტრაცია!")
# register = input("რეგისტრაციის დასაწყებად შემოიტანეთ სიტყვა: Registration               😊")
# register2 = "Registration"
# while register != register2:
#     register = input("რეგისტრაციის დაწყება ვერ მოხერხდა, სცადეთ ახლიდან!")
# print("რეგისტრაცია წარმატებით დაიწყო!")

# name = input("შემოიტანეთ თქვენი სახელი!:                            ")
# surname = input("შემოიტანეთ თქვენი გვარი!: ")
# while True:
#     user_input = input("გთხოვთ, შეიყვანეთ თვე (1-12): ")

#     if user_input.isdigit():
#         month = int(user_input)
#         if 1 <= month <= 12:
#             print(f"თქვენი არჩეული თვეა: {month}")
#             break 
#         else:
#             print("არასწორი თვე. გთხოვთ, შეიყვანეთ თვე 1-დან 12-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")
        

# while True:
#         user_input = input("გთხოვთ, შეიყვანეთ დაბადების დღე (01-31): ")
    
#         if user_input.isdigit() and len(user_input) == 2:
#             day = int(user_input)
#             if 1 <= day <= 31: 
#                 print(f"თქვენი არჩეული დაბადების დღეა: {user_input}")
#                 break
#             else:
#                 print("არასწორი დღე. გთხოვთ, შეიყვანეთ დღე 01-დან 31-მდე.")
#         else:
#             print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ ორი ციფრი (01-31).")
        
# import datetime

# while True:
#     user_input = input("შემოიტანეთ დაბადების წელი! (მაგ. 1900-2025): ")

#     if user_input.isdigit():
#         year = int(user_input)

#         current_year = datetime.datetime.now().year

#         if 1900 <= year <= current_year:
#             print(f"თქვენი არჩეული დაბადების წელი არის: {year}")
#             break 
#         else:
#             print(f"არასწორი წელი. გთხოვთ, შეიყვანოთ წელი 1900-დან {current_year}-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")

# email = input("შემოიტანეთ თქვენი ელ-ფოსტა!:                        ")
# password1 = input("შექმენით პაროლი!:      ")
# password2 = input("გაიმეორეთ თქვენი პაროლი!:      ")

# while password1 != password2:
#     password2 = input("პაროლი არასწორია, ცადეთ თავიდან!")
# print("რეგისტრაცია წარმატებით დასრულდა!")






# print("მოგესალმებით ჩვენს ბანკში!")
# print("დასაწყებად გაიარეთ რეგისტრაცია!")
# register = input("რეგისტრაციის დასაწყებად შემოიტანეთ სიტყვა: Registration               😊")
# register2 = "Registration"
# while register != register2:
#     register = input("რეგისტრაციის დაწყება ვერ მოხერხდა, სცადეთ ახლიდან!")
# print("რეგისტრაცია წარმატებით დაიწყო!")

# name = input("შემოიტანეთ თქვენი სახელი!:                            ")
# surname = input("შემოიტანეთ თქვენი გვარი!: ")
# while True:
#     user_input = input("გთხოვთ, შეიყვანეთ თვე (1-12): ")

#     if user_input.isdigit():
#         month = int(user_input)
#         if 1 <= month <= 12:
#             print(f"თქვენი არჩეული თვეა: {month}")
#             break 
#         else:
#             print("არასწორი თვე. გთხოვთ, შეიყვანეთ თვე 1-დან 12-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")
        

# while True:
#         user_input = input("გთხოვთ, შეიყვანეთ დაბადების დღე (01-31): ")
    
#         if user_input.isdigit() and len(user_input) == 2:
#             day = int(user_input)
#             if 1 <= day <= 31: 
#                 print(f"თქვენი არჩეული დაბადების დღეა: {user_input}")
#                 break
#             else:
#                 print("არასწორი დღე. გთხოვთ, შეიყვანეთ დღე 01-დან 31-მდე.")
#         else:
#             print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ ორი ციფრი (01-31).")
        
# import datetime

# while True:
#     user_input = input("შემოიტანეთ დაბადების წელი! (მაგ. 1900-2025): ")

#     if user_input.isdigit():
#         year = int(user_input)

#         current_year = datetime.datetime.now().year

#         if 1900 <= year <= current_year:
#             print(f"თქვენი არჩეული დაბადების წელი არის: {year}")
#             break 
#         else:
#             print(f"არასწორი წელი. გთხოვთ, შეიყვანოთ წელი 1900-დან {current_year}-მდე.")
#     else:
#         print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")

# email = input("შემოიტანეთ თქვენი ელ-ფოსტა!:                        ")
# password1 = input("შექმენით პაროლი!:      ")
# password2 = input("გაიმეორეთ თქვენი პაროლი!:      ")

# while password1 != password2:
#     password2 = input("პაროლი არასწორია, ცადეთ თავიდან!")
# print("რეგისტრაცია წარმატებით დასრულდა!")

# cards = ["Mastercard", "Amex"]

# def get_valid_input(prompt, valid_options):
#     while True:
#         choice = input(prompt)
#         if choice in valid_options:
#             return choice
#         else:
#             print("არასწორი არჩევანი! გთხოვთ, სცადეთ ისევ.")


# def get_valid_amount(prompt):
#     while True:
#         try:
#             amount = float(input(prompt))
#             if amount > 0:
#                 return amount
#             else:
#                 print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
#         except ValueError:
#             print("გთხოვთ, შეიყვანოთ gültური რიცხვი.")

# choose_a_card = get_valid_input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard(1), Amex(2)!: ", ['1', '2'])

# if choose_a_card == '1':
#     print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
#     balance1 = 450
#     while True:
#         choose_next = get_valid_input(
#             "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3), სხვა ანგარიშზე გადაცემა(4)\nაირჩიე შემდეგი მოქმედება: ",
#             ['1', '2', '3', '4']
#         )
        
#         if choose_next == '1':  
#             deposit_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ დაემატოს ანგარიშზე: ")
#             balance1 += deposit_amount
#             print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")

#         elif choose_next == '2':  
#             withdraw_ammount = get_valid_amount("შეიყვანეთ თანხა, რომლის გამოტანაც გსურთ: ")
#             balance1 -= withdraw_ammount
#             print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")

#         elif choose_next == '3':  
#             value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
#             if value == '1':
#                 new_balance1 = balance1 * 0.9  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} Euro")
#             elif value == '2':
#                 new_balance1 = balance1 * 0.85  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} USD")

#         elif choose_next == '4':  
#             transfer_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გადარიცხოთ: ")
#             if transfer_amount <= balance1:
#                 balance1 -= transfer_amount
#                 print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")
#                 print(f"გადაირიცხა {transfer_amount} Dollars")
#             else:
#                 print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

#         continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
#         if continue_choice.lower() != 'კი':
#             break

# elif choose_a_card == '2':
#     print("თქვენი ანგარიშია:", "Amex", "400 GEL")
#     balance2 = 400
#     while True:
#         choose_next = get_valid_input(
#             "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3), სხვა ანგარიშზე გადაცემა(4)\nაირჩიე შემდეგი მოქმედება: ",
#             ['1', '2', '3', '4']
#         )
        
#         if choose_next == '1': 
#             deposit_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ დაემატოს ანგარიშზე: ")
#             balance2 += deposit_amount
#             print(f"თქვენი ახალი ბალანსია: {balance2} GEL")

#         elif choose_next == '2':  
#             withdraw_ammount = get_valid_amount("შეიყვანეთ თანხა, რომლის გამოტანაც გსურთ: ")
#             balance2 -= withdraw_ammount
#             print(f"თქვენი ახალი ბალანსია: {balance2} GEL")

            
#         elif choose_next == '3':  
#             value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
#             if value == '1':
#                 new_balance2 = balance2 * 0.35  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} Euro")
#             elif value == '2':
#                 new_balance2 = balance2 * 0.36  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} USD")

#         elif choose_next == '4':  
#             transfer_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გადარიცხოთ: ")
#             if transfer_amount <= balance2:
#                 balance2 -= transfer_amount
#                 print(f"თქვენი ახალი ბალანსია: {balance2} GEL")
#                 print(f"გადაირიცხა {transfer_amount} GEL")
#             else:
#                 print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

#         continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
#         if continue_choice.lower() != 'კი':
#             break

# else:
#     print("არასწორი ბარათის ტიპი აირჩიეთ.")







# def get_valid_input(prompt, valid_options):
#     while True:
#         choice = input(prompt)
#         if choice in valid_options:
#             return choice
#         else:
#             print("არასწორი არჩევანი! გთხოვთ, სცადეთ ისევ.")


# def get_valid_amount(prompt):
#     while True:
#         try:
#             amount = float(input(prompt))
#             if amount > 0:
#                 return amount
#             else:
#                 print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
#         except ValueError:
#             print("გთხოვთ, შეიყვანოთ gültური რიცხვი.")

# choose_a_card = get_valid_input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard(1), Amex(2)!: ", ['1', '2'])

# if choose_a_card == '1':
#     print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
#     balance1 = 450
#     while True:
#         choose_next = get_valid_input(
#             "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3), სხვა ანგარიშზე გადაცემა(4)\nაირჩიე შემდეგი მოქმედება: ",
#             ['1', '2', '3', '4']
#         )
        
#         if choose_next == '1':  
#             deposit_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ დაემატოს ანგარიშზე: ")
#             balance1 += deposit_amount
#             print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")

#         elif choose_next == '2':  
#             withdrawal_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გამოიტანოთ: ")
#             if withdrawal_amount <= balance1:
#                 balance1 -= withdrawal_amount
#                 print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")
#                 print(f"გამოიტანეთ {withdrawal_amount} Dollars")
#             else:
#                 print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

#         elif choose_next == '3': 
#             value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
#             if value == '1':
#                 new_balance1 = balance1 * 0.9 
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} Euro")
#             elif value == '2':
#                 new_balance1 = balance1 * 0.85  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance1} USD")

#         elif choose_next == '4':  
#             send_name = str(input("მიმღების სახელი:   "))
#             send_surname = str(input("მიმღების გვარი:   "))
#             send_num = int(input("მიმღების პირადი ნომერი:   "))
#             transfer_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გადარიცხოთ: ")
#             if transfer_amount <= balance1:
#                 balance1 -= transfer_amount
#                 print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")
#                 print(f"გადაირიცხა {transfer_amount} Dollars")
#             else:
#                 print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

#         continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
#         if continue_choice.lower() != 'კი':
#             break

# elif choose_a_card == '2':
#     print("თქვენი ანგარიშია:", "Amex", "400 GEL")
#     balance2 = 400
#     while True:
#         choose_next = get_valid_input(
#             "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3), სხვა ანგარიშზე გადაცემა(4)\nაირჩიე შემდეგი მოქმედება: ",
#             ['1', '2', '3', '4']
#         )
        
#         if choose_next == '1':  
#             deposit_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ დაემატოს ანგარიშზე: ")
#             balance2 += deposit_amount
#             print(f"თქვენი ახალი ბალანსია: {balance2} GEL")

#         elif choose_next == '2':  
#             withdrawal_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გამოიტანოთ: ")
#             if withdrawal_amount <= balance2:
#                 balance2 -= withdrawal_amount
#                 print(f"თქვენი ახალი ბალანსია: {balance2} GEL")
#                 print(f"გამოიტანეთ {withdrawal_amount} GEL")
#             else:
#                 print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

#         elif choose_next == '3': 
#             value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
#             if value == '1':
#                 new_balance2 = balance2 * 0.35  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} Euro")
#             elif value == '2':
#                 new_balance2 = balance2 * 0.36  
#                 print(f"თქვენი ახალი ბალანსია: {new_balance2} USD")

#         elif choose_next == '4':
#             send_name = str(input("მიმღების სახელი:   "))
#             send_surname = str(input("მიმღების გვარი:   "))
#             send_num = int(input("მიმღების პირადი ნომერი:   "))
#             transfer_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გადარიცხოთ: ")
#             if transfer_amount <= balance2:
#                 balance2 -= transfer_amount
#                 print(f"თქვენი ახალი ბალანსია: {balance2} GEL")
#                 print(f"გადაირიცხა {transfer_amount} GEL")
#             else:
#                 print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

#         continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
#         if continue_choice.lower() != 'კი':
#             break

# else:
#     print("არასწორი ბარათის ტიპი აირჩიეთ.")
















# print("--------------------------------------------------------------------------")


    
print("მოგესალმებით ჩვენს ბანკში!")
print("დასაწყებად გაიარეთ რეგისტრაცია!")
register = input("რეგისტრაციის დასაწყებად შემოიტანეთ სიტყვა: Registration               😊")
register2 = "Registration"
while register != register2:
    register = input("რეგისტრაციის დაწყება ვერ მოხერხდა, სცადეთ ხელახლა!")
print("რეგისტრაცია წარმატებით დასრულდა!")

name = input("შემოიტანეთ თქვენი სახელი!:                            ")
surname = input("შემოიტანეთ თქვენი გვარი!: ")
while True:
    user_input = input("გთხოვთ, შეიყვანეთ თქვენი თვე (1-12): ")

    if user_input.isdigit():
        month = int(user_input)
        if 1 <= month <= 12:
            print(f"თქვენი არჩეული თვეა: {month}")
            break 
        else:
            print("არასწორი თვე. გთხოვთ, შეიყვანეთ თვე 1-დან 12-მდე.")
    else:
        print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")
        

while True:
        user_input = input("გთხოვთ, შეიყვანეთ დაბადების დღე (01-31): ")
    
        if user_input.isdigit() and len(user_input) == 2:
            day = int(user_input)
            if 1 <= day <= 31: 
                print(f"თქვენი არჩეული დაბადების დღეა: {user_input}")
                break
            else:
                print("არასწორი დღე. გთხოვთ, შეიყვანეთ დღე 01-დან 31-მდე.")
        else:
            print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ ორი ციფრი (01-31).")
        
import datetime

while True:
    user_input = input("შემოიტანეთ დაბადების წელი! (მაგ. 1900-2025): ")

    if user_input.isdigit():
        year = int(user_input)

        current_year = datetime.datetime.now().year

        if 1900 <= year <= current_year:
            print(f"თქვენი არჩეული დაბადების წელი არის: {year}")
            break 
        else:
            print(f"არასწორი წელი. გთხოვთ, შეიყვანოთ წელი 1900-დან {current_year}-მდე.")
    else:
        print("არასწორი მონაცემი, გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")

email = input("შემოიტანეთ თქვენი ელ-ფოსტა!:                        ")
password1 = input("შექმენით პაროლი!:      ")
password2 = input("გაიმეორეთ  პაროლი!:      ")

while password1 != password2:
    password2 = input("პაროლი არასწორია, ცადეთ თავიდან!")
print("რეგისტრაცია წარმატებით დასრულდა!")

cards = ["Mastercard", "Amex"]

def get_valid_input(prompt, valid_options):
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print("არასწორი არჩევანი! გთხოვთ, სცადეთ ისევ.")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
        except ValueError:
            print("გთხოვთ, შეიყვანოთ სწორი რიცხვი.")

choose_a_card = get_valid_input("აირჩიეთ ბარათის ტიპი, შესაძლო ვარიანტებია: Mastercard(1), Amex(2)!: ", ['1', '2'])

if choose_a_card == '1':
    print("თქვენი ანგარიშია:", "Mastercard(1)", "450 Dollars(2)")
    balance1 = 450
    while True:
        choose_next = get_valid_input(
            "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3), სხვა ანგარიშზე გადაცემა(4)\nაირჩიე შემდეგი მოქმედება: ",
            ['1', '2', '3', '4']
        )
        
        if choose_next == '1':  
            deposit_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ დაემატოს ანგარიშზე: ")
            balance1 += deposit_amount
            print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")

        elif choose_next == '2':  
            withdrawal_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გამოიტანოთ: ")
            if withdrawal_amount <= balance1:
                balance1 -= withdrawal_amount
                print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")
                print(f"გამოიტანეთ {withdrawal_amount} Dollars")
            else:
                print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

        elif choose_next == '3':  
            value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
            if value == '1':
                new_balance1 = balance1 * 0.9  
                print(f"თქვენი ახალი ბალანსია: {new_balance1} Euro")
            elif value == '2':
                new_balance1 = balance1 * 0.85  
                print(f"თქვენი ახალი ბალანსია: {new_balance1} USD")

        elif choose_next == '4':  
            send_name = str(input("მიმღების სახელი:   "))
            send_surname = str(input("მიმღების გვარი:   "))
            send_num = int(input("მიმღების პირადი ნომერი:   "))
            transfer_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გადარიცხოთ: ")
            if transfer_amount <= balance1:
                balance1 -= transfer_amount
                print(f"თქვენი ახალი ბალანსია: {balance1} Dollars")
                print(f"გადაირიცხა {transfer_amount} Dollars")
            else:
                print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")


        continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
        if continue_choice.lower() != 'კი':
            print("მადლობა, რომ სარგებლობთ ჩვენი ბანკით!")
            break

elif choose_a_card == '2':
    print("თქვენი ანგარიშია:", "Amex", "400 GEL")
    balance2 = 400
    while True:
        choose_next = get_valid_input(
            "შეგიძლიათ განახორციელოთ შემდეგი მოქმედებები: შეტანა(1), გამოტანა(2), სხვა ვალუტაში გადაცვლა(3), სხვა ანგარიშზე გადაცემა(4)\nაირჩიე შემდეგი მოქმედება: ",
            ['1', '2', '3', '4']
        )
        
        if choose_next == '1': 
            deposit_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ დაემატოს ანგარიშზე: ")
            balance2 += deposit_amount
            print(f"თქვენი ახალი ბალანსია: {balance2} GEL")

        elif choose_next == '2':  
            withdrawal_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გამოიტანოთ: ")
            if withdrawal_amount <= balance2:
                balance2 -= withdrawal_amount
                print(f"თქვენი ახალი ბალანსია: {balance2} Dollars")
                print(f"გამოიტანეთ {withdrawal_amount} Dollars")
            else:
                print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

        elif choose_next == '3':  
            value = get_valid_input("აირჩიე ვალუტა: Euro(1) USD(2): ", ['1', '2'])
            if value == '1':
                new_balance2 = balance2 * 0.35  
                print(f"თქვენი ახალი ბალანსია: {new_balance2} Euro")
            elif value == '2':
                new_balance2 = balance2 * 0.36  
                print(f"თქვენი ახალი ბალანსია: {new_balance2} USD")

        elif choose_next == '4':  
            send_name = str(input("მიმღების სახელი:   "))
            send_surname = str(input("მიმღების გვარი:   "))
            send_num = int(input("მიმღების პირადი ნომერი:   "))
            transfer_amount = get_valid_amount("შეიყვანეთ თანხა, რომელიც გსურთ გადარიცხოთ: ")
            if transfer_amount <= balance2:
                balance2 -= transfer_amount
                print(f"თქვენი ახალი ბალანსია: {balance2} Dollars")
                print(f"გადაირიცხა {transfer_amount} Dollars")
            else:
                print("გთხოვთ, შეამოწმოთ თქვენი ბალანსი, საკმარისი თანხა არ არის.")

        continue_choice = get_valid_input("გსურთ გააგრძელოთ მოქმედება? (კი/არა): ", ['კი', 'არა'])
        if continue_choice.lower() != 'კი':
            print("მადლობა, რომ სარგებლობთ ჩვენი ბანკით!")
            break

else:
    print("არასწორი ბარათის ტიპი აირჩიეთ.")

# send_name = str(input("მიმღების სახელი:   "))
#         send_surname = str(input("მიმღების გვარი:   "))
#         send_num = int(input("მიმღების პირადი ნომერი:   "))