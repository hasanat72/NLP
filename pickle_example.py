import pickle

#list=["Hellow","Hi","NNN","KK","when","ll"]

##pick=open("list.pickle","wb")
##pickle.dump(list,pick)
##pick.close()


pick=open("list.pickle","rb")
file=pickle.load(pick)
pick.close()

for items in file:
        print(items)
