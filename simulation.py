import random


def generate_particles(n, x_range, y_range):
    """
    takes n (int) : number of particles
    
    returns particles (list) : [charge as 0/1, [list of [x, y]]]

    """
    # needs to check for overlap
    
    particles = []
    for i in range(n):
        p_info = []
        p_coords = []
        
        charge = random.randint(0, 1)
        p_info.append(charge)
        
        p_coords.append(random_coord(x_range, y_range))
        p_info.append(p_coords)

        particles.append(p_info)
    
    return particles
        

def random_coord(x_range, y_range):
    """
    takes x, y ranges (lists of two ints) : max and min values for each plane
    
    returns [x, y] 
    
    """
    coord = []
    
    coord.append(round(random.uniform(x_range[0], x_range[1]), 2))
    coord.append(round(random.uniform(y_range[0], y_range[1]), 2))
    
    return coord
    


def check_valid_position(x_range, y_range, pos):
    # checks for border
    x = pos[0]
    y = pos[1]
    
    if x < x_range[0] or x > x_range[1]:
        return False
    if y < y_range[0] or y > y_range[1]:
        return False
    
    return True

    # needs to also check for overlap
    # or maybe a different function for it?
    
    

def take_step(step_size, p_info, x_range, y_range):
    # i is a tempory solution to make sim spped faster
    
    coords = p_info[1] 
    valid_step = False
    
    
    i = 0
    while not valid_step:
        current_pos = (coords[len(coords) - 1]).copy()
        
        x = random.random()
        y = (step_size**2 - x**2)**.5
        
    
        if p_info[0] == 0:       
            if random.random() >= 0.1:
                x = -x
            if random.random() >= 0.1:
                y = -y
        
        current_pos[0] += x
        current_pos[1] += y
        
        valid_step = check_valid_position(x_range, y_range, current_pos)
        
        i += 1
        
        if i == 4:
            current_pos = (coords[len(coords) - 1]).copy()
            break

    
    coords.append(current_pos)



def run_simulation(n, step_size, frames, x_range, y_range):
    particles = generate_particles(n, x_range, y_range)
    
    for frame in range(frames - 1):
        for particle in particles:
            take_step(step_size, particle, x_range, y_range)
    
    for particle in particles:
        print(particle)
     


run_simulation(3, 1, 10, [-5, 5], [-5, 5])