import threading, random

def Splitter(words):
	mylist = words.split()
	newList = []
	while (mylist):
		newList.append(mylist.pop(
			random.randrange(0,len(mylist))))
	print(' '.join(newList))

if __name__== '__main__':
	sentance = 'Here is a sentence to test my threading task.'
	numOfThreads = 10
	threadList = []

	print("STARTING...\n")
	for i in range(numOfThreads):
		t = threading.Thread(target=Splitter, args=(sentance,))

		t.start()
		threadList.append(t)

	print("\nThread Count:" + str(threading.activeCount()))
	print("EXITING...\n")  