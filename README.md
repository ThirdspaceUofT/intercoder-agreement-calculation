# intercoder-agreement-calculation

<a name="usage"></a>
## Usage

<a name="1"></a>
### 1. calculate cohen's kappa

```console
$ cd basic
$ python basic.py
Cohen's Kappa: 0.689926604606
```


<a name="2"></a>
### 2. calculate weighted kappa (generalized)
```console
$ cd weighted
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
$ cd multi-label
$ python multilabel.py data.csv
Weighted Kappa: 0.723481095176
Weighted Observed Agreement: 0.945209973753
Weighted Agreement by Chance: 0.801857937049
```
