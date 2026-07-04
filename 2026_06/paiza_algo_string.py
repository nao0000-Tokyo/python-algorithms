# Paiza C Rank Level-Up Problem
# Topic: String Processing and Time Calculation
# Key Concepts: split(), zero-padding, handling minute overflow


N = int(input())

for i in range(N):
    t,h,m = input().split()
    st_h, st_m = t.split(":")
    aftr_h = int(st_h) + int(h)
    aftr_m = int(st_m) + int(m)
    if int(aftr_m) > 59:
        aftr_m -= 60
        aftr_h += 1
    aftr_h %= 24
    print(f"{aftr_h:02}:{aftr_m:02}")