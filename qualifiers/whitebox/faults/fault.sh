#!/bin/bash

rounds=('10 9 8 7 6 5 4 3 2')
faults=('0x41 0x42 0x43 0x44 0x45 0x46 0x47 0x48 0xff 0x00')
offsets=('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')
for round in ${rounds[@]}; do
	echo "Round $round"
	echo "$(./whitebox AAAABBBBCCCCDDDD | sed -e "s/ //g")" > round$round.log
	for fault in ${faults[@]}; do
		for offset in ${offsets[@]}; do
			echo "$(cat fault.gdb | sed -e "s/{{round}}/$((round-2))/" | sed -e "s/{{fault}}/$fault/" | sed -e "s/{{offset}}/$offset/" | gdb -q whitebox | grep -v gdb | grep -v Inferior | grep -v Breakpoint | grep -v Reading | grep . | sed 's/ //g' 2>/dev/null)" >> round$round.log
		done
	done
done

# first round - didn't work!
offsets=('0 1 2 3 4 5 6 7 8 9 10 11 12')
faults=('00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f')
echo "Round 1"
echo "$(./whitebox AAAABBBBCCCCDDDD | sed -e "s/ //g")" > round1.log
for fault in ${faults[@]}; do
	for offset in ${offsets[@]}; do
		echo "$(cat first_round.gdb | sed -e "s/{{fault}}/$fault/g" | sed -e "s/{{offset}}/$offset/" | gdb -q whitebox | grep -v gdb | grep -v Inferior | grep -v Breakpoint | grep -v Reading | grep . | sed 's/ //g' 2>/dev/null)" >> round1.log
	done
done
