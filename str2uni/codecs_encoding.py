from codecs_to_hex import to_hex
text = '/flag' #payload here
print 'Raw:', repr(text)
u = to_hex(text.encode('utf-8'),1)
a=[]
u_split = u.split(' ')
for i in u_split:
	a.append('\u00'+i)
	
print ''.join(a)
