def setup():
    # Set the size of your sketch
    size(400, 400)
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(10):
        num=(10-i)*10
        if num%20==0:
            fill(255,0,0)
        else:
            fill(255,255,255)
        ellipse(200, 200, num, num);
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
