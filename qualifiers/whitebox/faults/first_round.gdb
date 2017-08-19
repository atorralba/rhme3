b *0x46368C
d 1
b *0x463708
run AAAABBBBCCCCDDDD
d 2
print /x 0x7fffffffe9c0+{{offset}}
set *$1=0x{{fault}}{{fault}}{{fault}}{{fault}}
c
quit
