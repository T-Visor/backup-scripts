import sys
import time

print("Loading:")

animation_states = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
             "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
             "[■■■■■■■■■□]", "[■■■■■■■■■■]", "[□■■■■■■■■■]", "[□□■■■■■■■■]",
             "[□□□■■■■■■■]", "[□□□□■■■■■■]", "[□□□□□■■■■■]", "[□□□□□□■■■■]",
             "[□□□□□□□■■■]", "[□□□□□□□□■■]", "[□□□□□□□□□■]", "[□□□□□□□□□□]" ]

i = 0
# for i in range(len(animation_states)):
while True:
    time.sleep(0.2)
    sys.stdout.write("\r" + animation_states[i % len(animation_states)])
    sys.stdout.flush()
    i += 1

print("\n")
