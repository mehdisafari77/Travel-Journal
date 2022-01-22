log_file = open("um-server-01.txt") # requiring the csv file into this page


def sales_reports(log_file): # starting a function, passing in the csv file
    for line in log_file:   # for in loop, looping over every line in the file
        line = line.rstrip()   # taking each line and removing all the trailing white space
        day = line[0:3]    # setting a variable called "day" to the first 3 characters of each line
        if day == "Mon":    # if statement asking if the "day" variable = "tue"
            print(line)     # printing the whole line to the console, as long as it meets the above if statement conditions


sales_reports(log_file)
