"""

	ResourcePool.py -- Provides a resource pool for objects.

	by elchupa

"""
import inject
import thread
import threading

import Queue
import logging

class dummy:
	def __call__( self ):
		pass
def dummy_generate():
	return dummy()

class ResourcePool:
	resourcePoolTimeout = inject.attr( "resourcePoolTimeout" )
	maxObjects = inject.attr( "maxObjects" )

	@inject.param( "generate", bindto=dummy_generate )
	def __init__( self, generate ):
		self.generate = generate
		self.pool = Queue.Queue()
		self.lock = threading.RLock()
		
		for i in range( self.maxObjects ):
			self.pool.put( generate() )

		self.logger = logging.getLogger( "PoolManager.ResourcePool" )
	def __enter__( self ):
		self.logger.info( "Objects left in pool: " + str( self.pool.qsize() ) )
		self.obj = self.pool.get( timeout=self.resourcePoolTimeout )

		return self.obj

	def __exit__( self, t, v, b ):
		self.logger.info( "Putting object back into queue" )
		self.pool.put( self.obj )
