def get_daily_produce_summary(the_daily_file):
    """Tokenize daily file to gets a daily summary of produce"""
    print("Daily Log Sheet")
    year = the_daily_file[14:18]
    month = the_daily_file[18:20]
    day = the_daily_file[20:22]
    print("Date:", month, day, year)

    the_daily_file1 = open(the_daily_file)
    for line in the_daily_file1:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(count, melon, amount))

    the_daily_file1.close()

get_daily_produce_summary("um-deliveries-20140519.txt")
get_daily_produce_summary("um-deliveries-20140520.txt")
get_daily_produce_summary("um-deliveries-20140521.txt")


# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]
#     #added correct indexes to melon,count, and amount

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]
#     #added correct indexes to melon,count, and amount

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]
#     #added correct indexes to melon,count, and amount


#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
