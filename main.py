# Temporary main testing, can delete later if wanted :)
import simulation
import display

def main():
    print("Simulation of Charged Particles Moving Throughout a Biased Electrical Field")
    print("Please input the following parameters")
    n = int(input("Number of particles: "))
    step_size = int(input("Length of particle step: "))
    frames = int(input("Number of animation frames: "))
    x_range = [int(input("Electric Field, x coordinate range\nminimum: ")), int(input("maximum: "))]
    y_range = [int(input("Electric Field, y coordinate range\nminimum: ")), int(input("maximum: "))]

    generated_particles = simulation.run_simulation(n, step_size, frames, x_range, y_range)

    display.scatter_plot(generated_particles, frames, x_range, y_range)

if __name__ == "__main__":
    main()