# intercoder-agreement-calculation

<a name="usage"></a>
## Usage

<a name="1"></a>
### 1. calculate cohen's kappa

```console
$ cd 1-basic
$ python3 basic.py data.csv
Cohen's Kappa: 0.6899266046058918
```


<a name="2"></a>
### 2. calculate weighted kappa (generalized)
```console
$ cd 2-weighted
$ python weighted.py data.csv weights.txt
Weighted Kappa: 0.749071251175
```

```console
$ python weighted.py data1.csv weights1.txt
Weighted Kappa: 0.29021832124
```

<a name="3"></a>
### 3. calculate kappa with multiple labels
```console
$ cd 3-multilabel
$ python multilabel.py data.csv
Weighted Kappa: 0.723481095176
```
