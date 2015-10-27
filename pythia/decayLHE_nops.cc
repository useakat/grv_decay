#include <iostream>
#include "Pythia8/Pythia.h"

using namespace Pythia8;

int main(int argc, char *argv[]) {

  char *ends;
  double mDM = strtod(argv[1], &ends);

  double ECM = mDM;

  double xmin = 0.010;
  double xmax = 1000000.;
  int nbins = 800;
  double *x = new double[nbins];
  for (int i = 0; i < nbins+1; ++i) {
    //    x[i] = xmin +(xmax -xmin)/nbins*i;
    x[i] = pow(10,log10(xmin) +(log10(xmax) -log10(xmin))/float(nbins)*i);
  }

  std::ofstream ofsnp("np_sptrm.dat");
  for (int i = 0; i < nbins+1; ++i) {
    ofsnp << setiosflags(ios::scientific) << ECM << " " << x[i] << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " 
	  << 0 << " " << 1e99 << " " << endl;
  }

  //int Total = GamE.getEntries();
  std::ofstream ofsGamE("Edist.dat");
  ofsGamE << 0.0 << " " << 0.0 << " " << 0.0 << endl;
  for (int i = 0; i < nbins+1; ++i) {
    ofsGamE << x[i] << " " << 0.0 << " " << 0.0 << " " << 0.0 << endl;
  }

  std::ofstream ofsnini("nini.dat");
  ofsnini << setiosflags(ios::scientific) << ECM << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " 
	  << 0.0 << " " << 0.0 << " " << 0.0 << " " << 0.0 << " " 
	  << 0.0 << " " << 0.0 <<  " " << 1e99 << " " << endl;

  std::ofstream ofsEvis("Evis.dat");
  ofsEvis << setiosflags(ios::scientific) << ECM << " " << 0.0 << " "  << 0.0 <<  " " << 1e99 << " " << endl;

  // Done.
  return 0;
}
