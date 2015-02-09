import pickle
import numpy as np

p1 = open('anthprot.pkl', 'rb')
p2 = open('anthprotbc.pkl', 'rb')
p3 = open('anthprothalo.pkl', 'rb')

anthprot = pickle.load(p1)
anthprotbc = pickle.load(p2)
anthprothalo = pickle.load(p3)

traina = []
trainb = []

for x in anthprot[0]:
    traina.append(np.asarray(x))
for x in anthprot[1]:
    trainb.append(x)
for y in anthprotbc[0]:
    traina.append(np.asarray(y))
for y in anthprotbc[1]:
    trainb.append(y)
for z in anthprothalo[0]:
    traina.append(np.asarray(z))
for z in anthprothalo[1]:
    trainb.append(z)
traina = np.asarray(traina)
trainb = np.asarray(trainb)
out = open('traina.pkl', 'wb')
data = [traina, trainb]
pickle.dump(data, out)
out.close()
