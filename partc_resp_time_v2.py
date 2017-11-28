import glob
import csv
import os
import numpy as np

#Extracts the valid users who have participated in all the 3 surveys
def valid_files():
    with open('./data/data.csv','r') as f2:
        count=0
        reader=csv.reader(f2,delimiter=',')
        next(reader,None)
        for row in reader:
            if(row[4] not in (None,'') and row[5] not in (None,'') and row[6] not in (None, '')): #Codemixing parts - 1, 2, 3 should not be blank. It should contain the respective codemixing file names of the respective users

                with open(('./data_users1/'+row[0]),'w') as f3:
                    with open('./data/'+row[4],'r') as f4:
                        for line1 in f4:
                            f3.write(line1)
                    with open('./data/'+row[5],'r') as f6:
                        for line2 in f6:
                            f3.write(line2)
                    with open('./data/' + row[6], 'r') as f8:
                        for line3 in f8:
                            f3.write(line3)
                    count=count+1
        print(count)

def count_words():

    dir2='./data_users1/'

    for root,dir,filenames in os.walk(dir2):
        for f in filenames:
            countlines=0
            if f[0]!='.':
                #print(f)
                f1=dir2+f
                #print(f1)
                with open(f1,'r') as file1:
                    for line1 in file1:

                        countlines=countlines+1
                    print(countlines)

#Calculates the transliteration and translation response time for the words
def reaction_table():
    words=[]
    arr=np.zeros((57,44,2))
    c=0
    p=0
    reaction_dict={}
    with open('./outputfolder/output_file.txt', 'r') as f:
        for line in f:
            words.append(line.strip('\n')) #Keeps distinct words
    dir1='./data_users1/'
    avg_reaction_dict={}
    for word in words:
        avg_reaction_dict["word"]=word
        reaction_dict["word"]=word
        sum_transla = 0
        sum_transli = 0
        sum_transli_valid=0
        sum_transli_invalid=0
        sum_transla_valid = 0
        sum_transla_invalid = 0
        count_transli_valid=0
        count_transla_valid=0
        count_transli_invalid=0
        count_transla_invalid=0
        transli_valid_reaction_time=0
        transli_invalid_reaction_time=0
        transla_valid_reaction_time=0
        transla_invalid_reaction_time=0

        for root,dir,filenames in os.walk(dir1):

            for fname in filenames:
                if(fname[0]!='.'): #Ignoring hidden files or .DSStore(exclusively for MAC which contains metadata)
                    fnamefull=dir1+fname #Appending directory name and filename(respective user ID file names)
                    with open(fnamefull,'r') as fname1:
                        for line1 in fname1:
                            columns=line1.split(" ") #Splitting the columns; Col 1: word ; Col 2 : Transliterated/Translated ; Col 3 : Valid(1) , Invalid (2), Timeout (3) ; Col 4: Response Time in milliseconds
                            if(columns[0] == word):
                                if(columns[1] == 'Transliterated'):
                                    transli_reaction_time=columns[3].strip('\n')
                                    if(columns[2]=='1'):
                                        transli_valid_reaction_time=columns[3].strip('\n')
                                        if(float(transli_valid_reaction_time) >= 500 and float(transli_valid_reaction_time) <=3500): # Calculating scores for participants who have responded within 0.5s to 3.5 s
                                            count_transli_valid+=1
                                    elif(columns[2]=='2'):
                                        transli_invalid_reaction_time=columns[3].strip('\n')
                                        if(float(transli_invalid_reaction_time) >= 500 and float(transli_invalid_reaction_time) <= 3500):
                                            count_transli_invalid+=1

                                    if(float(transli_reaction_time) >=500 and float(transli_reaction_time) <=3500):
                                        sum_transli += float(transli_reaction_time)

                                    if(float(transli_valid_reaction_time) >= 500 and float(transli_valid_reaction_time) <= 3500 ):
                                        sum_transli_valid+=float(transli_valid_reaction_time)
                                    if(float(transli_invalid_reaction_time) >=500 and float(transli_invalid_reaction_time) <= 3500):
                                        sum_transli_invalid+=float(transli_invalid_reaction_time)

                                elif(columns[1] == 'Translated'):
                                    transla_reaction_time=columns[3].strip('\n')
                                    if (columns[2] == '1'):
                                        transla_valid_reaction_time = columns[3].strip('\n')
                                        if(float(transla_valid_reaction_time) >= 500 and float(transla_valid_reaction_time) <=3500):
                                            count_transla_valid+=1
                                    elif (columns[2] == '2'):
                                        transla_invalid_reaction_time = columns[3].strip('\n')
                                        if(float(transla_invalid_reaction_time) >= 500 and float(transla_invalid_reaction_time) <= 3500):
                                            count_transla_invalid+=1

                                    if(float(transla_reaction_time) >=500 and float(transla_reaction_time) <=3500):
                                        sum_transla += float(transla_reaction_time)
                                    if(float(transla_valid_reaction_time) >= 500 and float(transla_valid_reaction_time) <= 3500):
                                        sum_transla_valid += float(transla_valid_reaction_time)
                                    if(float(transla_invalid_reaction_time) >=500 and float(transla_invalid_reaction_time) <= 3500):
                                        sum_transla_invalid += float(transla_invalid_reaction_time)

                    reaction_dict["participant"]=fname.strip('.txt')
                    reaction_dict["translation_time"]=transla_reaction_time
                    reaction_dict["transliteration_time"] = transli_reaction_time


		    #Contains word, participant name, his/her translated reaction time, his/her transliterated reaction time
                    with open('./outputfolder/reaction_time_count1.txt', 'a') as r:
                        r.write(str(word)+' '+str(fname.strip('.txt'))+' '+str(transla_reaction_time)+' '+str(transli_reaction_time))
                        r.write('\n')
     
        # check zero in count_transli_valid and count_transli_invalid
        if(count_transli_valid==0):
            avg_transli_valid=0
        else:
            avg_transli_valid=float(sum_transli_valid)/ float(count_transli_valid)
        if(count_transli_invalid==0):
            avg_transli_invalid=0
        else:
            avg_transli_invalid=float(sum_transli_invalid)/float(count_transli_invalid)
        if(count_transla_valid==0):
            avg_transla_valid=0
        else:
            avg_transla_valid=float(sum_transla_valid)/float(count_transla_valid)
        if(count_transla_invalid==0):
            avg_transla_invalid=0
        else:
            avg_transla_invalid=float(sum_transla_invalid)/float(count_transla_invalid)
	
#Metric 1: Valid transliteration count / Valid translated count
#Metric 2: Valid transliteration count / Valid translated count + Invalid transliteration count
#Metric 3: (Valid transliteration count/ Average Valid transliteration count) / (Valid translation count / Average valid translation count)
#Metric 4: (Valid transliteration count/ Average Valid transliteration count) / [(Valid translation count / Average valid translation count) + (Invalid transliteration count/Average invalid translation count)]
        metric_1 = float(count_transli_valid) / float(count_transla_valid + 1)
        metric_2 = float(count_transli_valid) / float(count_transla_valid + count_transli_invalid + 1)
        metric_3 = (float(count_transli_valid)/float(avg_transli_valid))/(float(count_transla_valid)/float(avg_transla_valid))
        metric_4 = (float(count_transli_valid)/float(avg_transli_valid))/((float(count_transla_valid)/float(avg_transla_valid))+(float(count_transli_invalid)/float(avg_transli_invalid)))

#Col 1 : Word; Col 2 : Metric 1 value; Col 3: Metric 2 value; Col 4 : Metric 4 value        
        with open('./outputfolder/avgreaction_dict1.txt','a') as ar:
            ar.write(word+' '+str(metric_1)+' '+ str(metric_2)+ ' '+ str(metric_3)+ ' '+ str(metric_4) +'\n')



def main():
    reaction_table()
    
if __name__=="__main__":
    main()
