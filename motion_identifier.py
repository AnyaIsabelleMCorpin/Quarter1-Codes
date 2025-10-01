# Motion Type Identifier Template
 

# Function 1: Convert velocity to m/s

def convert_velocity(value, unit):

    """

    Convert velocity to meters per second (m/s)

    Supported units: m/s, ft/s, km/s, mi/s

    """
def convert_velocity(v_value, v_unit):
    if v_unit == "m/s":
        return v_value
    elif v_unit == "ft/s":
        return v_value/3.281
    elif v_unit == "km/s":
        return v_value*1000
    else:
        return v_value*1609

# Function 2: Convert acceleration to m/s²

def convert_acceleration(value, unit):

    """

    Convert acceleration to meters per second squared (m/s²)

    Supported units: m/s², ft/s², km/s², mi/s²

    """
def convert_acceleration(a_value, a_unit):
    if a_unit == "m/s":
        return a_value
    elif a_unit == "ft/s":
        return a_value/3.281
    elif a_unit == "km/s":
        return a_value*1000
    else:
        return a_value*1609

# Function 3: Determine motion type

def motion_type(v, a):

    """

    Determine the type of motion based on velocity and acceleration
''
    Rules:

    - v > 0 and a = 0 → "Uniform Motion"

    - v > 0 and a > 0 → "Accelerated Motion"

    - v > 0 and a < 0 → "Decelerated Motion"

    - v = 0 → "At Rest"

    """
def motion_type(v_si, a_si):
    if v_si > 0 and a_si == 0:
        return "Uniform_Motion"
    elif v_si > 0 and a_si > 0:
        return "Accelerated_Motion"
    elif v_si > 0 and a_si < 0:
        return "Decelerated_Motion"
    else:
        return "At_Rest"

# --- Main Program ---

# Step 1: Input velocity
v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

# Step 2: Input acceleration
a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

# Step 3: Convert to SI units
v_si = convert_velocity(v_value, v_unit)
a_si = convert_acceleration(a_value, a_unit)

# Step 4: Determine motion type
motion = motion_type(v_si, a_si)
 
# Step 5: Display results

print("\n--- Results ---")
print(f"Velocity = {v_si:.3f} m/s")
print(f"Acceleration = {a_si:.3f} m/s²")
print(f"Motion Type = {motion}")