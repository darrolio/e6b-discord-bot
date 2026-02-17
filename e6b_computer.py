import math

class E6BComputer:
    def __init__(self):
        self.isa_temp_at_sea_level = 15  # Celsius
        self.lapse_rate = 2  # Celsius per 1000 ft

    def wind_correction(self, true_course, true_airspeed, wind_direction, wind_speed):
        """Calculates Wind Correction Angle (WCA) and Groundspeed (GS)."""
        # Convert degrees to radians for math functions
        tc_rad = math.radians(true_course)
        wd_rad = math.radians(wind_direction)

        # Wind Correction Angle Formula
        wca_rad = math.asin((wind_speed * math.sin(wd_rad - tc_rad)) / true_airspeed)
        wca_deg = math.degrees(wca_rad)

        # Groundspeed Formula
        gs = math.sqrt(true_airspeed**2 + wind_speed**2 -
                       (2 * true_airspeed * wind_speed * math.cos(tc_rad - wd_rad + wca_rad)))

        return round(wca_deg, 1), round(gs, 1)

    def density_altitude(self, pressure_alt, oat):
        """Calculates Density Altitude based on Pressure Altitude and Outside Air Temp."""
        # Calculate standard temperature (ISA) for the given altitude
        isa_temp = self.isa_temp_at_sea_level - (self.lapse_rate * (pressure_alt / 1000))
        # Rule of thumb: 120ft per degree Celsius deviation from ISA
        density_alt = pressure_alt + (120 * (oat - isa_temp))
        return round(density_alt)

    def fuel_burn(self, gph, distance, groundspeed):
        """Calculates time en route and total fuel needed."""
        time_hours = distance / groundspeed
        total_fuel = gph * time_hours
        return round(time_hours * 60, 1), round(total_fuel, 2)  # minutes, gallons

    def true_airspeed_estimate(self, ias, altitude):
        """Standard rule of thumb: TAS increases 2% per 1000ft of altitude."""
        tas = ias * (1 + (0.02 * (altitude / 1000)))
        return round(tas)

# Example Usage:
# e6b = E6BComputer()
# print(e6b.wind_correction(true_course=090, true_airspeed=120, wind_direction=045, wind_speed=20))
