import numpy as np
from scipy.stats import kurtosis
from pywt import wavedec
from scipy.stats import skew

#transformada de Fourier
def transFourier(sinalt):
    sinalf=np.fft.fft(sinalt)
    sinalf=np.fft.fftshift(sinalf)
    return sinalf

#PSD
def PSD(sinalt):
    sinalf=(np.abs(np.fft.fft(sinalt)))**2
    #sinalf=np.fft.fftshift(sinalf)
    return sinalf


#transformada de fourier inversa
def itransFourier(sinalt):
    sinalf=np.fft.ifft(sinalt)
    #sinalf=np.fft.fftshift(sinalf)
    return sinalf
#FLTRAGEM
def filtragem(sinalt,freq):
    sinalf = np.fft.fft(sinalt)
    sinalf[freq:len(sinalf)] = 0
    sinalt = np.fft.ifft(sinalf)
    return sinalt

#media da trnasform de Fourier
def media(sinalf):
    med = np.zeros(960)
    for i in range(960):
         med[i] = sum(sinalf[10*i:10*(i+1)]) / 10
    return med


#Kurtosis
def Kurt(vet):
    vetf = kurtosis(vet)
    return vetf

#wavelet
def wavelet(sinalt,ordem):
    coeff = wavedec(sinalt, 'db1', level=ordem)
    return coeff
#ZCR
def ZCR(sinalt):
    cont=0
    for x in range(len(sinalt)-1):
        if (sinalt[x+1]*sinalt[x])<0:
            cont = cont+1
    return cont

#valor central
def VC(sinal):
    cent = sinal[400]
    return cent

#valor máximo
def ValorMax(vet):
    VM = max(vet)
    return VM

#skewness
def skw(vet):
    vet = skew(vet)
    return vet