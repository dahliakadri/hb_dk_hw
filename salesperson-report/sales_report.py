"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

def get_melons_sold_by_salesperson(sales_report_file):
    """returns a dictionary on salesperson and melons sold"""
    melons_by_salesperson = {}

    with open(sales_report_file) as file:
        for line in file:
            line = line.rstrip()
            entries = line.split('|')
            salesperson = entries[0]
            melons_sold = int(entries[2])

            if salesperson in melons_by_salesperson:
                melons_by_salesperson[salesperson] += melons_sold
            else:
                melons_by_salesperson[salesperson] = melons_sold

    return melons_by_salesperson

def print_sales_report(melons_by_salesperson):
    """print a report of salespeople and total num of melons they sold"""

    for salesperson, melons_sold in melons_by_salesperson.items():
        print(f'{salesperson} sold {melons_sold} melons')

print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))