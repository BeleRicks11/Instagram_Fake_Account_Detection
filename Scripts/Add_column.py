import csv
from csv import writer
from csv import reader
 
counter=0
# Open the input_file in read mode and output_file in write mode
with open('DataSet2.csv', 'r') as read_obj: 
    with open('DataSet3.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Append the default text in the row / list
            if(counter<=600):
                row.append('0')
            else: 
                row.append('1')
            counter=counter+1
            # Add the updated row / list to the output file
            csv_writer.writerow(row)