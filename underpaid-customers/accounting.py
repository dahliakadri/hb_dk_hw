# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

STANDARD_MELON_COST = 1.00

def parse_customer_orders(customer_order_file, melon_cost):
  """Takes in text file of customer orders and determines which customers have under and overpaid  """
  
  print("List of customers that over or underpaid:")
  customer_order_data = open(customer_order_file)

  for line in customer_order_data:
    line = line.rstrip()
    order = line.split('|')
    
    customer_number = order[0]
    customer_name = order[1]
    customer_melons = float(order[2])
    customer_paid = float(order[3])


    customer_full_name = customer_name.split(' ')
    customer_first_name = customer_full_name[0]


    customer_expected = (customer_melons) * melon_cost

    if customer_expected != customer_paid:
      print(f"Customer #{customer_number}, {customer_name}",
            f"paid ${customer_paid:.2f}, expected",
            f"${customer_expected:.2f}")

    if customer_expected > customer_paid:
      under_difference = customer_expected - customer_paid
      print(f"{customer_first_name} underpaid by ${under_difference:.2f}")

    elif customer_expected < customer_paid:
      over_difference = customer_paid - customer_expected
      print(f"{customer_first_name} overpaid by ${over_difference:.2f}")



  customer_order_data.close()

parse_customer_orders("customer-orders.txt", melon_cost = STANDARD_MELON_COST)
# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
