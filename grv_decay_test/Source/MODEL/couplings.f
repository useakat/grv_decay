ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP()

      IMPLICIT NONE
      DOUBLE PRECISION PI, ZERO
      LOGICAL READLHA
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      READLHA = .TRUE.
      INCLUDE 'intparam_definition.inc'
      CALL COUP1()
      CALL COUP2()
      CALL COUP3()
      CALL COUP4()
      CALL COUP5()
      CALL COUP6()
      CALL COUP7()
      CALL COUP8()
      CALL COUP9()
C     
C     couplings needed to be evaluated points by points
C     
      CALL COUP10()

      RETURN
      END

      SUBROUTINE UPDATE_AS_PARAM()

      IMPLICIT NONE
      DOUBLE PRECISION PI, ZERO
      LOGICAL READLHA
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      READLHA = .FALSE.

      INCLUDE 'intparam_definition.inc'


C     
C     couplings needed to be evaluated points by points
C     
      CALL COUP10()

      RETURN
      END
