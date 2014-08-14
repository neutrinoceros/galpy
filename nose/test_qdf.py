# Tests of the quasiisothermaldf module
import numpy
#fiducial setup uses these
from galpy.potential import MWPotential, vcirc, omegac, epifreq, verticalfreq
from galpy.actionAngle import actionAngleAdiabatic, actionAngleStaeckel
from galpy.df import quasiisothermaldf
aAA= actionAngleAdiabatic(pot=MWPotential,c=True)
aAS= actionAngleStaeckel(pot=MWPotential,c=True,delta=0.5)

def test_meanvR_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvR_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvR_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_meanvR_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvR(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvR(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvR(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_meanvT_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,gl=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvT_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,mc=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvT_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,gl=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,gl=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvT_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    #In the mid-plane
    vtp9= qdf.meanvT(0.9,0.,mc=True)
    assert numpy.fabs(vtp9-dfc.meanvT(0.9)) < 0.05, "qdf's meanvT is not close to that of dehnendf"
    assert vtp9 <  vcirc(MWPotential,0.9), "qdf's meanvT is not less than the circular velocity (which we expect)"
    #higher up
    assert qdf.meanvR(0.9,0.2,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    assert qdf.meanvR(0.9,-0.25,mc=True) < vtp9, "qdf's meanvT above the plane is not less than in the plane (which we expect)"
    return None

def test_meanvz_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvz_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for adiabatic approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for adiabatic approx."
    return None

def test_meanvz_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,gl=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_meanvz_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(qdf.meanvz(0.9,0.,mc=True)) < 0.01, "qdf's meanvr is not equal to zero for staeckel approx."
    #higher up
    assert numpy.fabs(qdf.meanvz(0.9,0.2,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    assert numpy.fabs(qdf.meanvz(0.9,-0.25,mc=True)) < 0.05, "qdf's meanvr is not equal to zero for staeckel approx."
    return None

def test_sigmar_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.,gl=True))-2.*numpy.log(0.2)-0.2) < 0.2, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.2,gl=True))-2.*numpy.log(0.2)-0.2) < 0.3, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,-0.25,gl=True))-2.*numpy.log(0.2)-0.2) < 0.3, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmar_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.,mc=True))-2.*numpy.log(0.2)-0.2) < 0.2, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,0.2,mc=True))-2.*numpy.log(0.2)-0.2) < 0.4, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaR2(0.9,-0.25,mc=True))-2.*numpy.log(0.2)-0.2) < 0.3, "qdf's sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmat_staeckel_gl():
    #colder, st closer to epicycle expectation
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    gamma= 2.*omegac(MWPotential,0.9)/epifreq(MWPotential,0.9)
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.,gl=True)/qdf.sigmaR2(0.9,0.,gl=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.2,gl=True)/qdf.sigmaR2(0.9,0.2,gl=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmat_staeckel_mc():
    numpy.random.seed(2)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    gamma= 2.*omegac(MWPotential,0.9)/epifreq(MWPotential,0.9)
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.,mc=True)/qdf.sigmaR2(0.9,0.,mc=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaT2(0.9,0.2,mc=True)/qdf.sigmaR2(0.9,0.2,mc=True))+2.*numpy.log(gamma)) < 0.3, "qdf's sigmaT2/sigmaR2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmaz_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.,gl=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #from Bovy & Rix 2013, we know that this has to be smaller
    assert numpy.log(qdf.sigmaz2(0.9,0.,gl=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.2,gl=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,0.2,gl=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,-0.25,gl=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,-0.25,gl=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmaz_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.,mc=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #from Bovy & Rix 2013, we know that this has to be smaller
    assert numpy.log(qdf.sigmaz2(0.9,0.,mc=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    #higher up
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,0.2,mc=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,0.2,mc=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.fabs(numpy.log(qdf.sigmaz2(0.9,-0.25,mc=True))-2.*numpy.log(0.1)-0.2) < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    assert numpy.log(qdf.sigmaz2(0.9,-0.25,mc=True)) < 2.*numpy.log(0.1)+0.2 < 0.5, "qdf's sigmaz2 deviates more than expected from input for staeckel approx."
    return None

def test_sigmarz_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,gl=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for adiabatic approx."
    return None

def test_sigmarz_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,mc=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for adiabatic approx."
    return None

def test_sigmarz_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,gl=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for staeckel approx."
    return None

def test_sigmarz_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #In the mid-plane, should be zero
    assert numpy.fabs(qdf.sigmaRz(0.9,0.,mc=True)) < 0.05, "qdf's sigmaRz deviates more than expected from zero in the mid-plane for staeckel approx."
    return None

def test_tilt_adiabatic_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #should be zero everywhere
    assert numpy.fabs(qdf.tilt(0.9,0.,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,0.2,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.25,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    return None

def test_tilt_adiabatic_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    #should be zero everywhere
    assert numpy.fabs(qdf.tilt(0.9,0.,mc=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,0.2,mc=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.25,mc=True)) < 0.05, "qdf's tilt deviates more than expected from zero for adiabatic approx."
    return None

def test_tilt_staeckel_gl():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #should be zero in the mid-plane and roughly toward the GC elsewhere
    assert numpy.fabs(qdf.tilt(0.9,0.,gl=True)) < 0.05, "qdf's tilt deviates more than expected from zero in the mid-plane for staeckel approx."
    assert numpy.fabs(qdf.tilt(0.9,0.1,gl=True)-numpy.arctan(0.1/0.9)/numpy.pi*180.) < 2., "qdf's tilt deviates more than expected from expected for staeckel approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.15,gl=True)-numpy.arctan(-0.15/0.9)/numpy.pi*180.) < 2.5, "qdf's tilt deviates more than expected from expected for staeckel approx."
    assert numpy.fabs(qdf.tilt(0.9,-0.25,gl=True)-numpy.arctan(-0.25/0.9)/numpy.pi*180.) < 4., "qdf's tilt deviates more than expected from expected for staeckel approx."
    return None

def test_tilt_staeckel_mc():
    numpy.random.seed(1)
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    #should be zero in the mid-plane and roughly toward the GC elsewhere
    assert numpy.fabs(qdf.tilt(0.9,0.,mc=True)) < 1., "qdf's tilt deviates more than expected from zero in the mid-plane for staeckel approx." #this is tough
    assert numpy.fabs(qdf.tilt(0.9,0.1,mc=True)-numpy.arctan(0.1/0.9)/numpy.pi*180.) < 3., "qdf's tilt deviates more than expected from expected for staeckel approx."
    return None

def test_estimate_hr():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hr(0.9,z=0.)-0.25)/0.25) < 0.1, 'estimated scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1./2.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hr(0.9,z=None)-0.5)/0.5) < 0.15, 'estimated scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hr(0.9,z=None,fixed_quad=False)-1.0)/1.0) < 0.3, 'estimated scale length deviates more from input scale length than expected'
    return None

def test_estimate_hz():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from scipy import integrate
    from galpy.potential import evaluateDensities
    expec_hz= 0.1**2./2.\
        /integrate.quad(lambda x: evaluateDensities(0.9,x,MWPotential),
                        0.,0.125)[0]/2./numpy.pi
    assert numpy.fabs((qdf.estimate_hz(0.9,z=0.125)-expec_hz)/expec_hz) < 0.1, 'estimated scale height not as expected'
    assert qdf.estimate_hz(0.9,z=0.) > 1., 'estimated scale height at z=0 not very large'
    #Another one
    qdf= quasiisothermaldf(1./4.,0.3,0.2,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    expec_hz= 0.2**2./2.\
        /integrate.quad(lambda x: evaluateDensities(0.9,x,MWPotential),
                        0.,0.125)[0]/2./numpy.pi
    assert numpy.fabs((qdf.estimate_hz(0.9,z=0.125)-expec_hz)/expec_hz) < 0.15, 'estimated scale height not as expected'
    return None

def test_estimate_hsr():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsr(0.9,z=0.)-1.0)/1.0) < 0.25, 'estimated radial-dispersion scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1./2.,0.2,0.1,2.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsr(0.9,z=0.05)-2.0)/2.0) < 0.25, 'estimated radial-dispersion scale length deviates more from input scale length than expected'
    return None

def test_estimate_hsz():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsz(0.9,z=0.)-1.0)/1.0) < 0.25, 'estimated vertical-dispersion scale length deviates more from input scale length than expected'
    #Another one
    qdf= quasiisothermaldf(1./2.,0.2,0.1,1.,2.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs((qdf.estimate_hsz(0.9,z=0.05)-2.0)/2.0) < 0.25, 'estimated vertical-dispersion scale length deviates more from input scale length than expected'
    return None

def test_meanjr():
    #This is a *very* rough test against a rough estimate of the mean
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    assert numpy.fabs(numpy.log(qdf.meanjr(0.9,0.,mc=True))\
                          -2.*numpy.log(0.2)-0.2
                      +numpy.log(epifreq(MWPotential,0.9))) < 0.4, 'meanjr is not what is expected'
    assert numpy.fabs(numpy.log(qdf.meanjr(0.5,0.,mc=True))\
                          -2.*numpy.log(0.2)-1.
                      +numpy.log(epifreq(MWPotential,0.5))) < 0.4, 'meanjr is not what is expected'
    return None

def test_meanlz():
    #This is a *very* rough test against a rough estimate of the mean
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    from galpy.df import dehnendf #baseline
    dfc= dehnendf(profileParams=(1./4.,1.0, 0.2),
                  beta=0.,correct=False)
    assert numpy.fabs(numpy.log(qdf.meanlz(0.9,0.,mc=True))\
                          -numpy.log(0.9*dfc.meanvT(0.9))) < 0.1, 'meanlz is not what is expected'
    assert numpy.fabs(numpy.log(qdf.meanlz(0.5,0.,mc=True))\
                          -numpy.log(0.5*dfc.meanvT(0.5))) < 0.2, 'meanlz is not what is expected'
    return None

def test_meanjz():
    #This is a *very* rough test against a rough estimate of the mean
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    ldiff= numpy.log(qdf.meanjz(0.9,0.,mc=True))-2.*numpy.log(0.1)-0.2\
        +numpy.log(verticalfreq(MWPotential,0.9))
    #expect this to be smaller than the rough estimate, but not by more than an order of magnitude
    assert ldiff > -1. and ldiff < 0., 'meanjz is not what is expected'
    ldiff= numpy.log(qdf.meanjz(0.5,0.,mc=True))-2.*numpy.log(0.1)-1.0\
        +numpy.log(verticalfreq(MWPotential,0.5))
    assert ldiff > -1. and ldiff < 0., 'meanjz is not what is expected'
    return None

def test_sampleV():
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    numpy.random.seed(1)
    samples= qdf.sampleV(0.8,0.1,n=1000)
    #test vR
    assert numpy.fabs(numpy.mean(samples[:,0])) < 0.02, 'sampleV vR mean is not zero'
    assert numpy.fabs(numpy.log(numpy.std(samples[:,0]))-0.5*numpy.log(qdf.sigmaR2(0.8,0.1))) < 0.05, 'sampleV vR stddev is not equal to sigmaR'
    #test vT
    assert numpy.fabs(numpy.mean(samples[:,1]-qdf.meanvT(0.8,0.1))) < 0.015, 'sampleV vT mean is not equal to meanvT'
    assert numpy.fabs(numpy.log(numpy.std(samples[:,1]))-0.5*numpy.log(qdf.sigmaT2(0.8,0.1))) < 0.05, 'sampleV vT stddev is not equal to sigmaT'
    #test vz
    assert numpy.fabs(numpy.mean(samples[:,2])) < 0.01, 'sampleV vz mean is not zero'
    assert numpy.fabs(numpy.log(numpy.std(samples[:,2]))-0.5*numpy.log(qdf.sigmaz2(0.8,0.1))) < 0.05, 'sampleV vz stddev is not equal to sigmaz'
    return None

def test_pvR_adiabatic():
    # Test pvR by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,51)
    pvR= numpy.array([qdf.pvR(vr,R,z) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for adiabatic actions'
    return None

def test_pvR_staeckel():
    # Test pvR by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,51)
    pvR= numpy.array([qdf.pvR(vr,R,z) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for staeckel actions'
    return None

def test_pvR_staeckel_diffngl():
    # Test pvR by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vRs= numpy.linspace(-1.,1.,51)
    #ngl=10
    pvR= numpy.array([qdf.pvR(vr,R,z,ngl=10) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for staeckel actions'
    #ngl=40
    pvR= numpy.array([qdf.pvR(vr,R,z,ngl=40) for vr in vRs])
    mvR= numpy.sum(vRs*pvR)/numpy.sum(pvR)
    svR= numpy.sqrt(numpy.sum(vRs**2.*pvR)/numpy.sum(pvR)-mvR**2.)
    assert numpy.fabs(mvR) < 0.01, 'mean vR calculated from pvR not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svR)-0.5*numpy.log(qdf.sigmaR2(R,z))) < 0.01, 'sigma vR calculated from pvR not equal to that from sigmaR2 for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvR= numpy.array([qdf.pvR(vr,R,z,ngl=11) for vr in vRs])
    except ValueError: pass
    else: raise AssertionError('pvR w/ ngl=odd did not raise ValueError')
    return None

def test_pvz_adiabatic():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAA,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,51)
    pvz= numpy.array([qdf.pvz(vz,R,z) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for adiabatic actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for adiabatic actions'
    return None

def test_pvz_staeckel():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,51)
    pvz= numpy.array([qdf.pvz(vz,R,z) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    #same w/ explicit sigmaR input
    pvz= numpy.array([qdf.pvz(vz,R,z,_sigmaR1=0.95*numpy.sqrt(qdf.sigmaR2(R,z))) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    return None

def test_pvz_staeckel_diffngl():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    vzs= numpy.linspace(-1.,1.,51)
    #ngl=10
    pvz= numpy.array([qdf.pvz(vz,R,z,ngl=10) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    #ngl=40
    pvz= numpy.array([qdf.pvz(vz,R,z,ngl=40) for vz in vzs])
    mvz= numpy.sum(vzs*pvz)/numpy.sum(pvz)
    svz= numpy.sqrt(numpy.sum(vzs**2.*pvz)/numpy.sum(pvz)-mvz**2.)
    assert numpy.fabs(mvz) < 0.01, 'mean vz calculated from pvz not equal to zero for staeckel actions'
    assert numpy.fabs(numpy.log(svz)-0.5*numpy.log(qdf.sigmaz2(R,z))) < 0.01, 'sigma vz calculated from pvz not equal to that from sigmaz2 for staeckel actions'
    #ngl=11, shouldn't work
    try:
        pvz= numpy.array([qdf.pvz(vz,R,z,ngl=11) for vz in vzs])
    except ValueError: pass
    else: raise AssertionError('pvz w/ ngl=odd did not raise ValueError')
    return None

def test_pvz_staeckel_arrayin():
    # Test pvz by calculating its mean and stddev by Riemann sum
    qdf= quasiisothermaldf(1./4.,0.2,0.1,1.,1.,
                           pot=MWPotential,aA=aAS,cutcounter=True)
    R,z= 0.8, 0.1
    pvz= qdf.pvz(0.05,R*numpy.ones(2),z*numpy.ones(2))
    assert numpy.all(numpy.log(pvz)-numpy.log(qdf.pvz(0.05,R,z))) < 10.**-10., 'pvz calculated with R and z array input does not equal to calculated with scalar input'
    return None

