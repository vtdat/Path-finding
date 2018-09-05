import pyvisgraph as vg
from matplotlib import pyplot

def main():
	graph = vg.VisGraph()
	graph.load('ntu_new_2')
	start = map(float, raw_input('Start: ').strip().split())
	end = map(float, raw_input('End: ').strip().split())
	shortest_path = graph.shortest_path(vg.Point(start[0], start[1]), vg.Point(end[0], end[1]))
	x = [point.x for point in shortest_path]
	y = [point.y for point in shortest_path]
	pyplot.plot(x, y)
	m = open('newMap_2.txt')

	for line in m:
		points = (line.strip()).split(',')
		x = []
		y = []
		for point in points:
			point = map(float, point.split())
			x.append(point[0])
			y.append(point[1])
		x.append(x[0])
		y.append(y[0])
		pyplot.plot(x, y)
	
	pyplot.show()
if __name__ == '__main__':
	main()