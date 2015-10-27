      FUNCTION GET_COLOR(IPDG)
      IMPLICIT NONE
      INTEGER GET_COLOR, IPDG

      IF(IPDG.EQ.35)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.1000025)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.1000049)THEN
        GET_COLOR=1
        RETURN
      ELSE IF(IPDG.EQ.7)THEN
C       This is dummy particle used in multiparticle vertices
        GET_COLOR=2
        RETURN
      ELSE
        WRITE(*,*)'Error: No color given for pdg ',IPDG
        GET_COLOR=0
        RETURN
      ENDIF
      END

