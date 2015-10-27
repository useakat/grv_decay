#include <iostream>
#include "Pythia8/Pythia.h"

using namespace Pythia8;

int main(int argc, char *argv[]) {

  Pythia pythia;
  Event& event      = pythia.event;
  ParticleData& pdt = pythia.particleData;
  double mDM = strtod(argv[1], &ends);
  int inevents = atoi(argv[2]);

  std::ofstream ofsmass("mass.dat");
  ofsmass << mDM << endl;

  // Initialize Les Houches Event File run. List initialization information.
  //pythia.readString("ProcessLevel:all = off");
  //pythia.readString("PartonLevel:all = on");
  //  pythia.readString("HadronLevel:Decay = off");
  pythia.readString("Random:setSeed = on");
  pythia.readString("Random:seed = 0"); //pick new random seed for each run, based on cloc
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF = unweighted_events_mod.lhe");
  pythia.readString("SLHA:useDecayTable = on");

//// Life time < 10^-10 s ////////////
  pdt.mayDecay(15,true);     // tau
  pdt.mayDecay(-15,true);
  pdt.mayDecay(310,true);    // KS
  pdt.mayDecay(111,true);    // pi0
  pdt.mayDecay(311,true);    // K0
  pdt.mayDecay(-311,true);   // K0_bar
  pdt.mayDecay(3122,true);   // Lambda
//// Life time > 10^-10 s ////////////
  pdt.mayDecay(13,false);     // muon
  pdt.mayDecay(-13,false);
  pdt.mayDecay(211,false);   // pi+
  pdt.mayDecay(-211,false);  // pi-
  pdt.mayDecay(130,false);    // KL
  pdt.mayDecay(321,false);    // K+
  pdt.mayDecay(-321,false);   // K-
  pdt.mayDecay(2112,false);  // n
  pdt.mayDecay(-2112,false); // n_bar
  
  pythia.init();

  // Allow for possibility of a few faulty events.
  int nAbort = 10;
  int iAbort = 0;

  //  double nevents = 90000.;
  //  int inevents;
  //inevents = atoi(argv[1]);

  double xmin = 0.01;
  double xmax = 1000000.;
  int nbins = 800;
  //  int nbins = 120;
  double *x = new double[nbins];
  for (int i = 0; i < nbins+1; ++i) {
    //    x[i] = xmin +(xmax -xmin)/nbins*i;
    x[i] = pow(10,log10(xmin) +(log10(xmax) -log10(xmin))/float(nbins)*i);
  }

  double me = 0.000511;
  double mp = 0.938272;
  double mn = 0.939565;
  double mpi = 0.13957018;
  double mKpm = 0.493677;
  double mKL = 0.497614; // K0 mass

  int *nnGam = new int[nbins];
  int *nnEle = new int[nbins];
  int *nnNeue = new int[nbins];
  int *nnNeumu = new int[nbins];
  int *nnNeutau = new int[nbins];
  int *nnP = new int[nbins];
  int *nnaP = new int[nbins];
  int *nnN = new int[nbins];
  int *nnaN = new int[nbins];
  int *nnpip = new int[nbins];
  int *nnpim = new int[nbins];
  int *nnKp = new int[nbins];
  int *nnKm = new int[nbins];
  int *nnKL = new int[nbins];
  for (int i = 0; i < nbins+1; ++i) {
    nnGam[i] = 0;
    nnEle[i] = 0;
    nnNeue[i] = 0;
    nnNeumu[i] = 0;
    nnNeutau[i] = 0;
    nnP[i] = 0;
    nnaP[i] = 0;
    nnN[i] = 0;
    nnaN[i] = 0;
    nnpip[i] = 0;
    nnpim[i] = 0;
    nnKp[i] = 0;
    nnKm[i] = 0;
    nnKL[i] = 0;
  }
  int totGam = 0;
  int totEle = 0;
  int totNeue = 0;
  int totNeumu = 0;
  int totNeutau = 0;
  int totP = 0;
  int totaP = 0;
  int totN = 0;
  int totaN = 0;
  int totpip = 0;
  int totpim = 0;
  int totKp = 0;
  int totKm = 0;
  int totKL = 0;
  int totOther = 0;

  double nevents = 0;
  // Begin event loop; generate until none left in input file.
  //  for (int iEvent = 0; iEvent < 27; ++iEvent) {
  for (int iEvent = 0; ; ++iEvent) {
    // Set up parton-level configuration.
    //    fillPartons( 91.188, event, pdt, pythia.rndm);

    // Generate events, and check whether generation failed.
    if (!pythia.next()) {
      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;
      // First few failures write off as "acceptable" errors, then quit.
      if (++iAbort < nAbort) continue;
      break;
    }

    //    pythia.event.list();

    double Ekin;
    // Fill in histogram.
    for (int i = 0; i < event.size(); ++i) {
      if (event[i].isFinal()) {
	if (event[i].id() == 22) {
	  Ekin = event[i].e();
	  totGam = totGam +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnGam[0] = nnGam[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnGam[ii+1] = nnGam[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (abs(event[i].id()) == 11) {
	  Ekin = event[i].e() -me;
	  totEle = totEle +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnEle[0] = nnEle[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnEle[ii+1] = nnEle[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (abs(event[i].id()) == 12) {
	  Ekin = event[i].e();
	  totNeue = totNeue +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnNeue[0] = nnNeue[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnNeue[ii+1] = nnNeue[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (abs(event[i].id()) == 14) {
	  Ekin = event[i].e();
	  totNeumu = totNeumu +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnNeumu[0] = nnNeumu[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnNeumu[ii+1] = nnNeumu[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (abs(event[i].id()) == 16) {
	  Ekin = event[i].e();
	  totNeutau = totNeutau +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnNeutau[0] = nnNeutau[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnNeutau[ii+1] = nnNeutau[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (event[i].id() == 2212) {
	  Ekin = event[i].e() -mp;
	  totP = totP +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnP[0] = nnP[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnP[ii+1] = nnP[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	else if (event[i].id() == -2212) {
	  Ekin = event[i].e() -mp;
	  totaP = totaP +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnaP[0] = nnaP[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnaP[ii+1] = nnaP[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (event[i].id() == 2112) {
	  Ekin = event[i].e() -mn;
	  totN = totN +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnN[0] = nnN[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnN[ii+1] = nnN[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	else if (event[i].id() == -2112) {
	  Ekin = event[i].e() -mn;
	  totaN = totaN +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnaN[0] = nnaN[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnaN[ii+1] = nnaN[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else if (event[i].id() == 211) {
	  Ekin = event[i].e() -mpi;
	  totpip = totpip +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnpip[0] = nnpip[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnpip[ii+1] = nnpip[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	else if (event[i].id() == -211) {
	  Ekin = event[i].e() -mpi;
	  totpim = totpim +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnpim[0] = nnpim[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnpim[ii+1] = nnpim[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	else if (event[i].id() == 321) {
	  Ekin = event[i].e() -mKpm;
	  totKp = totKp +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnKp[0] = nnKp[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnKp[ii+1] = nnKp[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	else if (event[i].id() == -321) {
	  Ekin = event[i].e() -mKpm;
	  totKm = totKm +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnKm[0] = nnKm[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnKm[ii+1] = nnKm[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	else if (event[i].id() == 130) {
	  Ekin = event[i].e() -mKL;
	  totKL = totKL +1;
	  if ( Ekin < x[0] ) {
	    if ( 0.00891251 < Ekin ) {
	      nnKL[0] = nnKL[0] +1;
	    }
	  }
	  else {
	    for (int ii = 0; ii < nbins; ++ii) {
	      if (x[ii] < Ekin) {
		if (Ekin < x[ii+1]) {
		  nnKL[ii+1] = nnKL[ii+1] +1;
		  break;
		}
	      }
	    }
	  }
	}
	else {
	  totOther = totOther +1;
	  //	  cout << event[i].id();
	}
      }
    }
    nevents = nevents +1;
    // End of event loop.
  }

  // Give statistics. Print histogram.
  pythia.stat();
  
  //int Total = GamE.getEntries();
  //  std::ofstream ofsGamE("dist_takaesu_nodecay.dat");
  //  std::ofstream ofsGamE("Edist.dat");
  std::ofstream ofsnp("np_sptrm.dat");
  for (int i = 0; i < nbins+1; ++i) {
    ofsnp << setiosflags(ios::scientific) << mDM << " " << x[i] << " " << nnN[i]/nevents << " " << nnP[i]/nevents << " " 
	    << nnpip[i]/nevents << " " << nnpim[i]/nevents << " " << nnKp[i]/nevents << " "
            << nnKm[i]/nevents << " " << nnKL[i]/nevents << " " << nnaN[i]/nevents << " " 
            << nnaP[i]/nevents << endl;
  }

  std::ofstream ofsEdist("Edist.dat");
  ofsEdist << setiosflags(ios::scientific) << (totpip+totpim)/nevents << " " << (totN+totaN)/nevents << " " << (totP+totaP)/nevents << endl;
  for (int i = 0; i < nbins+1; ++i) {
    ofsEdist << setiosflags(ios::scientific) << x[i] << " " << (nnpip[i]+nnpim[i])/nevents << " " << (nnN[i]+nnaN[i])/nevents << " " << (nnP[i]+nnaP[i])/nevents << endl;
  }

  std::ofstream ofsnini("nini.dat");
  ofsnini << setiosflags(ios::scientific) << mDM << " " << totN/nevents << " " << totP/nevents << " " << totpip/nevents << " " 
	  << totpim/nevents << " " << totKp/nevents << " " << totKm/nevents << " " << totKL/nevents << " " 
	  << totaN/nevents << " " << totaP/nevents << endl;

  cout << setiosflags(ios::scientific) << totGam/nevents << " " << totEle/nevents << " " << totN/nevents << " " << totP/nevents << " " 
       << totpip/nevents << " " << totpim/nevents << " " << totKp/nevents << " " << totKm/nevents << " " 
       << totKL/nevents << " " << totaN/nevents << " " << totaP/nevents << " " << totOther/nevents << endl;

  // ofsGamE << totpi/nevents << " " << totN/nevents << " " << totP/nevents << endl;
  // for (int i = 0; i < nbins+1; ++i) {
  //   //    ofsGamE << x[i+1] << " " << nnEle[i]/nevents << " " << nnGam[i]/nevents << " " << nnP[i]/nevents << " " << nnN[i]/nevents << " " << nnNeue[i]/nevents << " " << nnNeumu[i]/nevents << " " << nnNeutau[i]/nevents << endl;
  //   ofsGamE << x[i] << " " << nnpi[i]/nevents << " " << nnN[i]/nevents << " " << nnP[i]/nevents << endl;
  // }
  // Done.
  cout << totGam << " " << totEle << " " << totN << " " << totP << " " << totOther << endl;

////////////////           ////////////////////// 
//////////////// Evis data ////////////////////// 

//// Life time > 10^-10 s ////////////
  pdt.mayDecay(13,true);     // muon
  pdt.mayDecay(-13,true);
  pdt.mayDecay(211,true);   // pi+
  pdt.mayDecay(-211,true);  // pi-
  pdt.mayDecay(130,true);    // KL
  pdt.mayDecay(321,true);    // K+
  pdt.mayDecay(-321,true);   // K-
  pdt.mayDecay(2112,false);  // n
  pdt.mayDecay(-2112,false); // n_bar

  pythia.init();

  nevents = 0;
  double Ekin = 0;
  double Ekin_neu = 0;
  double Ekin_other = 0;
  // Begin event loop; generate until none left in input file.
  for (int iEvent = 0; iEvent < inevents; ++iEvent) {
    // Generate events, and check whether generation failed.
    if (!pythia.next()) {
      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;
      // First few failures write off as "acceptable" errors, then quit.
      if (++iAbort < nAbort) continue;
      break;
    }

    for (int i = 0; i < event.size(); ++i) {
      if (event[i].isFinal()) {
	if (abs(event[i].id()) == 12) {
	  Ekin_neu = Ekin_neu +event[i].e();
	}
	else if (abs(event[i].id()) == 14) {
	  Ekin_neu = Ekin_neu +event[i].e();
	}
	else if (abs(event[i].id()) == 16) {
	  Ekin_neu = Ekin_neu +event[i].e();
	}
	else if (abs(event[i].id()) == 11) {
	  Ekin = Ekin +event[i].e() -me;
	  //Ekin = Ekin +event[i].e();
	}
	else if (abs(event[i].id()) == 22) {
	  Ekin = Ekin +event[i].e();
	}
	else if (abs(event[i].id()) == 2112) {
	  Ekin = Ekin +event[i].e() -mn;
	  //Ekin = Ekin +event[i].e();
	}
	else if (abs(event[i].id()) == 2212) {
	  Ekin = Ekin +event[i].e() -mp;
	  //Ekin = Ekin +event[i].e();
	}
	else {
	  Ekin_other = Ekin_other +event[i].e();
	}
      }
    }
    nevents = nevents +1;
  // End of event loop.
  }

  // Give statistics. Print histogram.
  pythia.stat();

  std::ofstream ofsEvis("Evis.dat");
  ofsEvis << setiosflags(ios::scientific) << 2*mDM << " " << Ekin/nevents << " "  << Ekin/(2*mDM)/nevents << endl;

  cout << setiosflags(ios::scientific) << 2*mDM << " " << Ekin/nevents << " "  << Ekin/(2*mDM)/nevents << " " << Ekin_other/nevents << " " << nevents << endl;

  std::ofstream ofsGamE("Evis_tot.dat");
  ofsGamE << Ekin/nevents << endl;

  return 0;
}
