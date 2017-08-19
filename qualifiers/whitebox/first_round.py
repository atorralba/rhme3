import deadpool_dfa
import phoenixAES

def processinput(iblock, blocksize):
	inp = (bytes.fromhex('%0*x' % (2*blocksize, iblock)), [ '--stdin' ])
	return inp

def processoutput(output, blocksize):
	out = int(output.decode('utf-8').strip().replace(' ',''),16)
	return out

encrypt = True
outputbeforelastrounds = False
verbose = 1

engine = deadpool_dfa.Acquisition('./whitebox', 'whitebox.bin', './whitebox.gold',
	phoenixAES, processinput=processinput, processoutput=processoutput, encrypt=encrypt,
	verbose=verbose)

with open('lastroundkeys.lst', 'r') as f:
	lastroundkeys = f.readlines()

foundkey = False
tracefiles_sets = engine.runoninput(lastroundkeys)
tracefiles = tracefiles_sets[0]

for tracefile in tracefiles:
	k=phoenixAES.crack(tracefile, lastroundkeys, encrypt, outputbeforelastrounds and len(lastroundkeys)>0, verbose)
	if k:
		foundkey=True
		lastroundkeys.append(k)
		break

if foundkey:
	p = 0 # null plaintext
	cint,_,_ = engine.doit(engine.goldendata, processinput(p, 16), lastroundkeys=[])
	c = [(cint>>(i<<3) & 0xff) for i in range(16)][::-1]
	kr0 = phoenixAES.rewind(cint, lastroundkeys, encrypt=encrypt, mimiclastround=False)

	# Be cautious, round key could be wrong if there is some external encoding...
	found_key = '%032X' % kr0
	print("First round key found?:\n%s" % found_key)
	lastroundkeys.append(found_key)
	print(bytes.fromhex(found_key).decode('utf-8'))
else:
	print('Key not found, sorry!')
