class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = True


mon1 = Monitor
mon1.freq = 75
mon2 = Monitor
mon2.freq = 144
mon3 = Monitor
mon3.freq = 280
mon4 = Monitor
mon4.freq = 360

hd1 = Headphones
hd2 = Headphones
hd3 = Headphones
hd2.micro = True
