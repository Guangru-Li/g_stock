def Bode(path)
def hello():
  print("hello")
# PROCESS:
# 1. obtain monochro-whatever curve (0 V, 1 V, 1.5 V, 2 V)
def read_data(path="/Users/guangruli/Desktop/data_for_paper3/CHRONOA.DTA", plot=False, delta=False):
    import gamry_parser as parser
    import numpy as np
    gp = parser.GamryParser()
    gp.load(filename=path)
    data=gp.get_curve_data()
    Freq=data['Freq'].to_numpy()[select]
    Zreal=data["Zreal"].to_numpy()[select]
    Zimag=data["Zimag"].to_numpy()[select]
    return Zreal,Zimag,Freq
  
def Bode(path,plot=True):
    Zreal,Zimag,Freq=read_data(path=Path)
    if plot==True:
        import matplotlib.pyplot as plt
        plt.subplots(1,2)
        plt.subplot(121)
        plt.plot(freq,np.abs(Z_))
        plt.xscale("log")
        plt.subplot(122)
        plt.plot(freq,np.angle(Z_,deg=True))
        plt.xscale("log")
    
    return np.abs(Z_),freq
def Nyquist(I,V,t,plot=False,pad=0):
    Zreal,Zimag,Freq=read_data(path=Path)
    if plot==True:
        import matplotlib.pyplot as plt
        plt.subplots()
        plt.plot(Zreal,Zimag*-1)
    return Z_.real, Z_.imag*-1
def Cf(I,V,t, plot=False,pad=0):
    import numpy as np
    Zreal,Zimag,Freq=read_data(path=Path)
    C = (1/(Zreal+1j*Zimag)/2/Freq/np.pi).imag
    if plot==True:
        import matplotlib.pyplot as plt
        plt.subplots()
        plt.plot(Freq,C,"-o")
        plt.xscale("log")
    return C,Freq

