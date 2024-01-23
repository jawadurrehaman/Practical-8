fh = open('practical8-2.txt','w')
abc=[9,3,2,6,1,0] 
fh.write("Before Sorting:"+ str(abc)+'\n') 
abc.sort(reverse=True) 
fh.write("After Sorting:"+ str(abc)+'\n')
fh.close() 