print("\n")
print('Hi it\'s me again.')
print("\n")
print("Hi it's me again.")

print("\n")

Hinata = {
    "first_name": "Hinata",
    "lastName": "Hyuuga",
    "age": 21,
    "fighting_style": "Gentle Fist",
    "sex": "Female",
    "village": "Konoha",
    "missions_completed": 210,
    "c_ranked_missions": 72,
    "active_duty": False,
    
    
    
}

b_ranked_missions = Hinata["missions_completed"] - Hinata["c_ranked_missions"]

print("//////////////////////////////////")

print("////////Shinobi info card////////".upper())
ml = 50
print(" " * ml)
print(Hinata["lastName"].upper(), Hinata["first_name"].upper())
print(" ")
print("Fighting Style: ", Hinata["fighting_style"] , " \n\n\n\nNumber of missions completed: ", Hinata["missions_completed"])
print(" ")
print(" ")
print(" ")

#print(Hinata["missions_completed"])
print("C Ranked missions " ,Hinata["c_ranked_missions"])
print(" ")
print(" ")
print(" ")


print("B Ranked missions completed: " ,b_ranked_missions)
print(" ")
print("Currently active: ", Hinata["active_duty"])
print(" ")
print("//////////////////////////////////")
print("\n")

