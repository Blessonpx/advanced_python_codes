import Particle

class ParticleSimulator:
    def __init__(self,particles):
        self.particles=particles

    def evolve(self,dt):
        timestep = 0.0001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles
            # 1. calculate the directions
            norm = (p.x**2+p.y**2)**0.5
            v_x=-p.y/norm
            v_y=p.x/norm

            # 2. calculate Displacement
            d_x = timestep * p.ang_vel * v_x
            d_y = timestep * p.ang_vel * v_y
            p.x+=d_x
            p.y+=d_y

            # 3. repeat for all the time steps
            
