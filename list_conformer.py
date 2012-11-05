class Rule( object ):
	def __init__( self ):
		self.value = None

	def __lt__( self, v ):
		return None
	
	def __gt__( self, v ):
		return None

class Conform:

	def __init__( self, rules = [] ):
		self.rules = rules

	def conform( self, _list ):
		for r in self.rules:
			for i in xrange( 0, len( _list ) - 1 ):
				r.value = _list[i]

				#Check if the item before `i` conforms
				c = i - 1
				if c < 0:
					c = 0
				before = r < _list[c]
			
				after = r > _list[i + 1]
				
				if after == False:
					for k in xrange( i + 1, len( _list ) ):
						if r > _list[k]:
							_list[k], _list[i] = _list[i], _list[k]

				if before == False:
					for k in xrange( i + 1, len( _list ) ):
						if r < _list[k]:
							_list[k], _list[i] = _list[i], _list[k]
		return _list
