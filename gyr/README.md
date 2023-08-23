# AB diblock gyroid example

## Notes:
 - The initial guess in this example, `in/c.bf`, uses only the first
   two nonzero basis functions for the `I_a_-3_d` space group. This
   is similar to identifying the gyroid by its first two scattering 
   peaks. For many phases, this would not work, and a better initial
   guess would be required. However, SCFT is robust enough to find
   the correct solution in this case! It helps that this space 
   group has such high symmetry, and that we set up the calculation
   to correspond to a gyroid-forming diblock.

## To run the code:
In terminal, run `pscf_pc3 -e -p param -c command`
