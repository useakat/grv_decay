C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(2,2,-1)*ProjM(-1,1)
C     
      SUBROUTINE FRS2_0(F1, R2, S3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 S3(*)
      COMPLEX*16 R2(*)
      COMPLEX*16 F1(*)
      COMPLEX*16 VERTEX
      COMPLEX*16 COUP
      COMPLEX*16 TMP8
      TMP8 = (F1(3)*(R2(5)+R2(10)+R2(17)+CI*(R2(14)))+F1(4)*(R2(6)
     $ +R2(9)-CI*(R2(13))-R2(18)))
      VERTEX = COUP*-CI * TMP8*S3(3)
      END


