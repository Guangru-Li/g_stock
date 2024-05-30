def hello():
  print("hello")

# PROCESS:
# 1. obtain monochro-whatever curve (0 V, 1 V, 1.5 V, 2 V)
def read_data(path="/Users/guangruli/Desktop/data_for_paper3/CHRONOA.DTA", plot=False, min_t=-1,max_t=float("inf"),delta=False):
    import gamry_parser as parser
    import numpy as np
    path="/Users/guangruli/Desktop/data_for_paper3/CHRONOA.DTA"
    gp = parser.GamryParser()
    gp.load(filename=path)
    #ca.load(filename=path)
    data=gp.get_curve_data()
    select=np.logical_and(data['T']<max_t, data['T']>min_t)
    
    t=data['T'].to_numpy()[select]
    v=data["Vf"].to_numpy()[select]
    I=data["Im"].to_numpy()[select]
    
    if delta==True:
        I=np.gradient(I)
        v=np.gradient(v)
    if plot==True:
        import matplotlib.pyplot as plt
        plt.subplots(1,2)
        plt.subplot(121)
        plt.plot(t,v)
        plt.subplot(122)
        plt.plot(t,I)
    return I,v,t

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

# 3. compare 
# Finish RED
# Finish R-G-B
# Investigate degradation
# Spectrograph??
# linear integration??
