# Solution to the Whitebox RHme3 Qualifier challenge

The solution is divided in two scripts:

+ `dfa_rounds.py` performs DFA on rounds 10 to 2 of the AES algorithm, finding
the corresponding round keys. It saves them to the file `lastroundkeys.lst`.

+ By reading `lastroundkeys.lst`, `first_round.py` injects faults into the first
AES round and finds the corresponding round key and so obtains the full AES cipher
key.

The `faults` directory contains the GDB instructions and the shell script used to
inject faults at the beginning of every AES round up until round 2, and the list
of faulty outputs generated.

## Dependencies

This solution **heavily** relies on the excellent tools of [SideChannelMarvels](https://github.com/SideChannelMarvels),
more specifically [Deadpool](https://github.com/SideChannelMarvels/Deadpool)
and [JeanGrey](https://github.com/SideChannelMarvels/JeanGrey).
