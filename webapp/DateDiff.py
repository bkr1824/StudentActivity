class DateDiff:
	def calc(d1, d2):
		d1=d1.split('T')[0]
		d2=d2.split('T')[0]
		d1=d1.replace('-','/')
		d2=d2.replace('-','/')

		from datetime import datetime
		date_format = "%Y/%m/%d"
		a = datetime.strptime(d1, date_format)
		b = datetime.strptime(d2, date_format)
		delta = b - a
		print(delta.days)
		return delta.days


if __name__ == '__main__':
	DateDiff.calc('2015-11-22','2015-11-23')
