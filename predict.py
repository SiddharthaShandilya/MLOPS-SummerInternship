import sys

import joblib as jb

model = jb.load('Saalry2.pk1')

ar = sys.argv

exp = int(ar[1])

p = model.predict([[exp]])

print(p)
