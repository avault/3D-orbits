
x = []
y = []
x = []
vx = []
vy = []
vz = []
m = []
"""never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna never gonna give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you give you  UP"""
va = PVector(0,0,0)
vt = PVector(0,0,0)

g = 10
dt = 0.01

def setup():
    global x, y, z, vx, vy, vz, r, c, m, g, va, dt, n
    n = 4
    x = [0,150,0, 50]
    y = [0, 0, 100, 80]
    z = [0, 50, -50, 100]
    vx = [0, 0, 140, 130]
    vy = [0, 120, 0, 0]
    vz = [0, 0, 0, 20]
    m = [200, 5, 5, 5]
    r = [50, 10, 10, 10]
    c = [color(0,250,0),color(250,0,0),color(0,0,250), color(255,255,0)]
    size(500,500, P3D)

def draw():
    global x, y, z, vx, vy, vz, vt, m, r, c, g, va, dt, n
    background(0)
    translate(width/2, height/2, 0)
    tot_p = 0
    for p in range(0,n):
        get_vector(p)
        vx[p] += vt.x * dt
        vy[p] += vt.y * dt
        vz[p] += vt.z * dt
        tot_p += sqrt(vx[p]**2 + vy[p]**2 + vz[p]**2)
        x[p] += vx[p] * dt
        y[p] += vy[p] * dt
        z[p] += vz[p] * dt
        pushMatrix()
        rotateX(radians((height/2)-mouseY))
        rotateY(radians(mouseX-(width/2)))
        translate(x[p],y[p],z[p])
        if mousePressed:
            strokeWeight(2)
            stroke(c[p])
            line(0,0,0,vt.x,vt.y,vt.z)
        fill(c[p])
        stroke(225)
        strokeWeight(0.1)
        sphere(r[p])
        popMatrix()
    if mousePressed:
        pushMatrix()
        fill(255)
        text("Total p: " + str(tot_p), 10-width/2 , 20-height/2)
        popMatrix()
    pushMatrix()
    translate(-width/2 + 25,height/2 - 25,0)
    rotateX(radians((height/2)-mouseY))
    rotateY(radians(mouseX-(width/2)))
    strokeWeight(2)
    stroke(255,0,0)
    line(0,0,0,20,0,0)
    stroke(0,255,0)
    line(0,0,0,0,20,0)
    stroke(0,0,255)
    line(0,0,0,0,0,20)
    popMatrix()

def get_vector(a):
    global x, y, z, vt, m, g, va, dt
    vt.set(0,0,0)
    for p in range(0,n):
        if a != p:
            va.set(x[p]-x[a],y[p]-y[a],z[p]-z[a])
            d = va.mag()
            f = (g * m[p] * 1000)/(d**2 + 10)
            va.setMag(f)
            vt.add(va)