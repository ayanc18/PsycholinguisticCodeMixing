
#Extracts distinct words from the merged set of files
with open('./outputfolder/result.txt','r') as f:
    lines=f.readlines()
    result = []
    for x in lines:
        result.append(x.split(' ')[0])
    f.close()
    distinct_content=set(result)

to_file=""
for element in distinct_content:
    to_file=to_file+element+'\n'
with open('./outputfolder/output_file.txt','w') as w:
    w.write(to_file)
