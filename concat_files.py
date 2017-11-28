import glob
import partc_resp_time_v2

#Using the function valid_files to extract data of valid participants (valid indicates participants who have participated in all the 3 surveys)
partc_resp_time_v2.valid_files()
read_files = glob.glob("./data_users1/*.txt") 
#data_users1 folder will contain the data for all the valid participants -> files are named with user IDs
#result.txt will contain the merged data< word, Transliterated/Translated, Valid(1)/Invalid(2)/TimeOut(3) , Response Time> for all the participants
with open("./outputfolder/result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
