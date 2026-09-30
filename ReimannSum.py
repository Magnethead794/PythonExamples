import csv

engine_revolutions = 0
driveshaft_revolutions = 0
fuel_used = 0

old_time = None
old_engine_rpm = None
old_driveshaft_rpm = None
old_fuel_flow = None

with open("0513tmp2r.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        time = float(row[0])

        engine_rpm = float(row[1])

        driveshaft_rpm = float(row[2])

        fuel_flow = float(row[3])

        # First point only establishes a starting point
        if old_time is None:

            old_time = time
            old_engine_rpm = engine_rpm
            old_driveshaft_rpm = driveshaft_rpm
            old_fuel_flow = fuel_flow

            continue

        dt = time - old_time

        # ENGINE RPM
        engine_area = (
            old_engine_rpm * dt
            + ((engine_rpm - old_engine_rpm) / 2) * dt
        )

        # DRIVESHAFT RPM
        driveshaft_area = (
            old_driveshaft_rpm * dt
            + ((driveshaft_rpm - old_driveshaft_rpm) / 2) * dt
        )

        # FUEL FLOW
        fuel_area = (
            old_fuel_flow * dt
            + ((fuel_flow - old_fuel_flow) / 2) * dt
        )

        engine_revolutions += engine_area
        driveshaft_revolutions += driveshaft_area
        fuel_used += fuel_area

        old_time = time
        old_engine_rpm = engine_rpm
        old_driveshaft_rpm = driveshaft_rpm
        old_fuel_flow = fuel_flow

# Convert RPM-based integrals into actual revolutions
engine_revolutions /= 60
driveshaft_revolutions /= 60

# Convert gallons/minute into gallons
fuel_used /= 60

print("Engine Revolutions:", engine_revolutions)
print("Driveshaft Revolutions:", driveshaft_revolutions)
print("Fuel Used (gal):", fuel_used)