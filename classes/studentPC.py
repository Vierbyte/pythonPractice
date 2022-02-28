from pc import *
from student import *

coreys_pc = PC("desktop", "windows", 64)
ronnies_pc = PC("laptop", "windows", 16)
montys_pc = PC("tablet", "linux", 8)
corey = student("Corey", 27, "C")
ronnie = student("Ronie", 25, "B")
monty = student("Monty", 21, "B")
print(coreys_pc.btype, coreys_pc.OS, coreys_pc.ram)

print(ronnies_pc.ram)
coreys_pc.power_on()
monty.no_pc()
print(monty.name + " is running " + montys_pc.OS + " on his machine.")
print(coreys_pc.is_on)
print(ronnie.name, ronnie.age, ronnie.grade)
coreys_pc.pc_attributes()