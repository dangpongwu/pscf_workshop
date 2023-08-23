# AB diblock lamellar example

## Notes:
 - The initial guess in this example, `in/c.rf`, is constructed using
   the "level-set" method. In this method, we estimate the shape of
   the domains, and set the volume fractions to be constant within
   each domain. Here, we set the majority-block fraction to 0.9 and
   the minority block fraction to 0.1, and we estimate the domain 
   shapes to simply be alternating A- and B-domains of equal width.
   The python script `edit_rgrid.py` was used to generate this guess.

## To run the code:
In terminal, run `pscf_pc1 -e -p param -c command`
