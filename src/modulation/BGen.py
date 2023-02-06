import numpy as np
from scipy import signal

class BinaryGenerator:

    def __init__(self,Message: str, SampleSize: int):
        self.dmsg = Message
        self.samples = SampleSize
        self.bits = [1 if bit == '1' else 0 for bit in self.dmsg]
    
    @classmethod
    def generateClock(cls,t: np.ndarray, pulseSize: int) -> np.ndarray:
        signal = np.zeros(len(t))
        for i in range(0,len(t),2*pulseSize):
            signal[(i) : (i + pulseSize)] = 1
        return signal
    
    @classmethod
    def generateSawtooth(cls,t: np.ndarray,freq: int,amp: float) -> np.ndarray:
        wave = amp * signal.sawtooth(2*np.pi*freq*t)
        return wave

    def generate(self) -> np.ndarray:
        sig = np.zeros(self.samples * len(self.bits))
        for j in range(len(self.bits)):
            if(self.bits[j] == 1):
                sig[(j * self.samples) : (j * self.samples + self.samples)] = 1
        return sig

    def generateInverse(self) -> np.ndarray:
        sig = np.ones(self.samples * len(self.bits))
        for j in range(len(self.bits)):
            if(self.bits[j] == 1):
                sig[(j * self.samples) : (j * self.samples + self.samples)] = 0
        return sig

    def generateBipolar(self) -> np.ndarray:
        sig = np.ones(self.samples * len(self.bits))
        for j in range(len(self.bits)):
            if(self.bits[j] == 0):
                sig[(j * self.samples) : (j * self.samples + self.samples)] = -1
        return sig
