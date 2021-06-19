#!/usr/bin/env python
# Copyright 2021 Jérôme Dumonteil
# Licence: MIT
# Authors: jerome.dumonteil@gmail.com
"""Calculate Kolakoski Sequence and Kolakoski Constant

Compute Kolakoski Sequence and check against known value of Kolakoski Constant.
"""
from decimal import Decimal, getcontext  # to compute Kolakoski Constant

# number o steps of the sequence, change this if needed :
steps = 200

# Start with empty sequence, but could directly start with usual [1, 2, 2]
seq = []
digit, other = 1, 2  # to alternate odd/even values without computation
seq.extend([digit] * digit)
digit, other = other, digit
seq.extend([digit] * digit)  # Here we shoud have the [1, 2, 2] actual starting values

digit, other = other, digit
index = 2
while index < steps:
    seq.extend([digit] * seq[index])  # core of Kolakoski iteration
    index += 1
    digit, other = other, digit

print(f"Kolakoski Sequence, {len(seq)} digits:")
print(str(seq)[1:-1].replace(",", ""))

# checking against reference value
getcontext().prec = 76
kc = Decimal(0)
pow = 1
for i in seq:
    pow -= 1
    if i == 1:
        continue
    kc += Decimal(2) ** Decimal(pow)

reference = Decimal(
    "0.7945071927794792762403624156360456462985771009886069672658867371538147750246"
)
print(
    "\nApproximation of Kolakoski Constant from this sequence, \n"
    "followed by first digits of reference value and difference \n"
    "(value from http://plouffe.fr/simon/constants/Kolakoski.txt):"
)
print(kc)
print(reference)
print(kc - reference)
