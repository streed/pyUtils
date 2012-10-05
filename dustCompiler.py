import os
import sys
import time

def scan_dir( dirpath ):
	if os.path.isdir( dirpath ):
		items = []

		for d in os.listdir( dirpath ):
			if os.path.isdir( os.path.join( dirpath, d ) ):
				subItems = scan_dir( os.path.join( dirpath, d ) )
				items = items + subItems

			else:
				if d.endswith( "dustjs" ):
					items.append(os.path.join( dirpath, d ) )
	else:
		if d.endswith( "dustjs" ):
			items.append( d )
	return items

if __name__ == "__main__":
	items = scan_dir( sys.argv[1] )

	for i in items:
		name = i.split( "/" )
		name = name[-1]
		cmd = "buildjs -f %s -n %s" % ( i, name[:name.find( "." )] )

		os.system( cmd )
