import math

#  --- CONSTANTS --- 
# gravitation parameters
us = 132712440000 # sol gravitational parameter
ume = 22032
uv = 324859
ue = 398600
um = 42828
uj = 126686534
usa = 37931187
uu = 5793939
un = 6836529

# planet radii
rme = 2439
rv = 6051
re = 6378
rm = 3389
rj = 69911
rs = 58232
ru = 25362
rn = 24622

# orbital radius of all planets around sol
rmes = 57909227
rvs = 108209475
res = 149597870
rms = 227943824
rjs = 778340821
rss = 1426666422
rus = 2870658186
rns = 4498396441

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

    # delta v calc
    dv = abs(vdep - v1s)

    # round to 2dp
    dv = round(dv, 2)
    t = round(t, 2)
    ty = round(ty, 2)

    ClearScreen()
    print("This transfer will cost: " + str(dv) + "km/s and will take:", t, "days (" + str(ty) + " years)")
    input()

def PlanetChoice():
    ClearScreen()
    print("\n\nChoose planet: \na) Mercury, \nb) Venus, \nc) Earth, \nd) Mars, \ne) Jupiter, \nf) Saturn, \ng) Uranus, \nh) Neptune")
    plan = input().lower()
    if (plan == "a"):
        return rmes
    elif (plan == "b"):
        return rvs
    elif (plan == "c"):
        return res
    elif (plan == "d"):
        return rms
    elif (plan == "e"):
        return rjs
    elif (plan == "f"):
        return rss
    elif (plan == "g"):
        return rus
    elif (plan == "h"):
        return rns

def SinglePlanetChoice():
    ClearScreen()
    rf = float(input("Enter first orbit altitude: (km) "))
    rs = float(input("Enter second orbit altitude: (km) "))
    ClearScreen()

    print("\n\nChoose planet: \na) Mercury, \nb) Venus, \nc) Earth, \nd) Mars, \ne) Jupiter, \nf) Saturn, \ng) Uranus, \nh) Neptune \ni) Custom")
    plan = input().lower()
    if (plan == "a"):
        SinglePlanet(rf, rs, ume, rme)
    elif (plan == "b"):
        SinglePlanet(rf, rs, uv, rv)
    elif (plan == "c"):
        SinglePlanet(rf, rs, ue, re)
    elif (plan == "d"):
        SinglePlanet(rf, rs, um, rm)
    elif (plan == "e"):
        SinglePlanet(rf, rs, uj, rj)
    elif (plan == "f"):
        SinglePlanet(rf, rs, usa, rs)
    elif (plan == "g"):
        SinglePlanet(rf, rs, uu, ru)
    elif (plan == "h"):
        SinglePlanet(rf, rs, un, rn)
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

        InterplanetaryTransfer(p1, p2, us)

    elif (transfer.lower() == "q"):
        run = False

    else:
        print(transfer, "not recognised...\n\n\n")


while run == True:
    Menu()