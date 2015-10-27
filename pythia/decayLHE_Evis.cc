#include <iostream>
#include "Pythia8/Pythia.h"

using namespace Pythia8;

int main(int argc, char *argv[]) {

  Pythia pythia;
  Event& event      = pythia.event;
  ParticleData& pdt = pythia.particleData;

  // Initialize Les Houches Event File run. List initialization information.
  //pythia.readString("ProcessLevel:all = off");
  //pythia.readString("PartonLevel:all = on");
  //  pythia.readString("HadronLevel:Decay = off");
  pythia.readString("Random:setSeed = on");
  pythia.readString("Random:seed = 0"); //pick new random seed for each run, based on clock
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF = unweighted_events_mod.lhe");
  pythia.readString("SLHA:useDecayTable = off");

  pdt.mayDecay(13,true);
  pdt.mayDecay(-13,true);
  pdt.mayDecay(15,true);
  pdt.mayDecay(-15,true);
  pdt.mayDecay(130,true);
  pdt.mayDecay(310,true);
  pdt.mayDecay(111,true);
  pdt.mayDecay(211,true);  // pi+
  pdt.mayDecay(-211,true); // pi-
  pdt.mayDecay(311,true);
  pdt.mayDecay(-311,true);
  pdt.mayDecay(321,true);
  pdt.mayDecay(-321,true);
  pdt.mayDecay(2112,false);
  pdt.mayDecay(-2112,false);
  pythia.init();

  // Allow for possibility of a few faulty events.
  int nAbort = 10;
  int iAbort = 0;

  //  double nevents = 90000.;
  int inevents;
  inevents = atoi(argv[1]);
  double nevents = 0;

  double xmin = 0.01;
  double xmax = 100000.;
  int nbins = 140;
  double *x = new double[nbins];
  for (int i = 0; i < nbins+1; ++i) {
    //    x[i] = xmin +(xmax -xmin)/nbins*i;
    x[i] = pow(10,log10(xmin) +(log10(xmax) -log10(xmin))/nbins*i);
  }

  double me = 0.000511;
  double mp = 0.938272;

  double Etot_vis = 0;

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
    for (int i = 0; i < event.size(); ++i)
      if (event[i].isFinal()) {
	if (event[i].id() == 22) {
	  Ekin = event[i].e();
	  Etot_vis = Etot_vis +Ekin;
	}
	else if (abs(event[i].id()) == 11) {
	  Ekin = event[i].e() -me;
	  Etot_vis = Etot_vis +Ekin;
	}
	else if (abs(event[i].id()) == 2212) {
	  Ekin = event[i].e() -mp;
	  Etot_vis = Etot_vis +Ekin;
	}
      }
    nevents = nevents +1;
  // End of event loop.
  }

  // Give statistics. Print histogram.
  pythia.stat();
  
  //int Total = GamE.getEntries();
  //  std::ofstream ofsGamE("dist_takaesu_nodecay.dat");
  std::ofstream ofsGamE("Evis_tot.dat");
  ofsGamE << Etot_vis/nevents << endl;
  // Done.
  return 0;
}
