import pyvisgraph as vg
import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
	graph = vg.VisGraph()
	graph.load('ntu_new_2')
	# start = map(float, raw_input('Start: ').strip().split())
	# end = map(float, raw_input('End: ').strip().split())
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((HOST, PORT))
		s.listen(1)
		print 'Waiting for connection...'
		conn, addr = s.accept()
		print 'Connected by: ', addr
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print 'Data received: ', data
			startx, starty, endx, endy = map(float, data.split())
			start = vg.Point(startx, starty)
			end = vg.Point(endx, endy)
			c_start = graph.point_in_polygon(start)
			c_end = graph.point_in_polygon(end)
			path = []
			if c_start != -1:
				path.append(str(start.x) + ' ' + str(start.y))
				start = graph.closest_point(start, c_start)
			if c_end != -1: 
				end = graph.closest_point(end, c_end)
			shortest_path = graph.shortest_path(start, end)
			for point in shortest_path:
				path.append(str(point.x) + ' ' + str(point.y))
			path.append(str(endx) + ' ' +str(endy))
			print 'Data sent: ', ' '.join(path)
			conn.sendall(' '.join(path))
		conn.close()

if __name__ == '__main__':
	main()