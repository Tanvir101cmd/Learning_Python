total_choco = int(input("Number of chocolates: "))

extra_choco = total_choco%3
remaining_choco = (total_choco - extra_choco)//3

print (f"Each friend will receive {remaining_choco} chocolates")
print ("The number of remaining chocolates is", extra_choco)
