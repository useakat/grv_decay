C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     (Gamma(2,2,-1)*ProjP(-1,1)) * C(51,2) * C(52,1)
C     
      SUBROUTINE FRS7C1_0(R2, F1, S3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 S3(*)
      COMPLEX*16 R2(*)
      COMPLEX*16 TMP7
      COMPLEX*16 F1(*)
      COMPLEX*16 VERTEX
      COMPLEX*16 COUP
      TMP7 = (F1(5)*-1D0*(R2(3)+R2(8)+R2(15)-CI*(R2(12)))-F1(6)*(R2(4)
     $ +R2(7)+CI*(R2(11))-R2(16)))
      VERTEX = COUP*-CI * TMP7*S3(3)
      END


