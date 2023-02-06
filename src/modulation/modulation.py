from modulation.BGen import BinaryGenerator
import numpy as np

########################################################################
## START ==> MODULATION EVENTS
########################################################################

def checkMessage(message: str):
    length = len(message)
    if length == 0:
        return False
    for bit in message:
        if(bit not in ["0","1"]):
            return False
    if((length in [2**i for i in range(1,6)])):
        return True
    return False
    
def modulateASK(message, Fc):
    if(checkMessage(message)):
        Fs = 32 * Fc # Sampling freq must be >>> 2 * fc (Nyquist rate)
        Fs = Fs + (Fs % len(message))
        t = np.arange(0,1,1/Fs)
        samples = Fs // len(message)

        BG = BinaryGenerator(message,samples)

        data_signal = BG.generate()
        carrier_signal = np.cos(2 * np.pi * Fc * t)

        if len(t) > len(data_signal):
            dif = len(t) - len(data_signal)
            for i in range(dif):
                data_signal = np.append(data_signal, data_signal[-1])
                
        ask_signal = carrier_signal * data_signal

        bandWidth = len(message)
        return data_signal, carrier_signal, ask_signal, t, Fs, bandWidth
    else: 
        return 0
    
def modulateFSK(message, Fc1, Fc2):
    if(checkMessage(message)):
        Fs = 32 * max( Fc1, Fc2 ) # Sampling freq must be >>> 2 * fc (Nyquist rate)
        Fs = Fs + (Fs % len(message))
        t = np.arange(0, 1, 1/Fs)
        samples = Fs // len(message)

        BG = BinaryGenerator(message, samples)

        data_signal = BG.generate()
        data_signal_inverse = BG.generateInverse()
        carrier_signal_1 = np.cos(2 * np.pi * Fc1 * t)
        carrier_signal_2 = np.cos(2 * np.pi * Fc2 * t)

        if len(t) > len(data_signal_inverse):
            dif = len(t) - len(data_signal_inverse)
            for _ in range(dif):
                data_signal_inverse = np.append(data_signal_inverse, data_signal_inverse[-1])
        
        if len(t) > len(data_signal):
            dif = len(t) - len(data_signal)
            for _ in range(dif):
                data_signal = np.append(data_signal, data_signal[-1])

        fsk_signal = (carrier_signal_2 * data_signal) + (carrier_signal_1 * data_signal_inverse)

        # T = 1/bps seconds 
        # B = 1/(2T)
        # 2B = 1/T
        # 2B = 1/(1/bps) = bps
        # 2B = bps Hz

        bandWidth = (len(message))+(2*abs(Fc2-Fc1))
        return data_signal, carrier_signal_1, carrier_signal_2, fsk_signal, t, Fs, bandWidth
    else: 
        return 0

def modulatePSK(message, Fc):
    if(checkMessage(message)):
        # Fs = 32 * len(message)
        Fs = 32 * Fc
        t = np.arange(0, 1, 1/Fs)
        samples = len(t) // len(message)
        BG = BinaryGenerator(message, samples)

        data_signal = BG.generateBipolar()
        carrier_signal = np.sin(2 * np.pi * Fc * t)

        if len(t) > len(data_signal):
            dif = len(t) - len(data_signal)
            for i in range(dif):
                data_signal = np.append(data_signal, data_signal[-1])

        psk_signal = data_signal * carrier_signal

        bandWidth = len(message)

        return data_signal, carrier_signal, psk_signal, t, Fs, bandWidth
    else: 
        return 0
        
########################################################################
## END ==> MODULATION EVENTS
########################################################################