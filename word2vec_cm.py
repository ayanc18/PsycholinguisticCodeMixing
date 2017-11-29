from numpy.linalg import norm
from operator import itemgetter
import  os
import math
import numpy as np
from scipy.stats.stats import spearmanr
import csv

#Defining the interval buckets
interval =[0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000,2050,2100,2150,2200,2250,2300,2350,2400,2450,2500,2550,2600,2650,2700,2750,2800,2850,2900,2950,3000,3050,3100,3150,3200,3250,3300,3350,3400,3450,3500,3550,3600,3650,3700,3750,3800,3850,3900,3950,4000,4050,4100,4150,4200,4250,4300,4350,4400,4450,4500,4550,4600,4650,4700,4750,4800,4850,4900,4950,5000]
matallvec=[]
Fin=[]
words=[]

def get_interval():
    count1 = 0
    with open('./outputfolder/output_file.txt', 'r') as f1:
        for line in f1:
            words.append(line.strip('\n'))
        print(words)
    dir1 = './data_users1/'

    # For each word, search for each bucket in all the participants' files and report the count of participants responding in that range and obtain a probability distribution.
    # Probability(each word in a particular bucket) = Count of participants responding valid to the word in that bucket / Count of total participants responding as valid as a whole.Thus we obtain the word vector of dimension size = interval bucket size
    for v in range(1, 11):
        cnt = 0
        initial = 0
        for word in words:
            vecW = []
            diff = 0
            arr = np.zeros(
                (5700, 2))  # 57 words x 100 intervals x 2 responses ( 1 for transliteration , 1 for translation )
            count = 0
            transli = 0
            transla = 0
            countothers = 0
            int_dict = {}
            val_dict = {}
            for i in range(0, len(interval) - v, v): # for varying interval: 0-50,50-100 ; 0-100, 100-200...,0-500,500-1000..
                counttransli = 0
                counttransla = 0

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
                                                if (interval[i] <= float(transli_valid_reaction_time) and interval[
                                                        i + v] > float(
                                                        transli_valid_reaction_time)):  # Falling within the specific bucket range
                                                    counttransli = counttransli + 1
                                            else:
                                                countothers = countothers + 1
                                        elif (columns[1] == "Translated"):
                                            transla_reaction_time = columns[3].strip('\n')
                                            if (columns[2] == '1'):
                                                transla_valid_reaction_time = columns[3].strip('\n')
                                                if (interval[i] <= float(transla_valid_reaction_time) and interval[
                                                        i + v] > float(transla_valid_reaction_time)):
                                                    counttransla = counttransla + 1
                                            else:
                                                countothers = countothers + 1
                vecW.append(count)
                transli = transli + counttransli  # Total valid count in all buckets(or intervals) for a word in itransliterated form
                transla = transla + counttransla  # Total valid count in all buckets(or intervals) for a word in translated form
                arr[cnt, 0] = counttransli
                arr[cnt, 1] = counttransla
                cnt = cnt + 1
                print("word = ", word, "interval = ", interval[i], " transliterated count = ", counttransli,
                      "translated count = ", counttransla)
                # Col 1: word ; Col 2: interval bucket ; Col 3: transliterated count ; Col 4: Translated count
                dir2 = './outputfolder/interval' + str(v) + '.txt'
                with open(dir2, 'a') as ri:
                    ri.write(str(word) + ' ' + str(interval[i]) + ' ' + str(counttransli) + ' ' + str(counttransla))
                    ri.write('\n')

            print("total valid count of transliterated word = ", word, " = ", transli)
            print("total valid count of translated word = ", word, " = ", transla)
            dir3 = './outputfolder/vectorword' + str(v) + '.txt'
            with open(dir3, 'a') as vc:
                j = 0
                for i in range(initial, cnt):
                    # Finding probability of word: count of valid for the bucket / total count of valid
                    arr[i, 0] = arr[i, 0] / transli
                    arr[i, 1] = arr[i, 1] / transla
                    # Finding L2 norm between the 2 forms of each word after obtaining the word vector
                    diff = diff + (math.pow((arr[i, 0] - arr[i, 1]), 2))
                    # Col 1 : Word ; Col 2: Interval bucket ; Col 3: Probability for transliterated form ; Col 4 : Translated form
                    vc.write(str(word) + " " + str(interval[j]) + " " + str(arr[i, 0]) + " " + str(arr[i, 1]))
                    vc.write('\n')
                    j = j + 1
            initial = cnt
            diff = math.sqrt(diff)
            # Col 1: word ; Col 2: Total people termed it as Transliterated ; Col 3: Total people termed it as Translated ; Col 4: L2 Norm distance
            dir4 = './outputfolder/total' + str(v) + '.txt'
            with open(dir4, 'a') as rt:
                rt.write(str(word) + ' ' + str(transli) + ' ' + str(transla) + ' ' + str(diff))
                rt.write('\n')

#Sorting the file named as "total(i).txt" on the basis of L2 norm ( descending order )
def sort_thelist(m):
    Fin=[]
    with open('./outputfolder/total'+str(m)+'.txt', 'r') as rt: #total1 , total2 ... total(i) refers to ith interval file
        for line in rt:
            ar=line.split(" ")
            newarr=[]
            newarr.append(ar[0])
            newarr.append(float(ar[3]))
            Fin.append(newarr)
    #Sorting
    for i in range(len(Fin)):
        for j in range(len(Fin)):
            if(Fin[i][1] > Fin[j][1]):
                temp = Fin[i]
                Fin[i]=Fin[j]
                Fin[j]=temp
    with open('./outputfolder/sortedlist.txt','a') as st: #Contains the words and their L2 norm in a particular interval
        st.write("===================="+str(m*50)+"th interval ====================\n")
        for p in range(len(Fin)):
            st.write(Fin[p][0]+" ")
            st.write(str(Fin[p][1]))
            st.write("\n")
    return Fin

def log_ranklist():
    with open('./ranking_jp.csv','r') as f:
        #csvreader=csv.reader(f)
        csvreader = csv.reader(f, delimiter=',')
        next(csvreader, None)
        ranklist_jp=[]
        for row in csvreader:
            ranklist_jp.append(float(row[1]))

    return ranklist_jp

#Rank List for the words in the m-th interval
def generate_ranklist_for_wordvec(Fin,m):
    count2=1
    count3=1
    with open('./outputfolder/newrank1_'+str(m)+'.txt', 'w') as wt:
        i=1
        for f in Fin:
            wt.write(f[0]+" "+str(i))
            i=i+1
            wt.write('\n')
    with open('./outputfolder/newrank2_'+str(m)+'.txt', 'w') as wt2:
        i=57
        for f in Fin:
            wt2.write(f[0]+" "+str(i))
            i=i-1
            wt2.write('\n')


    with open('./outputfolder/newrank1_'+str(m)+'.txt', 'r') as f:
        lines = f.readlines()
        final_arr = []
        col_arr = []
    for line in lines:
        col_arr = line.split(" ")
        final_arr.append(col_arr)

    listfinal = []
    for term in final_arr:
        list1 = []
        list1.append(term[0])
        list1.append(count2)
        count2 += 1
        listfinal.append(list1)

    final = sorted(listfinal, key=itemgetter(0))
    with open('./outputfolder/rankorder1_'+str(m)+'.txt', 'w') as f11:
        for i in range(len(final)):
            f11.write(final[i][0]+" "+str(final[i][1]))
            f11.write('\n')

    with open('./outputfolder/newrank2_'+str(m)+'.txt', 'r') as f2:
        lines2 = f2.readlines()
        final_arr2 = []
        col_arr2= []
        for line in lines2:
            col_arr2 = line.split(" ")
            final_arr2.append(col_arr2)

        listfinal2 = []
        for term in final_arr2:
            list2 = []
            list2.append(term[0])
            list2.append(term[1])
            #count3 += 1
            listfinal2.append(list2)

    final2 = sorted(listfinal2, key=itemgetter(0))
    with open('./outputfolder/rankorder2_'+str(m)+'.txt', 'w') as f12:
            for i in range(len(final2)):
                f12.write(final2[i][0] + " " + str(final2[i][1]))
    #return final

def main():
    get_interval()
    for i in range(1,11):
        Fin=[]
        metric_ranklist = []
        metric_ranklist1 = []
        Fin=sort_thelist(i)
        generate_ranklist_for_wordvec(Fin,i)

        with open('./outputfolder/rankorder1_'+str(i)+'.txt', 'r') as fmt:
            lines4 = fmt.readlines()
            for line4 in lines4:
                metric = line4.split(" ")[1]
                metric_ranklist.append(int(metric.strip('\n')))
            corr_newmetric1 = spearmanr(log_ranklist(), metric_ranklist)

        with open('./outputfolder/descendingOrderCorrelation.txt', 'a') as doc: #Contains the correlation coefficient values for descending order L2 norm ranks
            doc.write(str(i*50)+' interval result for rank order 1: ')
            doc.write(str(corr_newmetric1[0]))
            doc.write("\n")

        with open('./outputfolder/rankorder2_'+str(i)+'.txt', 'r') as fmt:
            lines4 = fmt.readlines()
            for line4 in lines4:
                metric = line4.split(" ")[1]
                metric_ranklist1.append(int(metric.strip('\n')))
            corr_newmetric1 = spearmanr(log_ranklist(), metric_ranklist1)

        with open('./outputfolder/ascendingOrderCorrelation.txt', 'a') as aoc: #Contains the correlation coefficient values for ascending order L2 norm ranks
            aoc.write(str(i*50)+' interval for rank order 2: ')
            aoc.write(str(corr_newmetric1[0]))
            aoc.write("\n")


if __name__ == "__main__":
    main()
