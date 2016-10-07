#!/usr/bin/env python

import threading

def do_this():

	global x, lock

	lock.acquire()
	try:
		x = 0
		print('This is the first thread!')
		while (x<300):
			x +=1

		print(x)
	finally:
		lock.release(); #### The lock has to be released before modification, 
						#otherwise the next thread can't do anything if it's not released

def do_after():

	global x, lock
	
	lock.acquire()
	try:
		x = 450

		while (x<600):
			x +=1

		print(x)
	finally:
		lock.release();

def main():

	global x, lock
	x = 0

	lock = threading.Lock()

	# main_thread = threading.enumerate()[0]
	# print(main_thread)
	# print(main_thread.isDaemon())

	our_thread = threading.Thread( target = do_this, name = "OurThread" )
	# our_thread.setDaemon(True)
	our_thread.start()
	# print(our_thread.isDaemon())

	# print(our_thread.ident)

	# our_thread.join()

	our_next_thread = threading.Thread( target = do_after, name = "NextThread" )
	our_next_thread.start()

	# print(our_next_thread.ident)

	# print(our_thread.ident)


	# print(threading.active_count())
	# print(threading.enumerate())
	# print(threading.current_thread())
	# print(our_thread.is_alive())
	# input( "Hit enter to die.")
	# dead = True

	# input('''The thread has died. Wait a bit, 
	# 			and hit enter again''')
	# print(our_thread.is_alive())

if ( __name__ == "__main__" ):
	main()