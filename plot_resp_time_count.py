import matplotlib.pyplot as plt

def plot_it():
    words=[]
    timeframe =[]
    m=100
    interval_size=100
    while(m<5000):
        timeframe.append(m)
        m += interval_size

    print(timeframe)

    #timeframe = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000,2050,2100,2150,2200,2250,2300,2350,2400,2450,2500,2550,2600,2650,2700,2750,2800,2850,2900,2950,3000,3050,3100,3150,3200,3250,3300,3350,3400,3450,3500,3550,3600,3650,3700,3750,3800,3850,3900,3950,4000,4050,4100,4150,4200,4250,4300,4350,4400,4450,4500,4550,4600,4650,4700,4750,4800,4850,4900,4950,5000]
    #timeframe= [500,1000,1500,2000,2500,3000,3500,4000,4500,5000]

    with open('./outputfolder/output_file.txt', 'r') as f1:
        for line in f1:
            words.append(line.strip('\n'))
        print(words)

    for word in words:
        L=[]
        count=0
        count2=0
        L2 = []
        L5=[]
        L6=[]
        for time in timeframe:
            count=0
            count2=0
            with open('./outputfolder/reaction_time_count1.txt', 'r') as f:
                for line1 in f:
                    columns = line1.split(" ")
                    if(columns[0] == word and int(columns[3]) <= time):
                        count += 1
                    if(columns[0] == word and int(columns[2].strip('\n')) <=time):
                        count2 += 1
                L.append(count)
                L5.append(count2)

        #print(L)

        L2.append(L[0])
        L6.append(L5[0])
        for i in range(1,len(L)):
            L2.append(L[i]-L[i-1])
            L6.append(L5[i]-L5[i-1])

        #print(L2) --> transliterated
        #print(L6) ---> translated
        plt.plot(timeframe,L2,'r-')
        plt.plot(timeframe,L6,'b-')


        plt.xlabel('Response Time')
        plt.ylabel('Response Count')


        plt.title(word)
        plt.grid(True)
        #fig.tight_layout()
        plt.savefig('./images_nlp/'+word+ '_'+str(interval_size)+'.png')
        plt.show()


    L3 = []
    count = 0
    L4 = []
    L7 = []
    L8 = []
    for time in timeframe:
        count=0
        count2=0
        with open('./outputfolder/reaction_time_count1.txt', 'r') as f3:
            for line1 in f3:
                columns = line1.split(" ")
                if (columns[0] == word and int(columns[3]) <= time):
                    count += 1
                if(columns[0] == word and int(columns[2].strip('\n')) <=time):
                    count2 += 1
            L3.append(count) #transli
            L7.append(count2) #transla

        # print(L)
    L4.append(L3[0]) #transli
    L8.append(L7[0]) #transla
    for i in range(1, len(L3)):
        L4.append(L3[i] - L3[i - 1])
        L8.append(L7[i]-L7[i-1])

    #print(L4) ---> transliterated
    #print(L8) ----> translated
    plt.plot(timeframe,L4,'r-') #transli
    plt.plot(timeframe,L8,'b-') #transla
    """fig,ax1=plt.subplots()
    ax1.plot(timeframe,L4,'r-')"""
    plt.xlabel('Response Time')
    plt.ylabel('Response Count')

    plt.title("Across all words for interval size "+str(interval_size))
    plt.grid(True)
    #fig.tight_layout()
    plt.savefig('./images_nlp/across_all_words_'+'_'+str(interval_size)+'.png')
    plt.show()

def main():
    plot_it()

if __name__=='__main__':
    main()