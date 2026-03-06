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
        
        while True:
            pos = random_coord(x_range, y_range)
            if check_collision(pos, particles, None):
                break
            
        p_coords.append(pos)
        p_info.append(p_coords)

        particles.append(p_info)
    
    return particles
        

def random_coord(x_range, y_range):
    """
    takes x, y ranges (lists of two ints) : max and min values for each plane
    
    returns [x, y] 
    
    """
    coord = []
    x = round(random.uniform(x_range[0], x_range[1]), 2)
    y = round(random.uniform(y_range[0], y_range[1]), 2)
    
    coord.append(x)
    coord.append(y)
    
    return coord


def check_collision(pos, particles, current_particle, min_distance=0.25):

    #empty space margin
    space = 1.2
    min_area = (min_distance * space) ** 2

    for particle in particles:

        if particle is current_particle:
            continue

        other_pos = particle[1][-1]

        dx = pos[0] - other_pos[0]
        dy = pos[1] - other_pos[1]
            
        #deals with the fact coordinates are to the decimal places, calculating the area the point occupies
        distance_squared = dx*dx + dy*dy

        if distance_squared < min_area:
            return False

    return True


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



def take_step(step_size, p_info, particles, x_range, y_range):
    
    coords = p_info[1] 
    
    i = 0
    
    while True:
        current_pos = (coords[len(coords) - 1]).copy()
        
        # x step testing
        x = random.uniform(0, step_size)
        if p_info[0] == 0 and random.random() > 0.05:       
            x = -x
        
        current_pos[0] += x
        valid_x_step = check_valid_position(x_range, y_range, current_pos)
        
        if valid_x_step == False:
            current_pos[0] -= x
            y = random.uniform(0, step_size)
        else:
            y = (step_size**2 - x**2)**.5
         
        # y step testing
        if p_info[0] == 0 and random.random() > 0.05:
            y = -y
        
        current_pos[1] += y
        valid_y_step = check_valid_position(x_range, y_range, current_pos) and \
               check_collision(current_pos, particles, p_info) 
        
        if valid_y_step == True:
            break
        
        i += 1
        
        if i == 5:
            current_pos = (coords[len(coords) - 1]).copy()
            break
        
    coords.append(current_pos)



def run_simulation(n, step_size, frames, x_range, y_range):
    """
    Parameters
    ----------
    n : int
        number of particles
    step_size : int
        length of step
    frames : int
        number of animation frames
    x_range : list
        [min_x, max_x]
    y_range : list
        [min_y, max_y]

    Returns
    -------
    particles : list of particles info
    """
    
    particles = generate_particles(n, x_range, y_range)
    
    for frame in range(frames - 1):
        for particle in particles:
            take_step(step_size, particle, particles, x_range, y_range)

    return particles
