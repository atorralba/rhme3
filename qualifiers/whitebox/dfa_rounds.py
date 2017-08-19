import phoenixAES

foundkey = True
lastroundkeys = []
round = 10
while foundkey and round > 1:
    print("Round %i" % round)
    foundkey = False
    k = phoenixAES.crack('faults/round%d.lst' % round,
        lastroundkeys=lastroundkeys,
        outputbeforelastrounds=False,
        verbose=1)
    if k:
        foundkey = k not in lastroundkeys
        lastroundkeys.append(k)
        round -= 1

with open('lastroundkeys.lst','w+') as f:
    for key in lastroundkeys:
        f.write("%s\n" % key)
