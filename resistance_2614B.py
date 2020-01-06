import visa

# VISA接続
rm = visa.ResourceManager()
print(rm.list_resources())
smu = rm.open_resource('USB0::0x05E6::0x2614::4045691::0::INSTR')
print('SOURCE METER IDN = ' + smu.query('*IDN?'))

# Restore Series 2600B defaults
smu.write('smua.reset()')
# Select voltage source function
smu.write('smua.source.func = smua.OUTPUT_DCVOLTS')
# Set source range to auto
smu.write('smua.source.autorangev = smua.AUTORANGE_ON')
# Set voltage source to 3.3V
smu.write('smua.source.levelv = 3.3')
# Set current range to 100mA
smu.write('smua.source.limiti = 100e-3')
# Set current range to 100mA
smu.write('smua.measure.rangei = 100e-3')
# Turn on output
smu.write('smua.source.output = smua.OUTPUT_ON')
# Read measurement values
print('V = ' + smu.query('print(smua.measure.v())'))
print('I = ' + smu.query('print(smua.measure.i())'))
print('R = ' + smu.query('print(smua.measure.r())'))
print('P = ' + smu.query('print(smua.measure.p())'))
# Turn off output
smu.write('smua.source.output = smua.OUTPUT_OFF')