#!/usr/bin/env python3
"""
Test script for E6B calculations
Run this to verify the E6B computer is working correctly
"""

from e6b_computer import E6BComputer

def test_wind_correction():
    """Test wind correction calculation"""
    print("=" * 60)
    print("TEST: Wind Correction Angle and Groundspeed")
    print("=" * 60)

    e6b = E6BComputer()

    # Example from user's request
    true_course = 180
    true_airspeed = 110
    wind_direction = 220
    wind_speed = 15

    wca, gs = e6b.wind_correction(true_course, true_airspeed, wind_direction, wind_speed)

    print(f"True Course: {true_course}°")
    print(f"True Airspeed: {true_airspeed} knots")
    print(f"Wind: {wind_direction}° at {wind_speed} knots")
    print(f"\nResults:")
    print(f"  Wind Correction Angle: {wca}°")
    print(f"  Groundspeed: {gs} knots")
    print()

def test_density_altitude():
    """Test density altitude calculation"""
    print("=" * 60)
    print("TEST: Density Altitude")
    print("=" * 60)

    e6b = E6BComputer()

    pressure_alt = 5000
    oat = 25

    density_alt = e6b.density_altitude(pressure_alt, oat)

    print(f"Pressure Altitude: {pressure_alt} ft")
    print(f"Outside Air Temperature: {oat}°C")
    print(f"\nResults:")
    print(f"  Density Altitude: {density_alt} ft")
    print()

def test_fuel_burn():
    """Test fuel burn calculation"""
    print("=" * 60)
    print("TEST: Fuel Burn and Time En Route")
    print("=" * 60)

    e6b = E6BComputer()

    gph = 8
    distance = 200
    groundspeed = 130

    time_minutes, fuel_gallons = e6b.fuel_burn(gph, distance, groundspeed)

    print(f"Fuel Burn Rate: {gph} GPH")
    print(f"Distance: {distance} nm")
    print(f"Groundspeed: {groundspeed} knots")
    print(f"\nResults:")
    print(f"  Time En Route: {time_minutes} minutes ({time_minutes/60:.2f} hours)")
    print(f"  Fuel Required: {fuel_gallons} gallons")
    print()

def test_true_airspeed():
    """Test TAS estimation"""
    print("=" * 60)
    print("TEST: True Airspeed Estimate")
    print("=" * 60)

    e6b = E6BComputer()

    ias = 100
    altitude = 6000

    tas = e6b.true_airspeed_estimate(ias, altitude)

    print(f"Indicated Airspeed: {ias} knots")
    print(f"Altitude: {altitude} ft")
    print(f"\nResults:")
    print(f"  True Airspeed: {tas} knots")
    print()

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("E6B COMPUTER TEST SUITE")
    print("=" * 60 + "\n")

    test_wind_correction()
    test_density_altitude()
    test_fuel_burn()
    test_true_airspeed()

    print("=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)
