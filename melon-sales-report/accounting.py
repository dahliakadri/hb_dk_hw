SALESPERSON_INDEX = 0
INTERNET_INDEX = 1

def prints_a_line_break():
    """Prints a line"""
    print("*" * 80)



def melons_sold(order_file):
    """gets melons total by melon type sold"""

    #create a dictionary that counts 
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    #open orders-by-type file
    order_file = open(order_file)

    #breaks down file by line and then by index in the line
    for line in order_file:
        melon_data = line.split("|")
        
        melon_type = melon_data[1]
        melon_count = int(melon_data[2])

        melon_tallies[melon_type] += melon_count

    order_file.close()
    
    return melon_tallies
    

def melons_revenue(mellon_tallies):
    """gets mellons revenue utilizing mellon tallies"""

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }


    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print("We sold %d %s melons at %0.2f each for a total of %0.2f" %
        # (melon_tallies[melon_type], melon_type, price, revenue))
        print(f"{melon_tallies[melon_type]} {melon_type} melons sold at "
        f"${price:.2f} each for a total of ${revenue:.2f}")


def team_revenue_breakdown(order_sales_file):
    """gets revenue breakdown by two teams, the sales team and the internet
    sales team"""

    opened_sales_file = open(order_sales_file)
    team_sales = [0, 0]
    for line in opened_sales_file:
        team_data = line.split("|")
        if team_data[1] == "0":
            team_sales[0] += float(team_data[3])
        else:
            team_sales[1] += float(team_data[3])

    print(f"Salespeople generated ${team_sales[1]:.2f} in revenue.")
    print(f"Internet sales generated ${team_sales[0]:.2f} in revenue.")

    return team_sales


def team_outcomes(team_sales):

    if team_sales[1] > team_sales[0]:
        sales_diff = team_sales[1] - team_sales[0]
        print(f"Salespeople generated ${sales_diff:.2f} more dollars than"
                "online sales.")
    else:
        sales_diff - team_sales[0] - team_sales[1]
        print(f"Online sales rule generated ${sales_diff:.2f} more dollars than"
                "salespeople.")



prints_a_line_break()
#gets mellon_tallies from order by type file
melon_tallies = melons_sold("orders-by-type.txt")
#prints mellons revenu utilizing mellon tallies
print("Melons Revenue Breakdown")
melons_revenue(melon_tallies)

prints_a_line_break()
print("Sales Team Revenue Breakdown")
team_sales = team_revenue_breakdown("orders-with-sales.txt")

prints_a_line_break()
#based on the team revenue breakdown, assigns most valued team
print("Outcomes")
team_outcomes(team_sales)



