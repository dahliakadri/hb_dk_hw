"""Print out all the melons in our inventory."""


from melons import melon_data


def print_melon(melon_data):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melon_data.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print ("---------------------------------")

 
print_melon(melon_data)
