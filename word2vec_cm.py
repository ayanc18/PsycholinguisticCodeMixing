from numpy.linalg import norm
import  os
import math
import numpy as np

#Defining the interval buckets of span 50
interval =[0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000,2050,2100,2150,2200,2250,2300,2350,2400,2450,2500,2550,2600,2650,2700,2750,2800,2850,2900,2950,3000,3050,3100,3150,3200,3250,3300,3350,3400,3450,3500,3550,3600,3650,3700,3750,3800,3850,3900,3950,4000,4050,4100,4150,4200,4250,4300,4350,4400,4450,4500,4550,4600,4650,4700,4750,4800,4850,4900,4950,5000]
matallvec=[]

words=[]
def get_interval():
    count1 = 0
    with open('./outputfolder/output_file.txt', 'r') as f1:
        for line in f1:
            words.append(line.strip('\n'))
        print(words)
    dir1 = './data_users1/'
    cnt=0
    initial=0
    #For each word, search for each bucket in all the participants' files and report the count of participants responding in that range and obtain a probability distribution. 
    #Probability(each word in a particular bucket) = Count of participants responding valid to the word in that bucket / Count of total participants responding as valid as a whole.Thus we obtain the word vector of dimension size = interval bucket size
    for word in words:
        vecW=[]
        diff=0
        arr=np.zeros((5700,2)) # 57 words x 100 intervals x 2 responses ( 1 for transliteration , 1 for translation )
        count = 0
        transli=0
        transla=0
        countothers = 0
        int_dict={}
        val_dict={}
        for i in range(len(interval)-1):
            counttransli=0
            counttransla=0

            for root, dir, filenames in os.walk(dir1):

                for fname in filenames:

                    if (fname[0] != '.'):
                            fnamefull = dir1 + fname
                            with open(fnamefull, 'r') as fname1:
                                for line1 in fname1:
                                    columns = line1.split(" ")
                                    if (columns[0] == word):
                                        if (columns[1] == 'Transliterated'):
                                            transli_reaction_time = columns[3].strip('\n')
                                            if (columns[2] == '1'):
                                                transli_valid_reaction_time = columns[3].strip('\n')
                                                if (interval[i] <= float(transli_valid_reaction_time) and interval[i+1] > float(transli_valid_reaction_time)): #Falling within the specific bucket range
                                                    counttransli = counttransli+1
                                            else:
                                                countothers=countothers+1
                                        elif(columns[1] == "Translated"):
                                            transla_reaction_time = columns[3].strip('\n')
                                            if (columns[2] == '1'):
                                                transla_valid_reaction_time = columns[3].strip('\n')
                                                if (interval[i] <= float(transla_valid_reaction_time) and interval[i + 1] > float(transla_valid_reaction_time)):
                                                    counttransla = counttransla + 1
                                            else:
                                                countothers=countothers+1
            vecW.append(count)
            transli=transli+counttransli #Total valid count in all buckets(or intervals) for a word in itransliterated form
            transla=transla+ counttransla #Total valid count in all buckets(or intervals) for a word in translated form
            arr[cnt,0]=counttransli
            arr[cnt,1]=counttransla
            cnt=cnt+1
            print("word = ", word, "interval = ",interval[i], " transliterated count = ", counttransli, "translated count = ", counttransla)
           #Col 1: word ; Col 2: interval bucket ; Col 3: transliterated count ; Col 4: Translated count
            with open('./outputfolder/interval.txt', 'a') as ri:
                ri.write(str(word) + ' ' + str(interval[i]) + ' ' + str(counttransli) + ' ' + str(counttransla))
                ri.write('\n')

        print("total valid count of transliterated word = ", word ," = ",transli)
        print("total valid count of translated word = ", word ," = ",transla)
        with open('./outputfolder/vectorword.txt','a') as vc:
            j=0
            for i in range(initial,cnt):
		    #Finding probability of word: count of valid for the bucket / total count of valid
                arr[i,0]=arr[i,0]/transli
                arr[i,1]=arr[i,1]/transla
		    #Finding L2 norm between the 2 forms of each word after obtaining the word vector
                diff=diff+(math.pow((arr[i,0]-arr[i,1]),2))
		     #Col 1 : Word ; Col 2: Interval bucket ; Col 3: Probability for transliterated form ; Col 4 : Translated form
                vc.write(str(word)+" "+str(interval[j])+" "+str(arr[i,0])+" "+str(arr[i,1]))
                vc.write('\n')
                j=j+1
        initial=cnt
        diff=math.sqrt(diff)
	#Col 1: word ; Col 2: Total people termed it as Transliterated ; Col 3: Total people termed it as Translated ; Col 4: L2 Norm distance
        with open('./outputfolder/total.txt','a') as rt:
            rt.write(str(word)+ ' '+ str(transli)+' '+str(transla)+' '+str(diff))
            rt.write('\n')


        matallvec.append(vecW)



def main():
    get_interval()

if __name__ == "__main__":
    main()
