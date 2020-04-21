# intercoder-agreement-calculation
## Table of Contents
### [Usage](#usage)
   * [calculate cohen's kappa](#1)
   * [calculate weighted kappa (generalized)](#2)
   * [calculate kappa with multiple labels](#3)

<a name="usage"></a>
## Usage

<a name="1"></a>
### 1. calculate cohen's kappa

```console
$ cd basic
$ python basic.py
Cohen's Kappa: 0.689926604606
Observed Agreement: 0.733680227058
Agreement by Chance: 0.141107309114
```


<a name="2"></a>
### 2. calculate weighted kappa (generalized)
```console
$ cd weighted
$ python weighted.py data.csv weights.txt
Weighted Kappa: 0.749071251175
Weighted Observed Agreement: 0.924759405074
Weighted Agreement by Chance: 0.700151555859
```

```console
$ python weighted.py data1.csv weights1.txt
Weighted Kappa: 0.29021832124
Weighted Observed Agreement: 0.72 
Weighted Agreement by Chance: 0.6055125
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
