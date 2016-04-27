      DOUBLE PRECISION FUNCTION DSIG(PP,WGT,IMODE)
C     ****************************************************
C     
C     Generated by MadGraph5_aMC@NLO v. 2.3.3, 2015-10-25
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Process: grv > h2 n3 @1
C     
C     RETURNS DIFFERENTIAL CROSS SECTION
C     Input:
C     pp    4 momentum of external particles
C     wgt   weight from Monte Carlo
C     imode 0 run, 1 init, 2 reweight, 
C     3 finalize, 4 only PDFs,
C     5 squared amplitude only (never
C     generate events)
C     Output:
C     Amplitude squared and summed
C     ****************************************************
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INCLUDE 'genps.inc'
      INCLUDE 'nexternal.inc'
      INCLUDE 'maxconfigs.inc'
      INCLUDE 'maxamps.inc'
      DOUBLE PRECISION       CONV
      PARAMETER (CONV=389379.66*1000)  !CONV TO PICOBARNS
      REAL*8     PI
      PARAMETER (PI=3.1415926D0)
C     
C     ARGUMENTS 
C     
      DOUBLE PRECISION PP(0:3,NEXTERNAL), WGT
      INTEGER IMODE
C     
C     LOCAL VARIABLES 
C     
      INTEGER I,ITYPE,LP,IPROC

      DOUBLE PRECISION XPQ(-7:7),PD(0:MAXPROC)
      DOUBLE PRECISION DSIGUU,R,RCONF
      INTEGER LUN,ICONF,IFACT,NFACT
      DATA NFACT/1/
      SAVE NFACT
C     
C     EXTERNAL FUNCTIONS
C     
      LOGICAL PASSCUTS
      DOUBLE PRECISION ALPHAS2,REWGT,PDG2PDF
      INTEGER NEXTUNOPEN
C     
C     GLOBAL VARIABLES
C     
      INTEGER          IPSEL
      COMMON /SUBPROC/ IPSEL
C     MINCFIG has this config number
      INTEGER           MINCFIG, MAXCFIG
      COMMON/TO_CONFIGS/MINCFIG, MAXCFIG
      INTEGER MAPCONFIG(0:LMAXCONFIGS), ICONFIG
      COMMON/TO_MCONFIGS/MAPCONFIG, ICONFIG
C     Keep track of whether cuts already calculated for this event
      LOGICAL CUTSDONE,CUTSPASSED
      COMMON/TO_CUTSDONE/CUTSDONE,CUTSPASSED

      INCLUDE 'coupl.inc'
      INCLUDE 'run.inc'
C     
C     DATA
C     

C     ----------
C     BEGIN CODE
C     ----------
      DSIG=0D0
      CUTSDONE=.FALSE.
      CUTSPASSED=.FALSE.
      IF(IMODE.EQ.1)THEN
C       Set up process information from file symfact
        LUN=NEXTUNOPEN()
        NFACT=1
        OPEN(UNIT=LUN,FILE='../symfact.dat',STATUS='OLD',ERR=20)
        DO WHILE(.TRUE.)
          READ(LUN,*,ERR=10,END=10) RCONF, IFACT
          ICONF=INT(RCONF)
          IF(ICONF.EQ.MAPCONFIG(MINCFIG))THEN
            NFACT=IFACT
          ENDIF
        ENDDO
 10     CLOSE(LUN)
        RETURN
 20     WRITE(*,*)'Error opening symfact.dat. No symmetry factor used.'
        RETURN
      ENDIF
C     Continue only if IMODE is 0, 4 or 5
      IF(IMODE.NE.0.AND.IMODE.NE.4.AND.IMODE.NE.5) RETURN

      IF (PASSCUTS(PP)) THEN
        PD(0) = 0D0
        IPROC = 0
        IPROC=IPROC+1  ! grv > h2 n3
        PD(IPROC)=1D0

        PD(0)=PD(0)+PD(IPROC)
        IF (IMODE.EQ.4)THEN
          DSIG = PD(0)
          RETURN
        ENDIF
        CALL SMATRIX(PP,DSIGUU)
        IF (IMODE.EQ.5) THEN
          IF (DSIGUU.LT.1D199) THEN
            DSIG = DSIGUU*CONV
          ELSE
            DSIG = 0.0D0
          ENDIF
          RETURN
        ENDIF
C       Select a flavor combination (need to do here for right sign)
        CALL RANMAR(R)
        IPSEL=0
        DO WHILE (R.GE.0D0 .AND. IPSEL.LT.IPROC)
          IPSEL=IPSEL+1
          R=R-DABS(PD(IPSEL))/PD(0)
        ENDDO
        DSIGUU=DSIGUU*REWGT(PP)*NFACT
        IF (DSIGUU.LT.1D199) THEN
C         Set sign of dsig based on sign of PDF and matrix element
          DSIG=DSIGN(PD(0)*DSIGUU,DSIGUU*PD(IPSEL))
        ELSE
          WRITE(*,*) 'Error in matrix element'
          DSIGUU=0D0
          DSIG=0D0
        ENDIF
C       Generate events only if IMODE is 0.
        IF(IMODE.EQ.0.AND.DABS(DSIG).GT.0D0)THEN
C         Call UNWGT to unweight and store events
          CALL UNWGT(PP,DSIG*WGT,1)
        ENDIF
      ENDIF
      END
C     
C     Functionality to handling grid
C     

      SUBROUTINE WRITE_GOOD_HEL(STREAM_ID)
      IMPLICIT NONE
      INTEGER STREAM_ID
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=8)
      LOGICAL GOODHEL(NCOMB)
      INTEGER NTRY
      COMMON/BLOCK_GOODHEL/NTRY,GOODHEL
      WRITE(STREAM_ID,*) GOODHEL
      RETURN
      END


      SUBROUTINE READ_GOOD_HEL(STREAM_ID)
      IMPLICIT NONE
      INCLUDE 'genps.inc'
      INTEGER STREAM_ID
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=8)
      LOGICAL GOODHEL(NCOMB)
      INTEGER NTRY
      COMMON/BLOCK_GOODHEL/NTRY,GOODHEL
      READ(STREAM_ID,*) GOODHEL
      NTRY = MAXTRIES + 1
      RETURN
      END

      SUBROUTINE INIT_GOOD_HEL()
      IMPLICIT NONE
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=8)
      LOGICAL GOODHEL(NCOMB)
      INTEGER NTRY
      INTEGER I

      DO I=1,NCOMB
        GOODHEL(I) = .FALSE.
      ENDDO
      NTRY = 0
      END

      INTEGER FUNCTION GET_MAXSPROC()
      IMPLICIT NONE
      GET_MAXSPROC = 1
      RETURN
      END



