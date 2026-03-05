import matplotlib.pyplot as plt

def scatter_plot(particle, x_range, y_range):
    '''
    input list with first index being charge level, and second index being another list containing particle coordinates. Along with that input the x and y ranges.

    creates scatter plot for every coordinate in found in the second index of the inputted list
    '''
    # Determines particle colour based on charge
    if particle[0] == 1:
        colour = "red"
    else:
        colour = "black"

    # Creates a plot for each coordinate the partical has been through
    particle_coordinates = particle[1]
    for i in particle_coordinates:
        cord = i
        plt.xlim(x_range[0], x_range[1])
        plt.ylim(y_range[0], y_range[1])
        plt.scatter(cord[0], cord[1], c=colour)
        plt.title("Random Walk Project\n Simulating Particals In A Biased Electrical Field")
        plt.xlabel("insert text here")
        plt.ylabel("wooaah y axis!!!")
        plt.show()
