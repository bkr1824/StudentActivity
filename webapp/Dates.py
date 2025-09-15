

def get(num):
	import datetime
	d=datetime.datetime.now() + datetime.timedelta(days=num)
	c=datetime.datetime.now()
	d=str(d)
	d=d.split()
	c=str(c)
	c=c.split()[0]

	print(d[0], )
	return c,d[0]
if __name__ == '__main__':
	print(get(2))

