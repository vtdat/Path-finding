import pyvisgraph as vg

def test():
	m = open('newMap.txt')
	polys = []
	for line in m:
		points = (line.strip()).split(',')
		poly = []
		for point in points:
			point = map(float, point.split())
			poly.append(vg.Point(point[0], point[1]))
		polys.append(poly)
	graph = vg.VisGraph()
	graph.build(polys, workers=4)
	shortest = graph.shortest_path(vg.Point(-520, -70), vg.Point(450, -1300))
	print shortest
if __name__ == '__main__':
	test()