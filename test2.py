try:    
    fin = open('bad.txt')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong.')
    
print('Hello World!')
