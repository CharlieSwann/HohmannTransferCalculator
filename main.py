import math

#  --- CONSTANTS --- 

bodyNames = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Sun"]
# gravitation parameters
gravParams = [22032, 324859, 398600, 42828, 126686534, 37931187, 5793939, 6836529, 132712440000]

# planet radii
radii = [2439, 6051, 6378, 3389, 69911, 58232, 25362, 24622]

# orbital radius of all planets around sol
orbitRads = [57909227, 108209475, 149597870, 227943824, 778340821, 1426666422, 2870658186, 4498396441]

run = True

def ClearScreen():
    print("\n" * 100)

def SinglePlanet(r1, r2, u, rp):
    # add planets radius to orbit altitude
    r1 += rp
    r2 += rp

    # first find orbit speeds
    v1 = math.sqrt(u/r1)
    v2 = math.sqrt(u/r2)

    # first burn delta v calculation
    a = (r1 + r2) / 2 # semi major axis
    vf = math.sqrt(u * ((2/r1)-(1/a))) # vis viva equation

    dv1 = abs(vf - v1)

    # second burn delta v calculation
    vs = math.sqrt(u * ((2/r2)-(1/a))) # vis viva equation

    dv2 = abs(vs - v2)

    # total delta v:
    dv = dv1 + dv2

    # transfer time (keplers third law)
    t = math.pi * math.sqrt((a*a*a)/u)
    th = t/3600 # convert to hours
    t = t/86400 # convert to days

    # convert to m/s if less than 1km/s
    dv1str = "km/s"
    dv2str = "km/s"
    dvstr = "km/s"
    if (dv1 < 1): 
        dv1 *= 1000 
        dv1str = "m/s"
    if (dv2 < 1): 
        dv2 *= 1000
        dv2str = "m/s"
    if (dv < 1): 
        dv *= 1000
        dvstr = "m/s"

    # round to 2dp
    dv = round(dv, 2)
    dv1 = round(dv1, 2)
    dv2 = round(dv2, 2)
    t = round(t, 2)
    th = round(th, 2)

    

    ClearScreen()
    print("delta v for first burn (Perigee boost): " + str(dv1) + dv1str)
    print("delta v for second burn (Circularization): " + str(dv2) + dv2str)
    print("This transfer will cost: " + str(dv) + dvstr + " total and will take:", t, "days, (" + str(th) + " hours)")
    input()

def InterplanetaryTransfer(rp1, rp2, u):
    # planets orbit vel around sol
    v1s = math.sqrt(u/rp1)
    v2s = math.sqrt(u/rp2)

    # semi major axis
    a = (rp1+rp2) / 2

    # transfer time (keplers third law)
    t = math.pi * math.sqrt((a*a*a)/u)
    t = t/86400 # convert to days
    ty = t/365 # convert to years

    # departure and arrival velocity
    vdep = math.sqrt(u * ((2/rp1)-(1/a))) # vis viva
    varr = math.sqrt(u * ((2/rp2)-(1/a))) 

    # Hyperbolic excess speed relative to the destination planet
    vinf = abs(varr - v2s)

    # delta v calc
    dv = abs(vdep - v1s)

    # angle calc
    ang = 180 * (1 - pow(((rp1 + rp2) / (2*rp2)), (3/2)))

    # round to 2dp
    dv = round(dv, 2)
    t = round(t, 2)
    ty = round(ty, 2)
    ang = round(ang, 2)

    ClearScreen()
    print("This transfer will cost: " + str(dv) + "km/s and will take:", t, "days (" + str(ty) + " years)")
    print("The transfer angle is: " + str(ang) + "°")
    alt = float(input("Enter altitude for circularisation: (km) "))
    ind = orbitRads.index(rp2)
    r = alt + float(radii[ind])
    ClearScreen()

    # find speed at periapsis
    vp = math.sqrt(vinf**2 + (2*gravParams[ind]/r))
    vdes = math.sqrt(gravParams[ind]/r)

    vcir = vp-vdes
    print("Delta V for circularisation: " + str(round(vcir, 2)) + "km/s")
    input()

def PlanetChoice():
    ClearScreen()
    print("\n\nChoose planet: \na) Mercury, \nb) Venus, \nc) Earth, \nd) Mars, \ne) Jupiter, \nf) Saturn, \ng) Uranus, \nh) Neptune")
    plan = input().lower()
    if (plan == "a"):
        return orbitRads[0]
    elif (plan == "b"):
        return orbitRads[1]
    elif (plan == "c"):
        return orbitRads[2]
    elif (plan == "d"):
        return orbitRads[3]
    elif (plan == "e"):
        return orbitRads[4]
    elif (plan == "f"):
        return orbitRads[5]
    elif (plan == "g"):
        return orbitRads[6]
    elif (plan == "h"):
        return orbitRads[7]

def SinglePlanetChoice():
    ClearScreen()
    rf = float(input("Enter first orbit altitude: (km) "))
    rs = float(input("Enter second orbit altitude: (km) "))
    ClearScreen()

    print("\n\nChoose planet: \na) Mercury, \nb) Venus, \nc) Earth, \nd) Mars, \ne) Jupiter, \nf) Saturn, \ng) Uranus, \nh) Neptune \ni) Custom")
    plan = input().lower()
    if (plan == "a"):
        SinglePlanet(rf, rs, gravParams[0], radii[0])
    elif (plan == "b"):
        SinglePlanet(rf, rs, gravParams[1], radii[1])
    elif (plan == "c"):
        SinglePlanet(rf, rs, gravParams[2], radii[2])
    elif (plan == "d"):
        SinglePlanet(rf, rs, gravParams[3], radii[3])
    elif (plan == "e"):
        SinglePlanet(rf, rs, gravParams[4], radii[4])
    elif (plan == "f"):
        SinglePlanet(rf, rs, gravParams[5], radii[5])
    elif (plan == "g"):
        SinglePlanet(rf, rs, gravParams[6], radii[6])
    elif (plan == "h"):
        SinglePlanet(rf, rs, gravParams[7], radii[7])
    elif (plan == "i"):
        u = float(input("Enter planets gravitational parameter: "))
        r = float(input("Enter planets radius: "))
        SinglePlanet(rf, rs, u, r)

def Menu():
    global run
    ClearScreen()
    print("----- Hohmann Transfer Calculator -----")
    print("Would you like to calculate: \n1) Single Planet orbit transfer (eg. LEO -> GEO) \n2) Interplanetary transfer \nQ) Quit program")
    transfer = input()
    if (transfer == "1"):
        SinglePlanetChoice()

    elif (transfer == "2"):
        p1 = PlanetChoice()
        p2 = PlanetChoice()

        InterplanetaryTransfer(p1, p2, gravParams[8])

    elif (transfer.lower() == "q"):
        run = False

    else:
        print(transfer, "not recognised...\n\n\n")


while run == True:
    Menu()