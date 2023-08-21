# AB diblock Sweep Steps
## Objective:
For $\chi N = 20$, the goal is to obtain converged solutions for $f_{A}$ values: 0.5, 0.52, 0.54, 0.56, and 0.58.

### Sweep Documentation:
Detail information regarding sweep can be found in:
https://dmorse.github.io/pscfpp-man/user_param_sweep_page.html

### Sweep steps:
1. Obtain converged solution at $\chi N = 20$ and $f_{A} = 0.5$ (initial state of the sweep).
2. Copy the converged solution (out/w.bf) at $\chi N = 20$ and $f_{A} = 0.5$ to sweep "in" folder.
3. Modify the command file as following:
    * `READ_W_BASIS  in/w.bf` Read an initial guess for the chemical potential fields at the initial state of the sweep (the state s=0) from the file in/w.bf
    * `SWEEP` Executes a sweep operation
    * `FINISH` Finish execution 
4. Modify param file:
    * After Iterator/AmIterator block, add a LinearSweep block. (`LinearSweep{}`)
    * Inside the curly brackets, specify sweep parameters: 
     * Number of step changes in the parameter values(`ns    4`)
     * Prefix added to the names of output files (`baseFileName out/`)
     * Number of parameters that are modified during the sweep (`nParameter  2`)
        * To keep $N = 1$, the block lengths of both A and B should be modified.
     * Magnitude of change for each parameter(`parameters[]`)
        * Inside the square brackets, each line specify one parameter
            * For block length of A (`block  0 0 +0.08`)
                * `block` is parameter type identifier string
                * First number (`0`) is the index of polymer species 
                * Second number (`0`) is the index of A block within the polymer
                * Third number (`+0.08`) is the magnitude of change
            * For block length of B (`block  0 1 -0.08`)

5. In terminal, run `pscf_pc1 -e -p param -c command`
