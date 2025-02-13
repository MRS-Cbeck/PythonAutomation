import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
# Create a Root Window title and dimensions
root.title("Sales Integration Sheet")
# Set Geometry (widthxheight)
root.geometry("850x850")
content = ttk.Frame(root)
# Configure the grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=3)

scrollbar = ttk.Scrollbar(root)
content.config()








# Function to decide the combo box values
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def combo_values(event):
    selected_rollformer = rollformer_type_combobox.get()
    selected_voltage = voltage_combobox.get()
    if selected_rollformer.startswith('Titan'):
        if selected_rollformer.endswith('16 Pass'):
            if selected_voltage == '240V 3-Phase' or  '480V 3-Phase':
                controller_combobox['values'] = ('AMS', 'ELO', 'BECK')
            else:
                controller_combobox['values'] = ('AMS', 'ELO', 'BECK', 'TRI PLC')
    elif selected_rollformer.startswith('Signature'):
        controller_combobox['values'] = ('AMS', 'ELO', 'BECK')


# Function to decide the motor drive value
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def rf_value(rf, dir, lp, up):
    if 'Tuff Rib' in lp or 'Quad Rib' in lp or 'Tuff Rib' in up or 'Quad Rib' in up:
        if dir == 'Standard':
            result = 'TRFA-2505 (STD)'
        else:
            result = 'TRFA-2505 (REV)'
    # Titan Rollformers
    # Single Deck Rollformers
    elif rf.startswith('Titan I '):
        result = singleTitan_motorDrive_value(dir, rf)
    # Double Deck Rollformers
    elif rf.startswith('Titan II '):
        result = doubleTitan_motorDrive_value(dir, rf)
    # Signature Rollformers
    elif rf.startswith('Signature '):
        result = signature_motorDrive_value(dir, rf)
    # Patriot Rollformers
    elif rf.startswith('Patriot '):
        result = patriot_motorDrive_value(dir, rf)
    else:
        result = 'Invalid Rollformer Type'
    return result
# end of rf_value() function


# Single Titan - No Quad or Tuff Rib profiles
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def singleTitan_motorDrive_value(direction, rf_type):
    if rf_type.endswith('16 Pass'):
        switch={
            'Standard' : 'TRFA-2501 (STD)',
            'Reverse' : 'TRFA-2501 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('18 Pass'):
        switch={
            'Standard' : 'TRFA-2503 (STD)',
            'Reverse' : 'TRFA-2503 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('20 Pass'):
        switch={
            'Standard' : 'TRFA-2503 (STD)',
            'Reverse' : 'TRFA-2503 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('21 Pass'):
        switch={
            'Standard' : 'TRFA-2503 (STD)',
            'Reverse' : 'TRFA-2503 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('24 Pass'):
        switch={
            'Standard' : 'TRFA-1403 (STD)',
            'Reverse' : 'TRFA-1403 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('25 Pass'):
        switch={
            'Standard' : 'TRFA-1403 (STD)',
            'Reverse' : 'TRFA-1403 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
# end of singleTitan_motorDrive_value() function


# Double Deck Titan - No Quad or Tuff Rib profiles
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def doubleTitan_motorDrive_value(direction, rf_type):
    if rf_type.endswith('16 Pass'):
        switch={
            'Standard' : 'TRFA-2502 (STD)',
            'Reverse' : 'TRFA-2502 (REV)'
        }
        results = switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('18 Pass'):
        switch={
            'Standard' : 'TRFA-2504 (STD)',
            'Reverse' : 'TRFA-2504 (REV)'
        }
        results = switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('20 Pass'):
        switch={
            'Standard' : 'TRFA-2504 (STD)',
            'Reverse' : 'TRFA-2504 (REV)'
        }
        results = switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('21 Pass'):
        switch={
            'Standard' : 'TRFA-2507 (STD)',
            'Reverse' : 'NEEDS DESIGN'
        }
        results = switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('24 Pass'):
        switch={
            'Standard' : 'TRFA-1402 (STD)',
            'Reverse' : 'TRFA-1402 (REV)'
        }
        results = switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('25 Pass'):
        switch={
            'Standard' : 'TRFA-1402 (STD)',
            'Reverse' : 'TRFA-1402 (REV)'
        }
        results = switch.get(direction, 'Invalid Direction')
    return results
# end of doubleTitan_motorDrive_value() function



# Signature Rollformer - No Quad or Tuff Rib profiles
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def signature_motorDrive_value(direction, rf_type):
    if rf_type.endswith('I'):
        switch={
            'Standard' : 'TRFA-2501 (STD)',
            'Reverse' : 'TRFA-2501 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('II'):
        switch={
            'Standard' : 'TRFA-2502 (STD)',
            'Reverse' : 'TRFA-2502 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
# end of signature_motorDrive_value() function



# Patriot Rollformer - No Quad or Tuff Rib profiles
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def patriot_motorDrive_value(direction, rf_type):
    if rf_type.endswith('Electric'):
        switch={
            'Standard' : 'TRFA-2501 (STD)',
            'Reverse' : 'TRFA-2501 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
    elif rf_type.endswith('Hydraulic'):
        switch={
            'Standard' : 'TRFA-2501 (STD)',
            'Reverse' : 'TRFA-2501 (REV)'
        }
        return switch.get(direction, 'Invalid Direction')
# end of patriot_motorDrive_value() function


# Create label widgets
# -----------------------------------------------------------------------------------------------------------------------------------------------------
company_name = tk.Label(content, text="Company Name", padx=5, pady=5)
company_name.grid(row=1, column=0, padx=5, pady=5)

company_location = tk.Label(root, text="Company Location", padx=5, pady=5)
company_location.grid(row=2, column=0, padx=5, pady=5)

job_location = tk.Label(root, text="Job Location", padx=5, pady=5)
job_location.grid(row=3, column=0, padx=5, pady=5)

contract_date = tk.Label(root, text="Contract Date", padx=5, pady=5)
contract_date.grid(row=4, column=0, padx=5, pady=5)

rollformer_type = tk.Label(root, text="Rollformer Type", padx=5, pady=5)
rollformer_type.grid(row=5, column=0, padx=5, pady=5)

serial_number = tk.Label(root, text="Serial Number", padx=5, pady=5)
serial_number.grid(row=6, column=0, padx=5, pady=5)

direction = tk.Label(root, text="Direction", padx=5, pady=5)
direction.grid(row=7, column=0, padx=5, pady=5)

voltage = tk.Label(root, text="Voltage", padx=5, pady=5)
voltage.grid(row=8, column=0, padx=5, pady=5)

controller = tk.Label(root, text="Controller", padx=5, pady=5)
controller.grid(row=9, column=0, padx=5, pady=5)

label_printer = tk.Label(root, text="Label Printer", padx=5, pady=5)
label_printer.grid(row=10, column=0, padx=5, pady=5)

lubricator = tk.Label(root, text="Lubricator", padx=5, pady=5)
lubricator.grid(row=11, column=0, padx=5, pady=5)

lower_profile = tk.Label(root, text="Lower Profile", padx=5, pady=5)
lower_profile.grid(row=12, column=0, padx=5, pady=5)

upper_profile = tk.Label(root, text="Upper Profile", padx=5, pady=5)
upper_profile.grid(row=13, column=0, padx=5, pady=5)

guidetype = tk.Label(root, text="Guide Type", padx=5, pady=5)
guidetype.grid(row=14, column=0, padx=5, pady=5)

feedtable = tk.Label(root, text="FeedTable Length")
feedtable.grid(row=15, column=0, padx=5, pady=5)

feedguide = tk.Label(root, text="Feedtable Guide")
feedguide.grid(row=16, column=0, padx=5, pady=5)

sheartype = tk.Label(root, text="Shear Type")
sheartype.grid(row=16, column=0, padx=5, pady=5)

shearguide = tk.Label(root, text="Shear Guide")
shearguide.grid(row=17, column=0, padx=5, pady=5)

filmapp = tk.Label(root, text="Film Applicator")
filmapp.grid(row=18, column=0, padx=5, pady=5)

decoiltype = tk.Label(root, text="Decoiler Type")
decoiltype.grid(row=19, column=0, padx=5, pady=5)

serial_number2 = tk.Label(root, text="Decoiler Serial #")
serial_number2.grid(row=20, column=0, padx=5, pady=5)

decoildirection = tk.Label(root, text="Decoiler Direction")
decoildirection.grid(row=21, column=0, padx=5, pady=5)

decoilVoltage = tk.Label(root, text="Decoiler Voltage")
decoilVoltage.grid(row=22, column=0, padx=5, pady=5)

controls = tk.Label(root, text="Controls")
controls.grid(row=23, column=0, padx=5, pady=5)

track = tk.Label(root, text="Track")
track.grid(row=24, column=0, padx=5, pady=5)

accOne = tk.Label(root, text="Accesory 1")
accOne.grid(row=25, column=0, padx=5, pady=5)

accTwo = tk.Label(root, text="Accesory 2")
accTwo.grid(row=26, column=0, padx=5, pady=5)

# Create entry and combobox widgets
# -----------------------------------------------------------------------------------------------------------------------------------------------------
company_name_entry = tk.Entry(root, width=50)
company_name_entry.grid(row=1, column=1, padx=5, pady=5)

company_location_entry = tk.Entry(root, width=50)
company_location_entry.grid(row=2, column=1, padx=5, pady=5)

job_location_entry = tk.Entry(root, width=50)
job_location_entry.grid(row=3, column=1, padx=5, pady=5)

contract_date_entry = tk.Entry(root, width=50)
contract_date_entry.grid(row=4, column=1, padx=5, pady=5)

rollformer_type_combobox = ttk.Combobox(root, width=47)
rollformer_type_combobox['values'] = ('Titan I 16 Pass', 'Titan II 16 Pass', 'Titan I 18 Pass', 'Titan II 18 Pass', 'Titan I 20 Pass', 'Titan II 20 Pass', 
'Titan I 21 Pass', 'Titan II 21 Pass', 'Titan I 24 Pass', 'Titan II 24 Pass', 'Titan I 25 Pass', 'Titan II 25 Pass', 'Signature I', 'Signature II', 
'Patriot I Electric', 'Patriot II Electric', 'Patriot I Hydraulic', 'Patriot II Hydraulic', 'Patriot S/D Electric', 'Patriot S/D Hydraulic')
rollformer_type_combobox.grid(row=5, column=1, padx=5, pady=5)

serial_number_entry = tk.Entry(root, width=50)
serial_number_entry.grid(row=6, column=1, padx=5, pady=5)

direction_combobox = ttk.Combobox(root, width=47)
direction_combobox['values'] = ('Standard', 'Reverse')
direction_combobox.grid(row=7, column=1, padx=5, pady=5)

voltage_combobox = ttk.Combobox(root, width=47)
voltage_combobox['values'] = ('240V 3-Phase', '480V 3-Phase', '24V DC (Hydraulic)')
voltage_combobox.grid(row=8, column=1, padx=5, pady=5)
voltage_combobox.bind('<<ComboboxSelected>>', combo_values)

controller_combobox = ttk.Combobox(root, width=47)
controller_combobox['values'] = ('AMS', 'ELO', 'BECK', 'TRI PLC')
controller_combobox.grid(row=9, column=1, padx=5, pady=5)

label_printer_combobox = ttk.Combobox(root, width=47)
label_printer_combobox['values'] = ('NO', 'Zebra', 'Eltron', 'Sato')
label_printer_combobox.grid(row=10, column=1, padx=5, pady=5)

lubricator_combobox = ttk.Combobox(root, width=47)
lubricator_combobox['values'] = ('NO', 'Manual', 'Photo-Eye')
lubricator_combobox.grid(row=11, column=1, padx=5, pady=5)

lower_profile_combobox = ttk.Combobox(root, width=47)
lower_profile_combobox['values'] = ('3/4\" Tuff Rib (WIDE MINORS)', '3/4"" Tuff Rib (STD MINORS)', 'R3')
lower_profile_combobox.grid(row=12, column=1, padx=5, pady=5)

upper_profile_combobox = ttk.Combobox(root, width=47)
upper_profile_combobox['values'] = ('3/4\" Tuff Rib (WIDE MINORS)', '3/4"" Tuff Rib (STD MINORS)', 'R3', '1\" Quad Rib', 'Master Rib')
upper_profile_combobox.grid(row=13, column=1, padx=5, pady=5)

guidetype_combobox = ttk.Combobox(root, width=47)
guidetype_combobox['values'] = ('NO', 'ANGLE', 'ROLLER')
guidetype_combobox.grid(row=14, column=1, padx=5, pady=5)

feedtable_combobox = ttk.Combobox(root, width=47)
feedtable_combobox['values'] = ('8\' FEED TABLE', '10\' FEED TABLE')
feedtable_combobox.grid(row=15, column=1, padx=5, pady=5)

feedguide_entry = tk.Entry(root, width=50)
feedguide_entry.grid(row=16, column=1, padx=5, pady=5)

sheartype_combobox = ttk.Combobox(root, width=47)
sheartype_combobox['values'] = ('NO', 'Clutch -', 'Clutch + carboxylate', '4 Post -', '4 Post + carboxylate', '4 Post HD -', 'With Leveler -')
sheartype_combobox.grid(row=16, column=1, padx=5, pady=5)

shearguide_entry = tk.Entry(root, width=50)
shearguide_entry.grid(row=17, column=1, padx=5, pady=5)

filmapp_combobox = ttk.Combobox(root, width=47)
filmapp_combobox['values'] = ('NO', 'YES')
filmapp_combobox.grid(row=18, column=1, padx=5, pady=5)

decoiltype_combobox = ttk.Combobox(root, width=47)
decoiltype_combobox['values'] = ('6TON (With Cart)', '6TON (NO CART)', '6TON (Rotating)', '10TON (With Cart)', '10TON (NO CART)')
decoiltype_combobox.grid(row=19, column=1, padx=5, pady=5)

serial_number2_entry = tk.Entry(root, width=50)
serial_number2_entry.grid(row=20, column=1, padx=5, pady=5)

decoildirection_combobox = ttk.Combobox(root, width=47)
decoildirection_combobox['values'] = ('STANDARD', 'REVERSE')
decoildirection_combobox.grid(row=21, column=1, padx=5, pady=5)

decoilVoltage_combobox = ttk.Combobox(root, width=47)
decoilVoltage_combobox['values'] = ('240V 3-Phase', '480V 3-Phase', '24V DC (Hydraulic)')
decoilVoltage_combobox.grid(row=22, column=1, padx=5, pady=5)

controls_entry = tk.Entry(root, width=50)
controls_entry.grid(row=23, column=1, padx=5, pady=5)

track_entry = tk.Entry(root, width=50)
track_entry.grid(row=24, column=1, padx=5, pady=5)

accOne_combobox = ttk.Combobox(root, width=47)
accOne_combobox['values'] = ('NO', 'Magnetic Stacker', 'Swing Arm Stacker', 'Leveler (Fixed)', 'Leveler(Tracks)', 'Rollout Table')
accOne_combobox.grid(row=25, column=1, padx=5, pady=5)

accTwo_combobox = ttk.Combobox(root, width=47)
accTwo_combobox['values'] = ('NO', 'Magnetic Stacker', 'Swing Arm Stacker', 'Leveler (Fixed)', 'Leveler(Tracks)', 'Rollout Table')
accTwo_combobox.grid(row=26, column=1, padx=5, pady=5)


# Create window to display results
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def submit():
    # Create results window
    results = tk.Tk()
    results.title("Results")
    results.geometry("600x600")
    
    # Configure the grid layout
    results.columnconfigure(0, weight=1)
    results.columnconfigure(1, weight=1)
    results.columnconfigure(2, weight=3)
    
    
    # Get values from entry widgets
    compname = company_name_entry.get()
    comLoc = company_location_entry.get()
    jobLoc = job_location_entry.get()
    contDate = contract_date_entry.get()
    rollType = rollformer_type_combobox.get()
    serNum = serial_number_entry.get()
    dir = direction_combobox.get()
    lp = lower_profile_combobox.get()
    up = upper_profile_combobox.get()
    motodrive = rf_value(rollType, dir, lp, up)
    volt = voltage_combobox.get()
    cont = controller_combobox.get()
    labelPrint = label_printer_combobox.get()
    
    # Create label widgets
    company_name2 = tk.Label(results, text="Company Name", padx=5, pady=5)
    company_name2.grid(row=1, column=0, padx=5, pady=5)
    
    company_location2 = tk.Label(results, text="Company Location", padx=5, pady=5)
    company_location2.grid(row=2, column=0, padx=5, pady=5)

    job_location2 = tk.Label(results, text="Job Location", padx=5, pady=5)
    job_location2.grid(row=3, column=0, padx=5, pady=5)

    contract_date2 = tk.Label(results, text="Contract Date", padx=5, pady=5)
    contract_date2.grid(row=4, column=0, padx=5, pady=5)

    rollformer_type2 = tk.Label(results, text="Rollformer Type", padx=5, pady=5)
    rollformer_type2.grid(row=5, column=0, padx=5, pady=5)

    serial_number2 = tk.Label(results, text="Serial Number", padx=5, pady=5)
    serial_number2.grid(row=6, column=0, padx=5, pady=5)

    direction2 = tk.Label(results, text="Direction", padx=5, pady=5)
    direction2.grid(row=7, column=0, padx=5, pady=5)

    motor_drive = tk.Label(results, text="Motor Drive", padx=5, pady=5)
    motor_drive.grid(row=8, column=0, padx=5, pady=5)
    
    voltage2 = tk.Label(results, text="Voltage", padx=5, pady=5)
    voltage2.grid(row=9, column=0, padx=5, pady=5)

    controller2 = tk.Label(results, text="Controller", padx=5, pady=5)
    controller2.grid(row=10, column=0, padx=5, pady=5)

    label_printer2 = tk.Label(results, text="Label Printer", padx=5, pady=5)
    label_printer2.grid(row=11, column=0, padx=5, pady=5)
    
    # Create entry widgets
    company_name_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    company_name_entry2.grid(row=1, column=1, padx=5, pady=5)
    
    company_location_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    company_location_entry2.grid(row=2, column=1, padx=5, pady=5)
    
    job_location_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    job_location_entry2.grid(row=3, column=1, padx=5, pady=5)
    
    contract_date_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    contract_date_entry2.grid(row=4, column=1, padx=5, pady=5)
    
    rollformer_type_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    rollformer_type_entry2.grid(row=5, column=1, padx=5, pady=5)
    
    serial_number_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    serial_number_entry2.grid(row=6, column=1, padx=5, pady=5)
    
    direction_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    direction_entry2.grid(row=7, column=1, padx=5, pady=5)
    
    motor_drive_entry = tk.Entry(results, width=50, font=('Arial', 14))
    motor_drive_entry.grid(row=8, column=1, padx=5, pady=5)
    
    voltage_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    voltage_entry2.grid(row=9, column=1, padx=5, pady=5)
    
    controller_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    controller_entry2.grid(row=10, column=1, padx=5, pady=5)
    
    label_printer_entry2 = tk.Entry(results, width=50, font=('Arial', 14))
    label_printer_entry2.grid(row=11, column=1, padx=5, pady=5)
    
    # Insert values into entry widgets
    company_name_entry2.insert(0, compname)
    company_location_entry2.insert(0, comLoc)
    job_location_entry2.insert(0, jobLoc)
    contract_date_entry2.insert(0, contDate)
    rollformer_type_entry2.insert(0, rollType)
    serial_number_entry2.insert(0, serNum)
    direction_entry2.insert(0, dir)
    motor_drive_entry.insert(0, motodrive)
    voltage_entry2.insert(0, volt)
    controller_entry2.insert(0, cont)
    label_printer_entry2.insert(0, labelPrint)


# Create a button widget
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(padx=5, pady=5)

# Run the main loop
root.mainloop()