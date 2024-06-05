import sys
from collections import Counter
if len(sys.argv)!=3:
	print('Usage: python evalPOS.py goldPOS_filename systemPOS_filename')
	sys.exit(1)

gold_original = [line.strip() for line in open(sys.argv[1], 'r')]
system_original = [line.strip() for line in open(sys.argv[2], 'r')]

gold = []
system = []
# remove all the empty lines
for i in gold_original:
        if i != '':
                gold.append(i)
for j in system_original:
        if j != '':
                system.append(j)


if len(gold)!=len(system):
	print('Number of lines between gold and system do not match!')
	sys.exit(1)

tagCnt = 0
correctCnt = 0
list_mistake = []
gold_tag = []
sys_tag = []
for i in range(0,len(gold)):
        if not gold[i]:
                continue
        tagCnt+=1
        goldPOS = gold[i].split('\t')[1]
        gold_tag.append(goldPOS)
	
        if not system[i]:
                continue
        elif goldPOS == system[i].split('\t')[1]:
                sys_tag.append(system[i].split('\t')[1])
                correctCnt+=1
                continue
        elif goldPOS != system[i].split('\t')[1]:
                list_mistake.append((system[i].split('\t')[1], goldPOS))
                sys_tag.append(system[i].split('\t')[1])
                continue      
        
print('Accuracy: %f%% %d/%d correct POS tags\n' % (100.0*(correctCnt)/tagCnt, correctCnt, tagCnt))
# gold_tag_count= {"NS" : 3}
gold_tag_count = dict(Counter(gold_tag).items())

# sys_tag_count = {"NS" : 6}
sys_tag_count = dict(Counter(sys_tag).items())

# list_mistake = [("NS" , "VB")] means NS is should be tagged as VB
# dict_mistake_count = {("NS" , "VB"):3} means "NS" was supposed to be tagged as "VB" 3 times
dict_mistake_count = dict(Counter(list_mistake).items())

print ("\tPrecision\tRecall")

sys_tag_unique = []
# dict_sys_error is for confusion matrix
dict_sys_error = {}
for i in sys_tag_count:

        sys_tag_unique.append(i)
        error_num = 0
        for j in dict_mistake_count:
                if i == j[0]:                        
                        error_num += dict_mistake_count[j]
        dict_sys_error[i] = error_num
        
        if i not in gold_tag_count:
                
                print ("%s\t0%%\tundefined" % (i))
        else:
                precision = 100*(sys_tag_count[i] - error_num) / sys_tag_count[i]
                recall = 100* (sys_tag_count[i] - error_num) / gold_tag_count[i]
                print ("%s\t%d%%\t\t%d%%" % (i, precision, recall))
print ("\nconfusion matrix:\n(Column is the gold standard POS; Row is the system POS)\n")

# the first row of confusion matrix is the system POS
sys_tag_unique.insert(0, "")
row1 = "\t".join(sys_tag_unique)
# expandtabs(5) is to shorten the gap between columns
print (row1.expandtabs(5))
# the column of confusion matrix is the gold standard POS
for i in gold_tag_count:
        list_matrix = [i]
        for j in sys_tag_unique[1:]:
# how many gold POS is correctly captured
                if j == i:
                        list_matrix.append(str(sys_tag_count[i]-dict_sys_error[i]))
# how many gold POS is wrongly tagged into which POS                        
                elif (j, i) in dict_mistake_count:
                        list_matrix.append(str(dict_mistake_count[(j, i)]))
                else:
                        list_matrix.append("0")
        row = "\t".join(list_matrix)
        print (row.expandtabs(5))




                
