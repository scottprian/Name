import sys
#str(sys.argv[1])
b = float(str(sys.argv[1]))
p = float(str(sys.argv[2]))
a = float(str(sys.argv[3]))

tr = p*100
xr = a*100
print 'bill =',b
print 'tip rate =',tr,'%'
print 'tax rate =',xr,'%'
t = b*p
x = b*a
o = b+t+x
print 'and'
print 'tip =',t
print 'tax =',x
print 'total =',o
