"""
	ThreadPool.py -- Implement a simple thread pool.
	
	by sean
"""

import threading
from Queue import Queue

import logging

class Worker( threading.Thread ):
	def __init__( self, event, jobs ):
		threading.Thread.__init__( self )

		self.jobs = jobs
		self.daemon = True
		self.event = event
		self.start()

	def run( self ):
		while not self.event.is_set():
			func, args, kargs = self.jobs.get()

			try: 
				func( *args, **kargs )
			except Exception, e:
				pass
			self.jobs.task_done()

class ThreadPool:
	def __init__( self, numThreads = 10 ):
		self.jobs = Queue( numThreads )
		self.event = threading.Event()

		for _ in range( numThreads ):
			Worker( self.event, self.jobs )

	def addJob( self, func, *args, **kargs ):
		self.jobs.put( ( func, args, kargs ) )
	
	def waitAll( self ):
		self.jobs.join()
	
	def killAll( self ):
		self.event.set();

if __name__ == "__main__":

	from time import sleep
	def test( t ):
		print "yay: " + str( t )
		sleep( 1 )
	def kill( event ):
		sleep( 5 )
		event.set()
	pool = ThreadPool( 10000 )

	for i in range( 100000 ):
		pool.addJob( test, i )

	pool.waitAll()
