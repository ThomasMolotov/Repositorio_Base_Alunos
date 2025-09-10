pa = 80000
pb = 200000
p100a = 0.03
p100b = 0.015
anos = 0

while pa < pb:
    pa *= (1 + p100a)
    pb *= (1 + p100b)
    anos += 1 

print(f"Será necessário {anos} anos")