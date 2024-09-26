# N1.
birth_year = input("რომელ წელს ხართ დაბადებული?: ")

print("თქვენი ასაკია", int(2024) - int(birth_year))

#N2.

length_of_rectangle = input("ოთხკუთხედის ერთი გვერდის სიგრძეა: ")
length_of_rectangle2 = input("ოთხკუთხედის მეორე გვერდის სიგრძეა: ")
print("ოთხკუთხედის პერიმეტრია: ", int(length_of_rectangle)*int(length_of_rectangle2))
print("ოთხკუთხედის პერიმეტრია: ", int(2)*int(length_of_rectangle+length_of_rectangle2))

#N3. 

the_distance = input("მანძილი შენი სახლიდან სკოლამზე კილომეტრებში არის: ")
print("შენი სახლიდან სკოლამდე მანძილი მეტრებში არის: ", int(the_distance)*int(1000), "მეტრი")
print("შენი სახლიდან სკოლამდე მანძილი სანტიმეტრებში არის: ", int(the_distance)*int(100000), "სანტიმეტრი")
print("შენი სახლიდან სკოლამდე მანძილი მილიმეტრებში არის: ", int(the_distance)*int(1000000), "მილიმეტრი")

# N4.

your_name = input("რა არის შენი სახელი: ")
your_surname = input("რა არის შენი გვარი: ")
mother_name = input("რა არის დედაშენის სახელი: ")
mother_surname = input("რა არის დედაშენის გვარი: ")
father_name = input("რა არის მამაშენის სახელი: ")
father_surname = input("რა არის მამაშენის გვარი: ")
fav_color = input("რა არის შენი საყვარელი ფერი: ")
fav_car = input("რომელი მანქანა მოგწონს ყველაზე მეტად?: ")
hobbies = input("რა არის შენი 3 ჰობი?: ")
print("შენი სრული სახელია: " + your_name + " " + your_surname + "," + " " + "შენი მშობლების სრული სახელები არის: " + mother_name + " " + mother_surname + " " + "და" + " " + father_name + " " +father_surname + "," + " " + "შენი საყვარელი მანქანაა: " + fav_car + "," + " " + "შენი საყვარელი ფერია: " + fav_color + "," + " " + "შენი სამი ჰობია: " + hobbies + ".")
                
# N5.

two_dgit_number = input("შემოიტანეთ ორნიშნა ციფრი: ")
first_number = int(two_dgit_number) // 10
second_number = int(two_dgit_number) % 10
print(first_number)
print(second_number)
sum_of_dgits = first_number + second_number
print("თქვენი ორნიშნა რიცხვის ციფრთა ჯამია: " + str(sum_of_dgits))
