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
$ python3 weighted.py data.csv weights.txt
Weighted Kappa: 0.7490712511745773
```

```console
$ python3 weighted.py data1.csv weights1.txt
Weighted Kappa: 0.2902183212395829
```

<a name="3"></a>
### 3. calculate kappa with multiple labels
```console
$ cd 3-multilabel
$ python3 multilabel.py data.csv
Weighted Kappa: 0.7234810951760119
```

### 4. calculate Krippendorff's alpha
```console
$ cd 4-krippendorff-alpha
$ python3 alpha.py -h
usage: alpha.py [-h] [-w WEIGHTS] {nominal,ordinal} data

This program calculates Krippendorff's Alpha given nominal data or ordinal data.

positional arguments:
  {nominal,ordinal}     set level of measurement
  data                  set the data file

optional arguments:
  -h, --help            show this help message and exit
  -w WEIGHTS, --weights WEIGHTS
                        set the weights file, required for ordinal data only
```
```console
$ python3 alpha.py nominal data.csv
Krippendorff's alpha for nominal metric:  0.6722775059943613
```
```console
$ python3 alpha.py ordinal -w weights1.txt data1.csv
Krippendorff's alpha for ordinal metric:  0.3136278980049674
```


