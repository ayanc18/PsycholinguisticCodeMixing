from scipy.stats.stats import spearmanr
import csv

# function to read the ground truth or benchmark rank list for the corresponding word list.
def log_ranklist():
    with open('./ranking_jp.csv','r') as f:
        #csvreader=csv.reader(f)
        csvreader = csv.reader(f, delimiter=',')
        next(csvreader, None)
        ranklist_jp=[]
        for row in csvreader:
            ranklist_jp.append(float(row[1]))

    return ranklist_jp

# function to read the rank list of the words by Metric 1 proposed by us.
def metric1_ranklist():
    metric1_ranklist=[]
    with open ('./outputfolder/sortedRankedWordByMetric1.txt','r') as fmt1:
        lines1=fmt1.readlines()
        for line1 in lines1:
            metric1_ranklist1=line1.split(" ")[1]
            metric1_ranklist.append(int(metric1_ranklist1.strip('\n')))

    return metric1_ranklist

# function to read the rank list of the words by Metric 2 proposed by us.
def metric2_ranklist():
    metric2_ranklist=[]
    with open ('./outputfolder/sortedRankedWordByMetric2.txt','r') as fmt2:
        lines2=fmt2.readlines()
        for line2 in lines2:
            metric2_ranklist1=line2.split(" ")[1]
            metric2_ranklist.append(int(metric2_ranklist1.strip('\n')))

    return metric2_ranklist

# function to read the rank list of the words by Metric 3 proposed by us.
def metric3_ranklist():
    metric3_ranklist=[]
    with open ('./outputfolder/sortedRankedWordByMetric3.txt','r') as fmt3:
        lines3=fmt3.readlines()
        for line3 in lines3:
            metric3_ranklist3=line3.split(" ")[1]
            metric3_ranklist.append(int(metric3_ranklist3.strip('\n')))

    return metric3_ranklist

#function to read the rank list of the words by Metric 4 proposed by us. 
def metric4_ranklist():
    metric4_ranklist=[]
    with open ('./outputfolder/sortedRankedWordByMetric4.txt','r') as fmt4:
        lines4=fmt4.readlines()
        for line4 in lines4:
            metric4_ranklist4=line4.split(" ")[1]
            metric4_ranklist.append(int(metric4_ranklist4.strip('\n')))

    return metric4_ranklist


def main():
    #valid_files()
    #metric1_ranklist()
    with open('./outputfolder/correlation.txt','a') as cf:
        #calculate the sperman correlation coefficient between ground truth rank list and rank list by metric 1.
        corr_metric1=spearmanr(log_ranklist(),metric1_ranklist())
        cf.write('Metric 1: '+str(corr_metric1[0]))
        cf.write('\n')
        print(corr_metric1)
        #calculate the sperman correlation coefficient between ground truth rank list and rank list by metric 2.
        corr_metric2 = spearmanr(log_ranklist(), metric2_ranklist())
        cf.write('Metric 2: '+str(corr_metric2[0]))
        cf.write('\n')
        print(corr_metric2)
        #calculate the sperman correlation coefficient between ground truth rank list and rank list by metric 3.
        corr_metric3 = spearmanr(log_ranklist(), metric3_ranklist())
        cf.write('Metric 3: '+str(corr_metric3[0]))
        cf.write('\n')
        print(corr_metric3)
        #calculate the sperman correlation coefficient between ground truth rank list and rank list by metric 4.
        corr_metric4 = spearmanr(log_ranklist(), metric4_ranklist())
        cf.write('Metric 4: '+str(corr_metric4[0]))
        cf.write('\n')
        print(corr_metric4)
    #count_words()
if __name__=="__main__":
    main()


