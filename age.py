Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def age():
	select=input("Press (S) For seconds, or (Y) for Years")
	if select=="s":
		age=input("How many years you lived for: ")
		sec=int(age)*365*24*60*60
		print("you have lived for {}".format(sec))
	elif select=="y":
		age=input("How many second you lived for: ")
		year=int(age)/60/60/24/365
		print("You have lived for {}".format(year))

		
>>> 
>>> age()
Press (S) For seconds, or (Y) for Yearss
How many years you lived for: 25
you have lived for 788400000
>>> age()
Press (S) For seconds, or (Y) for Yearsy
How many second you lived for: 157000000000000
You have lived for 4978437.34145104
>>> 
