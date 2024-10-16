import requests
import machine
import time

adc = machine.ADC(33,atten=machine.ADC.ATTN_11DB)

# Test the soil meter with a cup of water to get x_max value.  Notice that the
#max value is LOWER than the min value.  Set the x_min value based on what the
#meter reads when its just in the air.  #Use the additional plus/minus value in
#x_min to adjust the reading closer to what a moisture meter says
x_min = 49000 -12000
x_max = 20200
y_min = 0
y_max = 100


def linear_scale(x, x_min, x_max, y_min, y_max):
    """
    Scales a value from one range to another linearly.
    """
    if x >= x_min:
        return 0.0
    if x <= x_max:
        return 100.0
    return (y_max - y_min) * (x - x_min) / (x_max - x_min) + y_min

while True:
    result = linear_scale(adc.read_u16(), x_min, x_max, y_min, y_max)
    print(result)
    print(adc.read_u16())
    time.sleep(1)

