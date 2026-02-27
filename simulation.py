import random


def generate_particles(n, x_range, y_range, z_range):
    """
    takes n (int) : number of particles
    
    returns particles (list) : [p number, charge as 0/1, [list of [x, y, z]]]

    """
    
    particles = []
    for i in range(n):
        p_info = []
        p_info.append(i)
        
        charge = random.randint(0, 1)
        p_info.append(charge)
        
        p_info.append(random_coord(x_range, y_range, z_range))

        particles.append(p_info)
    
    return particles
        

def random_coord(x_range, y_range, z_range):
    """
    takes x, y, z ranges (lists of two ints) : max and min values for each plane
    
    returns [x, y, z] 
    
    """
    coord = []
    
    coord.append(round(random.uniform(x_range[0], x_range[1]), 2))
    coord.append(round(random.uniform(y_range[0], y_range[1]), 2))
    coord.append(round(random.uniform(z_range[0], z_range[1]), 2))
    
    return coord
    


def check_valid_position():
    ...


def take_step(step_size):
    ...


def run_simulation():
    ...



p = generate_particles(5, [-1, 1], [-2, 2], [5, 10])
print(p)
