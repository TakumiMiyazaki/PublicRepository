import visa

rm = visa.ResourceManager()
print(rm.list_resources())

WaveGen_81180B = rm.open_resource('USB1::0x0957::0xA918::IL51420125::0::INSTR')
print(WaveGen_81180B.query('*IDN?'))

# Initialize Wave Generator
WaveGen_81180B.write('*CLS')
WaveGen_81180B.write('*RST')
# Wave Generator CH1
WaveGen_81180B.write(':INST:SEL 1')                     # Select CH1
WaveGen_81180B.write(':SOUR:FUNC:SHAP SQU')             # Wace Shape : Square
WaveGen_81180B.write(':SOUR:FUNC:SHAP:SQU:DCYC 50.00')  # Duty : 50%
WaveGen_81180B.write(':SOUR:FREQ 100e3')                # Frequency 100kHz
WaveGen_81180B.write(':SOUR:VOLT:AMPL 800e-3')          # Amplitude 800mVpp
WaveGen_81180B.write(':SOUR:VOLT:OFFS 0')               # Offset 0Vdc
WaveGen_81180B.write(':OUTP:COUP DC')                   # Output Coumling DC
# Wave Generator CH2
WaveGen_81180B.write(':INST:SEL 2')                     # Select CH2
WaveGen_81180B.write(':SOUR:FUNC:SHAP SQU')             # Wace Shape : Square
WaveGen_81180B.write(':SOUR:FUNC:SHAP:SQU:DCYC 50.00')  # Duty : 50%
WaveGen_81180B.write(':SOUR:FREQ 10e6')                 # Frequency 10MHz
WaveGen_81180B.write(':SOUR:VOLT:AMPL 800e-3')          # Amplitude 800mVpp
WaveGen_81180B.write(':SOUR:VOLT:OFFS 0')               # Offset 0Vdc
WaveGen_81180B.write(':OUTP:COUP DC')                   # Output Coumling DC

# Wave Generator OUTPUT
WaveGen_81180B.write(':INST:SEL 1')  # Select CH1
WaveGen_81180B.write(':OUTP ON')     # Output
WaveGen_81180B.write(':INST:SEL 2')  # Select CH2
WaveGen_81180B.write(':OUTP ON')     # Output