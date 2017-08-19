b *0x4636EA
ignore 1 {{round}}
run AAAABBBBCCCCDDDD
d 1
print /x 0x7fffffffeb20+{{offset}}
set *(char*)$1={{fault}}
c
quit
