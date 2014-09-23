from matplotlib import pyplot as plt

def plot(data):
	# initialize variables to be lists
    x = []
    y = []

    # lines and add to lists
    for line in lines:
        p=line.split(',')
        x.append(float(p[0]))
        y.append(float(p[1]))
    
    fig=plt.figure()
    graph=fig.add_subplot(111)
    graph.set_title("Data logged from Arduino UNO")
    graph.plot(x,y,'ro')
    plt.show()
	
	