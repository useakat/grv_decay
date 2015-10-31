      program test
      implicit none
      real*8 a

      a = 3+ 5
      open(1,file="out.dat",status="replace")
      write(1,*) a
      close(1)

      end
