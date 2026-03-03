import matplotlib.pyplot as plt

def scatter_plot(x, y, charge):
    '''
    scatter_plot(x, y) | 
    oks so i believe the particals will have x and y cordinates and then a charge level to indicate which side of the graph it will be on, or idk how that will effect the x axis... maybe the charge is the x axis??? ¯\_(ツ)_/¯  idk will see later on ima just start writing stufff.
    
    input x and y cordinates along with the charge level and shoes the plot
    '''
    plt.scatter(x, y)
    plt.xlim(0, 1)
    plt.title("Random Walk Project\n Simulating Particals In A Biased Electrical Field")
    plt.xlabel("Charge Level\n 0 being positive and 1 being negative")
    plt.ylabel("wooaah y axis!!!")
    plt.show()
    
    #need to work on like colours 
