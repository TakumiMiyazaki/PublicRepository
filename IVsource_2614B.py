import visa
from time import sleep

# VISA接続
rm = visa.ResourceManager()
print(rm.list_resources())
smu = rm.open_resource('TCPIP0::192.168.60.23::inst0::INSTR')
print('SOURCE METER IDN = ' + smu.query('*IDN?'))

# Channel A 定電圧源動作
#     出力電圧 3.3V
#     電流制限 10mA
smu.write('smua.reset()')
smu.write('smua.source.func = smua.OUTPUT_DCVOLTS')
smu.write('smua.source.autorangev = smua.AUTORANGE_ON')
smu.write('smua.source.levelv = 3.3')
smu.write('smua.source.limiti = 10e-3')
smu.write('display.smua.measure.func = display.MEASURE_DCAMPS')

# Channel B 定電流源動作
#     出力電流 1mA
#     電圧制限 1V
smu.write('smub.reset()')
smu.write('smub.source.func = smub.OUTPUT_DCAMPS')
smu.write('smub.source.autorangev = smub.AUTORANGE_ON')
smu.write('smub.source.leveli = 1.0e-3')
smu.write('smub.source.limitv = 1.0')
smu.write('display.smub.measure.func = display.MEASURE_DCVOLTS')

smu.write('display.screen = display.SMUA_SMUB')

# Turn on output
smu.write('smua.source.output = smua.OUTPUT_ON')
smu.write('smub.source.output = smub.OUTPUT_ON')
sleep(10)
smu.write('smua.source.output = smua.OUTPUT_OFF')
smu.write('smub.source.output = smub.OUTPUT_OFF')