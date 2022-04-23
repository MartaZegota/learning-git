print("Liczby podzielne przez 5:\n")
for i in range(0, 100):
  if i % 5 == 0:
    print(i, end=" ")


print("\nSześciany tych liczb:\n")

for i in range(0, 100):
  if i % 5 == 0:
    print(i**3, end=" ")