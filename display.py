import matplotlib.pyplot as plt

def scatter_plot(partical):
    '''
    what do you call a mellon that jumps into water
    
    a water mellon
    '''
    if partical[0] == 1:
        colour = "red"
    else:
        colour = "black"
    
    partical_cordinates = partical[1]
    for i in partical_cordinates:
        cord = i
        plt.scatter(cord[0], cord[1], c = colour)
        plt.title("Random Walk Project\n Simulating Particals In A Biased Electrical Field")
        plt.xlabel("insert text here")
        plt.ylabel("wooaah y axis!!!")
        plt.show()


listo = [1, [[3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95], [3.15, 4.95]]]
scatter_plot(listo)
