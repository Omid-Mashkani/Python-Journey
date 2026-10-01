#جملات اول و هفتم دنباله حسابی به ترتیب ۱۱ و ۲۱ هستند. مجموع جملات؟

a1 = 11
a7 = 21
d = (a7 - a1) / (7 - 1)

total_sum = 0

print(f"d : {d} ")

for n in range(1, 15):
    an = a1 + ( (n - 1) * d )
    total_sum += an
   
    print(f" jomle{n}: {an} ")

print("____________________")
print(" ")
print(f"sum : {total_sum} ")