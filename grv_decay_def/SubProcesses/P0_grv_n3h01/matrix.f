      SUBROUTINE SMATRIX(P,ANS)
C     
C     Generated by MadGraph5_aMC@NLO v. 2.1.2, 2014-07-03
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     MadGraph5_aMC@NLO for Madevent Version
C     
C     Returns amplitude squared summed/avg over colors
C     and helicities
C     for the point in phase space P(0:3,NEXTERNAL)
C     
C     Process: grv > n3 h01
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INCLUDE 'genps.inc'
      INCLUDE 'maxconfigs.inc'
      INCLUDE 'nexternal.inc'
      INCLUDE 'maxamps.inc'
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=8)
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=1)
      INTEGER    NDIAGS
      PARAMETER (NDIAGS=1)
      INTEGER    THEL
      PARAMETER (THEL=NCOMB)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL),ANS
C     
C     LOCAL VARIABLES 
C     
      INTEGER NHEL(NEXTERNAL,NCOMB),NTRY
      REAL*8 T,MATRIX
      REAL*8 R,SUMHEL,TS(NCOMB)
      INTEGER I,IDEN
      INTEGER IPROC,JC(NEXTERNAL),II
      LOGICAL GOODHEL(NCOMB)
      REAL*8 HWGT, XTOT, XTRY, XREJ, XR, YFRAC(0:NCOMB)
      INTEGER IDUM, NGOOD, IGOOD(NCOMB), JHEL, J, JJ
      REAL     XRAN1
      EXTERNAL XRAN1
C     
C     GLOBAL VARIABLES
C     
      DOUBLE PRECISION AMP2(MAXAMPS), JAMP2(0:MAXFLOW)
      COMMON/TO_AMPS/  AMP2,       JAMP2

      CHARACTER*101        HEL_BUFF
      COMMON/TO_HELICITY/  HEL_BUFF

      REAL*8 POL(2)
      COMMON/TO_POLARIZATION/ POL

      INTEGER          ISUM_HEL
      LOGICAL                    MULTI_CHANNEL
      COMMON/TO_MATRIX/ISUM_HEL, MULTI_CHANNEL
      INTEGER MAPCONFIG(0:LMAXCONFIGS), ICONFIG
      COMMON/TO_MCONFIGS/MAPCONFIG, ICONFIG
      DATA NTRY,IDUM /0,-1/
      DATA XTRY, XREJ, NGOOD /0,0,0/
      SAVE YFRAC, IGOOD, JHEL
      DATA GOODHEL/THEL*.FALSE./
      DATA (NHEL(I,   1),I=1,3) /-3,-1, 0/
      DATA (NHEL(I,   2),I=1,3) /-3, 1, 0/
      DATA (NHEL(I,   3),I=1,3) /-1,-1, 0/
      DATA (NHEL(I,   4),I=1,3) /-1, 1, 0/
      DATA (NHEL(I,   5),I=1,3) / 1,-1, 0/
      DATA (NHEL(I,   6),I=1,3) / 1, 1, 0/
      DATA (NHEL(I,   7),I=1,3) / 3,-1, 0/
      DATA (NHEL(I,   8),I=1,3) / 3, 1, 0/
      DATA IDEN/ 4/
C     ----------
C     BEGIN CODE
C     ----------
      NTRY=NTRY+1
      DO I=1,NEXTERNAL
        JC(I) = +1
      ENDDO

      IF (MULTI_CHANNEL) THEN
        DO I=1,NDIAGS
          AMP2(I)=0D0
        ENDDO
        JAMP2(0)=1
        DO I=1,INT(JAMP2(0))
          JAMP2(I)=0D0
        ENDDO
      ENDIF
      ANS = 0D0
      WRITE(HEL_BUFF,'(20I5)') (0,I=1,NEXTERNAL)
      DO I=1,NCOMB
        TS(I)=0D0
      ENDDO
      IF (ISUM_HEL .EQ. 0 .OR. NTRY .LE. MAXTRIES) THEN
        DO I=1,NCOMB
          IF (GOODHEL(I) .OR. NTRY .LE. MAXTRIES) THEN
            T=MATRIX(P ,NHEL(1,I),JC(1))
            DO JJ=1,NINCOMING
              IF(POL(JJ).NE.1D0.AND.NHEL(JJ,I).EQ.INT(SIGN(1D0
     $         ,POL(JJ)))) THEN
                T=T*ABS(POL(JJ))
              ELSE IF(POL(JJ).NE.1D0)THEN
                T=T*(2D0-ABS(POL(JJ)))
              ENDIF
            ENDDO
            ANS=ANS+T
            TS(I)=T
          ENDIF
        ENDDO
        JHEL = 1
        IF(NTRY.LE.MAXTRIES)THEN
          DO I=1,NCOMB
            IF (.NOT.GOODHEL(I) .AND. (TS(I).GT.ANS*LIMHEL/NCOMB)) THEN
              GOODHEL(I)=.TRUE.
              NGOOD = NGOOD +1
              IGOOD(NGOOD) = I
              PRINT *,'Adding good helicity ',I,TS(I)/ANS
            ENDIF
          ENDDO
        ENDIF
        IF(NTRY.EQ.MAXTRIES)THEN
          ISUM_HEL=MIN(ISUM_HEL,NGOOD)
        ENDIF
      ELSE  !RANDOM HELICITY
        DO J=1,ISUM_HEL
          JHEL=JHEL+1
          IF (JHEL .GT. NGOOD) JHEL=1
          HWGT = REAL(NGOOD)/REAL(ISUM_HEL)
          I = IGOOD(JHEL)
          T=MATRIX(P ,NHEL(1,I),JC(1))
          DO JJ=1,NINCOMING
            IF(POL(JJ).NE.1D0.AND.NHEL(JJ,I).EQ.INT(SIGN(1D0,POL(JJ)))
     $       ) THEN
              T=T*ABS(POL(JJ))
            ELSE IF(POL(JJ).NE.1D0)THEN
              T=T*(2D0-ABS(POL(JJ)))
            ENDIF
          ENDDO
          ANS=ANS+T*HWGT
          TS(I)=T*HWGT
        ENDDO
        IF (ISUM_HEL .EQ. 1) THEN
          WRITE(HEL_BUFF,'(20i5)')(NHEL(II,I),II=1,NEXTERNAL)
        ENDIF
      ENDIF
      IF (ISUM_HEL .NE. 1) THEN
        R=XRAN1(IDUM)*ANS
        SUMHEL=0D0
        DO I=1,NCOMB
          SUMHEL=SUMHEL+TS(I)
          IF(R.LT.SUMHEL)THEN
            WRITE(HEL_BUFF,'(20i5)')(NHEL(II,I),II=1,NEXTERNAL)
            GOTO 10
          ENDIF
        ENDDO
 10     CONTINUE
      ENDIF
      IF (MULTI_CHANNEL) THEN
        XTOT=0D0
        DO I=1,NDIAGS
          XTOT=XTOT+AMP2(I)
        ENDDO
        IF (XTOT.NE.0D0) THEN
          ANS=ANS*AMP2(MAPCONFIG(ICONFIG))/XTOT
        ELSE
          ANS=0D0
        ENDIF
      ENDIF
      ANS=ANS/DBLE(IDEN)
      END


      REAL*8 FUNCTION MATRIX(P,NHEL,IC)
C     
C     Generated by MadGraph5_aMC@NLO v. 2.1.2, 2014-07-03
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Returns amplitude squared summed/avg over colors
C     for the point with external lines W(0:6,NEXTERNAL)
C     
C     Process: grv > n3 h01
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=1)
      INCLUDE 'genps.inc'
      INCLUDE 'nexternal.inc'
      INCLUDE 'maxamps.inc'
      INTEGER    NWAVEFUNCS,     NCOLOR
      PARAMETER (NWAVEFUNCS=3, NCOLOR=1)
      REAL*8     ZERO
      PARAMETER (ZERO=0D0)
      COMPLEX*16 IMAG1
      PARAMETER (IMAG1=(0D0,1D0))
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
C     
C     LOCAL VARIABLES 
C     
      INTEGER I,J
      COMPLEX*16 ZTEMP
      REAL*8 DENOM(NCOLOR), CF(NCOLOR,NCOLOR)
      COMPLEX*16 AMP(NGRAPHS), JAMP(NCOLOR)
      COMPLEX*16 W(18,NWAVEFUNCS)
C     Needed for v4 models
      COMPLEX*16 DUM0,DUM1
      DATA DUM0, DUM1/(0D0, 0D0), (1D0, 0D0)/
C     
C     GLOBAL VARIABLES
C     
      DOUBLE PRECISION AMP2(MAXAMPS), JAMP2(0:MAXFLOW)
      COMMON/TO_AMPS/  AMP2,       JAMP2
      INCLUDE 'coupl.inc'
C     
C     COLOR DATA
C     
      DATA DENOM(1)/1/
      DATA (CF(I,1),I=1,1) /1/
C     ----------
C     BEGIN CODE
C     ----------
      CALL IRXXXX(P(0,1),MDL_MGRV,NHEL(1),+1*IC(1),W(1,1))
      CALL OXXXXX(P(0,2),MDL_MNEU3,NHEL(2),+1*IC(2),W(1,2))
      CALL SXXXXX(P(0,3),+1*IC(3),W(1,3))
C     Amplitude(s) for diagram number 1
      CALL FRS2_4_7_9C1_0(W(1,1),W(1,2),W(1,3),GC_2432,GC_2420,GC_2380
     $ ,GC_2298,AMP(1))
      JAMP(1)=+AMP(1)
      MATRIX = 0.D0
      DO I = 1, NCOLOR
        ZTEMP = (0.D0,0.D0)
        DO J = 1, NCOLOR
          ZTEMP = ZTEMP + CF(J,I)*JAMP(J)
        ENDDO
        MATRIX=MATRIX+ZTEMP*DCONJG(JAMP(I))/DENOM(I)
      ENDDO
      AMP2(1)=AMP2(1)+AMP(1)*DCONJG(AMP(1))
      DO I = 1, NCOLOR
        JAMP2(I)=JAMP2(I)+JAMP(I)*DCONJG(JAMP(I))
      ENDDO

      END

