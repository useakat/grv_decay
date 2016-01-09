*HOW TO USE this package

0. Prerequisites
   PYTHIA 8
   SPheno (optional)
   slhaplot (optional)

1.preparation of param_card_temp.dat:

   <Using SUSYHIT>
     cd susyhit
     make
     modify susyhit.in
     modify suspect2_lha.in (or slhaspectrum.in when you do not use SUSPECT)
     ./run (Suspect-SDECAY-HDECAY or SDECAY-HDECAY)
     ./run.sh (SOFTSUSY-SDECAY-HDECAY)

   <Using SPheno>
     cd SUSYspc
     SPheno LesHouches.in

   <Using SOFTSUSY>
     cd SUSYspc
     softpoint.x leshouches < [softsusy].in > [softsusy].spc

   <modify output SLHA file>
     add 1000049 MMGRV # Mgrv to MASS COMMON BLOCK
     add the following lines to the end of the file
       DECAY 1000049 0.000000e+00 # Wgrv
       #===========================================================
       # QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)
       #===========================================================
       Block QNUMBERS 1000049  # grv
               1 0  # 3 times electric charge
               2 4  # number of spin states (2S+1)
               3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
               4 0  # Particle/Antiparticle distinction (0=own anti)

   <Comments>
    Please check your parameter card so that MODSEL and MINPAR is set 
   appropreately. Inappropreate settings would cause many abortions in
   Pythia run.

   In DECAY blocks, width should not be too small, otherwise pythia 
   doesn't work correctly (width should be larger at least 10^-12 GeV)

   It is highly recommended to check allprocess.log in par_n folder and 
   ensure that there is not many abortion or erros in Pythia run. 


2. Prepare MG5 directory
   cp grv_decay_def grv_decay
   cd grv_decay
   cp ../susyhit/XXX.slha Card/param_card_temp.dat
     

3. Modify relevant files
   * run_grv_decay_parallel.sh
      chi0mass: change to the LSP mass
      nevents (L35 & L38)


4. Run
   ./run.sh


5. Notes
