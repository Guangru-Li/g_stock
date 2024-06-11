"""
Z_simu: define impedance simulator
excit: define a fft voltage generator
recon: generate It or dI-dt curve from Z, freq relationships

"""
def Z_simu(omega=None):
  import numpy as np
  if omega == None:
    omega = np.logspace(-5,8,100)
  # Ref paper: an electrochemical impedance measurement technique employing fourier transform
  import numpy as np
  omega=omega*2*np.pi
  Rs=50
  Rp=1e2
  Cd=3e-5
  Z=Rs+Rp/(1+Rp*Cd*1j*omega)
  return np.array(Z)
def excit(dt=0.1,n=10,t_max=10):
  import scipy
  t=np.arange(0,t_max,dt)
  V = np.concatenate(([0]*n,[1]*(len(t)-n)))
  dV = np.diff(V)/dt
  t=t[:-1]
  from scipy.fft import rfft, rfftfreq
  dV_fft= rfft(dV)
  freq = rfftfreq(len(dV), dt)
  return V, dV_fft, freq

def recon(data,freq,accu=False):
  from scipy.fft import irfft
  import scipy
  re=irfft(data)
  dt = 1/np.max(freq)/2
  t = np.arange(0,dt*len(re),dt)
  if accu==True:
      re=scipy.integrate.cumtrapz(re)
      t=t[:-1]
  return re,t
## direct working with files##########
