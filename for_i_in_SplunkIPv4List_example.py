import csv # Import the python library called "csv" to work with csv file formats
with open('ip_list.csv', newline='') as f: # Open the target csv file with the list of IPs
    reader = csv.reader(f)
    data = list(reader) # Transform that data into a list format for use below
### NB: The IP list is simply a set of IPs in 1 column, without headers, along the lines of 
# 10.0.0.1
# 20.0.0.2
# ...

with open("splunk_SPL_output.txt", "w") as text_file: # Create an output text file for the query to go to --- ideally as part of modular work flow for ease of customisation --- with each section below appended to the output file as stated in text format
    print('index=myIndex sourcetype="somesourcetype"', file=text_file) # This is the start of the Splunk query that specifies the index (ie. data source details)
    ### This while loop creates the idividual search strings per IP/cidr as required by Splunk for this sort of bulk query search inline --- this can be done with an input lookup, provided that exists and is in a usable + accessable format, the reason for doing it inline is for expediency around testing and R+D while exploring data during new investigation types
    i = 0 
    while i < (len(data) - 1):
        print('c_ip="' + str(data[i]).replace("['", "").replace("']", "") + '" OR', file=text_file) # This loops through the IP list imported and places it within the required Splunk query format --- and removes the extra characters that come from the python outputs that would otherwise interfere with the search query function in Splunk
        i = i + 1
    print('c_ip="' + str(data[i]).replace("['", "").replace("']", "") + '"', file=text_file) # This ends the query and omits the final "OR" for accurate Splunk SPL to be able to run immediately
    print('| stats count by Email', file=text_file) # This creates a statistical count of the results by Email as an identifying tag
    print('| sort -count', file=text_file) # This completes the Splunk query by sorting the counts in descending order in the output table in Splunk