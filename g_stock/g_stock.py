def get_stock_data():
  print("this is the stock data")
#obtain impedance  
def Z(I,V,t):
    import numpy as np
    from scipy.fft import rfft,rfftfreq,irfft
    dt = np.diff(t).mean()
    dI = np.gradient(I)
    dV = np.gradient(V)
    n=len(t)
    freq=rfftfreq(n,dt)
    dV_fft=rfft(dV)
    dI_fft=rfft(dI)
    Z_fft=dV_fft/dI_fft
    return Z_fft,freq
# 2. obtain Impedance curve 
def Bode(I,V,t):
    Z,freq=Z(I,V,t)
    return np.abs(Z),freq
def Nyquist(I,V,t):
    Z,freq=Z(I,V,t)
    return Z.real, Z.imag*-1
def Cf(I,V,t):
    import numpy as np
    Z,freq=Z(I,V,t)
    C = (1/Z/2/freq/np.pi).imag
    return C,freq
