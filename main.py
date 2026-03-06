# Temporary main testing, can delete later if wanted :)

import simulation
import display

print("Simulation of Charged Particles Moving Throughout a Biased Electrical Field")
print("Please input the following parameters")
n = int(input("Number of particles: "))
step_size = int(input("Length of particle step: "))
frames = int(input("Number of animation frames: "))
x_range = [int(input("Field minimum x coordinate range: ")), int(input("Field maximum x coordinate range: "))]
y_range = [int(input("Field minimum y coordinate range: ")), int(input("Field maximum y coordinate range: "))]

generated_particles = simulation.run_simulation(n, step_size, frames, x_range, y_range)

display.scatter_plot(generated_particles, frames, x_range, y_range)