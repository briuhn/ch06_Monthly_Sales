
#Brian Herrera
#Chapter 06 Monthly Sales
#09/13/2024
#Create a program that displays 12 months of sales data, calculates the total yearly sales and
 #average monthly sales, and allows the user to edit the sales for any month


def months(monthlySales):
    """
    this function will display the values in the two dimensional parameter list
    """
    for month in monthlySales:
        print(month[0] + "\t" + str(month[1]))
    print()



def years(monthlySales):
    """
    this function will calculate the average based on the total of all sales values in the list even if
    its changed. 
    """
    total = 0
    for months in monthlySales:
        total += int(months[1])
    average = round(total / len(monthlySales), 2)
    print("yearly total: " + str(total))
    print("Monthly average: " + str(average))


def edit(monthlySales):
    """
    will ask the user for the three letter month and sales value and make a list of those two values
    will replace current single month in the sales list
    """
    month_input = input("Three letter month: ")
    found = False

    for month in monthlySales:
        if month[0] == month_input:
            new_sales = input("Sales Amount: ")
            month[1] = new_sales
            print("Sales amount for " + month_input + " was changed")
            found = True
            break
            

def main():
    monthlySales = [['Jan', '616'], ['Feb', '466'], ['Mar', '796'], ['Apr', '238'],
        ['May', '310'], ['Jun', '726'], ['Jul', '987'], ['Aug', '604'],
        ['Sep', '951'], ['Oct', '958'], ['Nov', '238'], ['Dec', '610']]

    while True:
        print()
        print("COMMAND MENU")
        print("monthly - View monthly sales")
        print("yearly - view yearly summary")
        print("edit - edit sales for a month")
        print("exit - exit program")
        print()

        command = input("Command: ")
        print()

        if command == "monthly":
            months(monthlySales)
        elif command == "yearly":
            years(monthlySales)
        elif command == "edit":
            edit(monthlySales)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid Command.")

        print()


if __name__ == "__main__":
    main()
        
