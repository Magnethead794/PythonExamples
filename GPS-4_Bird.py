import math

# Speed of light (m/s)
c = 299_792_458

# Satellite positions
satellites = [
    ("SAT1", 0,    0,    0.000007447),
    ("SAT2", 5000, 0,    0.000013839),
    ("SAT3", 0,    5000, 0.000011652),
    ("SAT4", 5000, 5000, 0.000016304)
]

print("Satellite Distances")
print("-------------------")

for sat in satellites:

    name = sat[0]
    x = sat[1]
    y = sat[2]
    transit_time = sat[3]

    distance = c * transit_time

    print(
        f"{name}: ({x},{y}) "
        f"Distance = {distance:.1f} meters"
    )
