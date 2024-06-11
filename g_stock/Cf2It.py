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
def read_data(path="/Users/guangruli/Desktop/data_for_paper3/CHRONOA.DTA", plot=False, delta=False,fmax=1e7,fmin=0):
  import gamry_parser as parser
  import numpy as np
  gp = parser.GamryParser()
  gp.load(filename=path)
  data=gp.get_curve_data()
  select = np.logical_and(data["Freq"]<fmax,data["Freq"]>fmin) 
  Freq=data['Freq'].to_numpy()[select]
  Zreal=data["Zreal"].to_numpy()[select]
  Zimag=data["Zimag"].to_numpy()[select]
  return Zreal,Zimag,Freq
def It_from_file(path,fmax=1e7,fmin=0):
  Zreal,Zimag,Freq_Z = read_data(path=path, fmax=fmax,fmin=fmin)
  Z=Zreal+1j*Zimag
  import numpy as np
  freq_min=np.min(freq_Z[np.where(freq_Z>0)])
  freq_max=np.max(freq_Z)
  freqs=np.arange(freq_min,freq_max,freq_min)
  t_max=1/freq_min
  t_min=1/freq_max*2
  ### generate exciting signal################
  V, dV_fft, freqs=excit(dt=t_min,t_max=t_max)
  from scipy.interpolate import interp1d
  Z_fft = interp1d(freq_Z,Z, fill_value=(0,0), bounds_error=False)(freqs)
  dI_fft=dV_fft/Z_fft
  I,t=recon(dI_fft,freqs,accu=True)
  return I,t
