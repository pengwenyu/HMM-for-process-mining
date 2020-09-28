import numpy as np
np.set_printoptions(suppress=True)
from hmmlearn import hmm
np.random.seed(42)
#model = hmm.GaussianHMM(n_components=3, covariance_type="full")
#model.startprob_ = np.array([0.6, 0.3, 0.1])
#model.transmat_ = np.array([[0.7, 0.2, 0.1], [0.3, 0.5, 0.2],[0.3, 0.3, 0.4]])
#model.means_ = np.array([[0.0, 0.0], [3.0, -3.0], [5.0, 10.0]])
#model.covars_ = np.tile(np.identity(2), (3, 1, 1))
#X, Z = model.sample(100)
#print(X,Z)


model = hmm.GaussianHMM(n_components=8, covariance_type="full")
#model.startprob_ = np.array([1,0,0,0,0,0,0,0])
X1=[[1],[2],[3],[4],[5],[6],[8]]
X2=[[1],[2],[4],[3],[5],[6],[8]]
X3=[[1],[7],[8]]
X = np.concatenate([X1, X2, X3])
lengths = [len(X1), len(X2),len(X3)]
print(lengths)

for i in range(0,100):
    X=np.concatenate([X,X1]);
    lengths.append(len(X1))
for i in range(0,100):
    X=np.concatenate([X,X2]);
    lengths.append(len(X2))
for i in range(0,100):
    X=np.concatenate([X,X3]);
    lengths.append(len(X3))


model.fit(X,lengths)
X, Z = model.sample(100)
print(model.transmat_)
print(model)
#print(X)
#print(Z)
#print(len(X))
#print(len(Z))
