# intercoder-agreement-calculation


## Usage

### 1. calculate cohen's kappa

```console
$ cd basic
$ python basic.py
The Cohen's Kappa coefficient between coders C1 and C2 is 0.689926604606.
```
### 2. calculate weighted kappa

```console
$ cd weighted_kappa
$ python weighted_kappa.py
The weighted Kappa between coders C1 and C2 is 0.29021832124.
The weighted observed-agreement is 0.72.
The weighted agreement-by-chance is 0.6055125.
```

### 3. generalize
```console
$ cd generalized
$ python generalized.py data.csv weights.txt
The weighted Kappa between coders C1 and C2 is 0.749071251175.
The weighted observed-agreement is 0.924759405074.
The weighted agreement-by-changce is 0.700151555859.
```
