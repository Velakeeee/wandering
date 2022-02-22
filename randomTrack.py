from wandering import ComunWandering
from track import track
from location import location

from bokeh.plotting import figure, output_file, show 

def walking(location, wandering, steps):
    beginning = location.get_location(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)
    return beginning.distance(location.get_location(wandering))


def simulate_walk(steps, number_attempts, type_wandering):
    wandering = type_wandering(name='Tulio')
    origen = location(0,0)
    distances = []
    
    for _ in range(number_attempts):
        track = track()
        track.add_wandering(wandering, origen)
        simulations_walk = walking(track, wandering, steps)
        distances.append(round(simulations_walk, 1))
    return distances

def graph(x, y):
    graphics = figure(tittle='Camino del errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x, y, legend='Distancia')
    show(graphics)