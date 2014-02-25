import csv
from collections import OrderedDict, namedtuple
import sys

if __name__=='__main__':
	try:
		path = sys.argv[1]
		with open(path) as f:
			reader = csv.reader(f)
			tup = namedtuple('tup', ['price', 'year', 'month'])
			d = OrderedDict()
			names = next(reader)[2:]
			for name in names:
				d[name] = tup(0, 'year', 'month')
			for row in reader:
				year, month = row[:2]         
				for name, price in zip(names, map(int, row[2:])): 
					if d[name].price < price:
						d[name] = tup(price, year, month)
		for k,v in d.items():
			print 'comapny name %s  |  price %s | year %s  | month %s' %(k,v.price,v.year,v.month)
	except IOError as e:
		print " File does not exist !"
	
		
		