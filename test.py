from shapely.geometry import Polygon
import shapely.ops
from matplotlib import pyplot
from shapely.geometry import JOIN_STYLE



def test():
	eps = 10
	m = open("mapFile.txt")
	
	maxX = max([float((line.strip()).split()[1]) for line in m])
	m.seek(0)
	maxY = max([float((line.strip()).split()[3]) for line in m])
	m.seek(0)
	minX = max([float((line.strip()).split()[1]) for line in m])
	m.seek(0)
	minY = max([float((line.strip()).split()[3]) for line in m])
	m.seek(0)
	polys = []
	polys.append(Polygon([(minX-10, minY-10), (minX-10, maxY+10), (maxX+10, maxY+10), (maxX+10, minY-10)]))
	for line in m:
		name, x, z, y, gx, gz, gy = (line.strip()).split()
		x = float(x)
		y = float(y)
		gx = float(gx)
		gy = float(gy)
		polys.append(Polygon([(x-gx, y-gy), (x-gx,y+gy), (x+gx, y+gy), (x+gx, y-gy)]))
	m.close()
	polyout = shapely.ops.unary_union(polys)
	polyout2 = polyout.buffer(eps, 1, join_style=JOIN_STYLE.mitre).buffer(-eps, 1, join_style=JOIN_STYLE.mitre)
	o = open('newMap.txt', 'w')
	for poly in polyout2:
		x, y = poly.exterior.xy
		for i in xrange(len(x)):
			o.write(str(x[i])+' '+str(y[i]))
			if i != len(x)-1:
				o.write(',') 
		o.write('\n')
		pyplot.plot(x,y)
	# o.close()
	s = '(-520.00, -70.00)(-493.04, -258.88)(-475.51, -282.08)(-457.98, -305.28)(-440.45, -328.47)(-355.16, -396.20)(-248.51, -514.82)(-223.34, -656.32)(-97.64, -804.73)(-60.36, -843.08)(40.28, -1299.34)(450.00, -1300.00)'
	s = s.split(')(')
	s= list (s)
	x = []
	y = []
	for item in s:
		cd = map(float,item.replace('(','').replace(')','').split(', '))
		x.append(cd[0])
		y.append(cd[1])
	pyplot.plot(x[0], y[0], 'go')
	pyplot.plot(x[len(x)-1], y[len(x)-1], 'go')
	pyplot.plot(x, y)
	# x, y = polyout.exterior.xy 
	# pyplot.plot(x,y)
	pyplot.show()

if __name__ == '__main__':
	test()