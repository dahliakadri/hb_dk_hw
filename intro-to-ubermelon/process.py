#create a file object from um-server-01.txt so we can access its contents via python
log_file = open("um-server-01.txt")

#Function to print particual day of sales, in this case for Monday
def sales_reports(logged_file):
    #get each line in the log_file
    for line in logged_file:
        #strip characters (extra white space from the right)
        line = line.rstrip() 
        #setting day to be first three characters of each line
        day = line[0:3]
        #if day is "Mon" print that line  
        if day == "Mon": 
            print(line)


#call the sales_reports function and pass in the log_file parameter
sales_reports(log_file)
