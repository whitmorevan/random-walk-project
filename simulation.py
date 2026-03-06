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
    x = round(random.uniform(x_range[0], x_range[1]), 2)
    y = round(random.uniform(y_range[0], y_range[1]), 2)
    
    coord.append(x)
    coord.append(y)
    
    return coord


def avoid_collision(particles):
    """
    Determines if a spot is occupied. If not occupied, the particle's x, y, z position are updated. If not, the particle remains in its current position.
    
    Arg:
        particles(list): list of particles each represented by their particle number, charge, and (x, y, z) position.
    
    Returns:
        list: updated particle positions
    """
    #pos=position
    #p[2] represents (x, y, z) in the tuple
    occupied_spot = {pos[2] for pos in particles} 
    updated_particles = []
    
    for particle_number, charge, (x, y, z) in particles:
        
        new_pos = random_step((x, y, z))
        
        #updates particle position if the new position is not occupied. Else it returns the same position to the list
        if new_pos not in occupied_spot:
            occupied_spot.remove(x, y, z)
            occupied_spot.add(new_pos)
            updated_particles.append(particle_number, charge, (new_pos))
        else:
            updated_particles.append(particle_number, charge, (x, y, z))
        
        return updated_particles


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
        valid_y_step = check_valid_position(x_range, y_range, current_pos)
        
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
            take_step(step_size, particle, x_range, y_range)

    return particles
