#include <iostream>
#include "Pythia8/Pythia.h"

using namespace Pythia8;

int main() {

  Pythia pythia;
  Event& event      = pythia.event;
  ParticleData& pdt = pythia.particleData;

  // Initialize Les Houches Event File run. List initialization information.
  //pythia.readString("ProcessLevel:all = off");
  //pythia.readString("PartonLevel:all = on");
  //  pythia.readString("HadronLevel:Decay = off");
  pythia.readString("Random:setSeed = on");
  pythia.readString("Random:seed = 0"); //pick new random seed for each run, based on cloc
 
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF = unweighted_events.lhe");

  // Allow no substructure in e+- beams: normal for corrected LEP data.
  //pythia.readString("PDF:lepton = off");
  // Process selection.
  //  pythia.readString("WeakSingleBoson:ffbar2gmZ = on");
  //pythia.readString("WeakSingleBoson:ffbar2ffbar(s:gmZ) = on");
  // Switch off all Z0 decays and then switch back on those to quarks.
  //  pythia.readString("23:onMode = off");
  //pythia.readString("23:onIfAny = 1 2 3 4 5");

  // LEP1 initialization at Z0 mass.
  //pythia.readString("Beams:idA =  11");
  //pythia.readString("Beams:idB = -11");
  //  double mZ = pythia.particleData.m0(23);

  pdt.mayDecay(13,false);
  pdt.mayDecay(-13,false);
  pdt.mayDecay(15,true);
  pdt.mayDecay(-15,true);
  pdt.mayDecay(130,false);
  pdt.mayDecay(310,true);
  pdt.mayDecay(111,true);
  pdt.mayDecay(211,false);  // pi+
  pdt.mayDecay(-211,false); // pi-
  pdt.mayDecay(311,false);
  pdt.mayDecay(-311,false);
  pdt.mayDecay(321,false);
  pdt.mayDecay(-321,false);
  pdt.mayDecay(2112,false);
  pdt.mayDecay(-2112,false);

  // Allow for possibility of a few faulty events.
  int nAbort = 10;
  int iAbort = 0;
  double Emin = 10;
  double Emax = 2000;
  int idiv = 1;
  std::ofstream ofsGamE("Nch.dat");
  double nevents;
  int nCh;

  for (int j = 0; j < idiv; ++j) {
    double rdiv = idiv;
    double E = pow(10,(log10(Emin) +(log10(Emax) -log10(Emin))/rdiv*j));
    pythia.settings.parm("Beams:eCM", E);
    pythia.init();

    nevents = 0;
    for (int iEvent = 0; iEvent < 10000; ++iEvent) {
      // Generate events, and check whether generation failed.
      if (!pythia.next()) {
	// If failure because reached end of file then exit event loop.
	if (pythia.info.atEndOfFile()) break;
	// First few failures write off as "acceptable" errors, then quit.
	if (++iAbort < nAbort) continue;
	break;
	
	nCh = 0;
	for (int i = 0; i < pythia.event.size(); ++i)
	  if (pythia.event[i].isFinal() && pythia.event[i].isCharged()) ++nCh;
	
      }
      nevents = nevents +1;
      // End of event loop.
    }
    cout << nCh << endl;
    ofsGamE << E << " " << nCh/nevents << endl;
  }

  return 0;
}




