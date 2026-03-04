import matplotlib.pyplot as plt

def scatter_plot(partical):
    '''
    input list with first index being charge level, and second index being another list containing partical cordinates

    creates scatter plot for every coordinate in found in the second index of the inputted list
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
