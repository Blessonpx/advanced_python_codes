# This is for final simulation where Class are declared here itself
# There no Glory in Modularity ........

from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform
import cProfile
import pytest
class Particle:
    __slots__ = ('x','y','ang_vel')
    def __init__(self,x,y,ang_vel):
        self.x=x
        self.y=y
        self.ang_vel=ang_vel

class ParticleSimulator:
    def __init__(self,particles):
        self.particles=particles
    
    def evolve(self,dt):
        timestep = 0.0001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 1. calculate the directions
                norm = (p.x**2+p.y**2)**0.5
                v_x=-p.y/norm
                v_y=p.x/norm
                # 2. calculate Displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y
                # Evole the Particles new position
                p.x+=d_x
                p.y+=d_y
                # 3. repeat for all the time steps

def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    fig = plt.figure()
    ax=plt.subplot(111,aspect='equal')
    line, = ax.plot(X,Y,'ro')

    plt.xlim(-1,1)
    plt.ylim(-1,1)

    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        simulator.evolve(0.01)
        X=[p.x for p in simulator.particles]
        Y=[p.y for p in simulator.particles]
        line.set_data(X,Y)
        return line,
    anim = animation.FuncAnimation(fig,animate,init_func=init,blit=True,interval=10)
    plt.show()
    
def test_visualize():
    particles = [
        Particle(0.3,0.5,1),
        Particle(0.0,-0.5,-1),
        Particle(-0.1,-0.4,3)
    ]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

def test_evolve(benchmark):
    particles = [
        Particle(0.3,0.5,+1),
        Particle(0,-0.5,-1),
        Particle(-0.1,-0.4,+3)
    ]
    simulator = ParticleSimulator(particles)
    benchmark(simulator.evolve,0.1)
    p0,p1,p2=particles
    # Original Code has eps value of 1e-5,the tolerance has decreased
    # needs to be found out whats the case 
    def fequal(a,b,eps=1e-3):
        return abs(a - b )< eps
    #print("p0.x=",p0.x,"||","p0.y=",p0.y)
    assert fequal(p0.x,0.210269)
    assert fequal(p0.y,0.543863)
    assert fequal(p1.x,-0.099334)
    assert fequal(p1.y,-0.490034)
    #print("p2.x=",p2.x,"||","p2.y=",p2.y)
    assert fequal(p2.x,0.191358)
    assert fequal(p2.y,-0.365227)

@profile
def benchmark():
    particles=[
        Particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0))
    for i in range(1000)]
    simulator= ParticleSimulator(particles)
    simulator.evolve(0.1)

if __name__ == '__main__':
    #test_visualize()
    #print("Testing Evolve Funtion")
    #test_evolve()
    #print("Run Benchmark for 1000 particles")
    benchmark()
    ## Adding benchmark to a funtion to give range of time of executions for a given call 
    ## Quite Good at predictions 
    ## Prefer to call in the code instead of terminal
    #######################################################################################################
    # finding bottlenecks with cProfile
    #python -m cProfile -o prof.out .\benchmarking_n_profiling\simul.py
    #pr=cProfile.Profile()
    #pr.enable()
    #benchmark()
    #pr.disable()
    #pr.print_stats()
    #benchmark()
    # Algo to do BenchMarking by Python 
    # 1- Figure Out Funtion By FUntion Profiler Time for execution 
    # 2- Once Narrowed on Function , figure out Line by Line profiler time 

    ## Unable to test line_profiler as working not happening 
    ## To use line profiler do the following 
    ## onda install line_profiler
    ## Add @Profile to function to find line by line bottle_necks
    ## #########################################################################################################
#     ## memory profiler gave the following output 
#     Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     90   88.730 MiB   88.730 MiB           1   @profile
#     91                                         def benchmark():
#     92   88.875 MiB    0.062 MiB        2004       particles=[
#     93   88.875 MiB    0.066 MiB        1000           Particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0))
#     94   88.875 MiB    0.016 MiB        1001       for i in range(1000)]
#     95   88.875 MiB    0.000 MiB           1       simulator= ParticleSimulator(particles)
#     96   88.875 MiB    0.000 MiB           1       simulator.evolve(0.1)
# highest increment happens over particles =[Particle ....] line
# Use of _slot_ to reduce memory_footprint to avoid making an internal dictionary for this
# Result Post that 
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     91   88.414 MiB   88.414 MiB           1   @profile
#     92                                         def benchmark():
#     93   88.531 MiB    0.074 MiB        2004       particles=[
#     94   88.531 MiB    0.027 MiB        1000           Particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0))
#     95   88.531 MiB    0.016 MiB        1001       for i in range(1000)]
#     96   88.531 MiB    0.000 MiB           1       simulator= ParticleSimulator(particles)
#     97   88.531 MiB    0.000 MiB           1       simulator.evolve(0.1)
