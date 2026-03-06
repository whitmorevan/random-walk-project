import matplotlib.pyplot as plt

def scatter_plot(listo, frames, x_range, y_range):
    """
    Displays a series of scatter plots based on inputted lists and number of plots to generate (as frames)

    input:
    list containing the particles, each particle is a list which contains its charge level, and another list of its coordinates
    number of animation frames
    min/max range for x coordinate for graph
    min/max range for y coordinate for graph
    """

    # Run count holds which index to use when plotting the particle coordinates and increases based on every run until all frames are displayed
    run_count = 0
    while run_count < frames:
        for particle in listo:
            # Determines particle colour based on charge
            if particle[0] == 1:
                colour = "red"
            else:
                colour = "black"

            # Pinpoints the coordinate within the lists and gets its x and y coordinates then adds it to the graph (along with setting the graphs titles, labels, and x/y ranges)
            particle_coordinates = particle[1]
            current_coordinate = particle_coordinates[run_count]
            plt.xlim(x_range[0], x_range[1])
            plt.ylim(y_range[0], y_range[1])
            plt.scatter(x=current_coordinate[0], y=current_coordinate[1], c=colour)
            plt.title("Random Walk Project\n Simulating Particals In A Biased Electrical Field")
            plt.xlabel("insert text here")
            plt.ylabel("wooaah y axis!!!")

        plt.show()
        run_count += 1