#Eric Broadbent
#9/18
# change sorter

def change():
    #1 get input from user how much change
    total_change = int(input("how much change do you have in your pocket: "))
    #2 calculate total for q n d p
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickles = whats_left // 5
    whats_left = whats_left % 5
    cents = whats_left
    #3 display it back to user
    print("Quaters: ",quarters, "\nDimes: ",dimes, "\nNickles: ",nickles,"\nCents: ",cents)

    
change()

def change2(total_change):
    #1 get input from user how much change
    total_change = total_change
    #2 calculate total for q n d p
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickles = whats_left // 5
    whats_left = whats_left % 5
    cents = whats_left
    #3 return value
    return quarters, dimes, nickles, cents

total_change = int(input("how much change do you have in your pocket: "))
quarters, dimes, nickles, cents = change2(total_change)
print("Quaters: ",quarters, "\nDimes: ",dimes, "\nNickles: ",nickles,"\nCents: ",cents)

    









    
