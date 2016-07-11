num_connections = float(150000000/10)
total_conn = 0

for i in range(0, int(num_connections)):
	total_conn += num_connections - i - 1
	i += 1
print(str(total_conn * 10) + ' : ' + str(num_connections * 1000000))