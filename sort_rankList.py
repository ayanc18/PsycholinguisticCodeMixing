from operator import itemgetter
import os
import numpy

#function to write ranked list in corresponding text output files.
def findrankedlist(input):
    if(input == 1):
        x=1
    elif(input == 2):
        x=2
    elif (input== 3):
        x=3
    else:
        x=4
    
    #open the file to write the word along with rank
    f1 = open('./outputfolder/sortedRankedWordByMetric'+str(x)+'.txt', 'w')
    f2 = open('./outputfolder/sortedRankedWordByMetricRank' + str(x) + '.txt', 'w')
    with open('./outputfolder/avgreaction_dict1.txt', 'r') as f:
        lines = f.readlines()
        final_arr=[]
        col_arr =[]
    for line in lines:
        col_arr = line.split(" ")
        final_arr.append(col_arr)

    #logic to sort
    for i in range(len(final_arr)):
        for j in range(len(final_arr)):
            if final_arr[i][x] >= final_arr[j][x]:
                temp=final_arr[i]
                final_arr[i]=final_arr[j]
                final_arr[j]=temp

    count=1
    listfinal =[]
    for term in final_arr:
        list1=[]
        list1.append(term[0])
        list1.append(count)
        count += 1
        listfinal.append(list1)

    final=sorted(listfinal,key=itemgetter(0))
    #final_rank=sorted(listfinal,key=itemgetter(1))
    #print(final)

    for term in final:
        f1.write(term[0]+ ' '+ str(term[1])+'\n')
    for term1 in listfinal:
        f2.write(term1[0]+' '+str(term1[1])+'\n')

def main():
    '''call the function and provide input as 1,2,3,4 where 1---> sort on the basis of metric 1,
        2---> sort on the basis of metric 2
        3---> sort on the basis of metric 3
        4----> sort on the basis of metric 4.
    '''
    findrankedlist(1)
    findrankedlist(2)
    findrankedlist(3)
    findrankedlist(4)

if __name__ == "__main__":
    main()






