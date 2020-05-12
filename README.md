# intercoder-agreement-calculation

<a name="ex"></a>
## Examples

<a name="1"></a>
### 1. calculate cohen's kappa
usage:
```console
$ python3 cohen_kappa.py <data-file>
```
```console
$ python3 cohen_kappa.py ./data/data0.csv
Cohen's Kappa: 0.6899266046058918
```


<a name="2"></a>
### 2. calculate weighted kappa
usage:
```console
python3 weighted_kappa.py [-h] <data-file> <weights-file>
```   
```console
$ python3 weighted_kappa.py ./data/data1.csv ./data/weights1.txt
Weighted Kappa: 0.7490712511745773
```

```console
$ python3 weighted_kappa.py ./data/data2.csv ./data/weights2.txt
Weighted Kappa: 0.2902183212395829
```

<a name="3"></a>
### 3. calculate kappa with multiple labels
usage:
```console
python3 multilabel_kappa.py [-h] <data-file>
``` 
```console
$ python3 multilabel_kappa.py ./data/data3.csv
Weighted Kappa: 0.7234810951760119
```

### 4. calculate Krippendorff's alpha
usage:
```console
python3 krippendorff_alpha.py [-h] [-w WEIGHTS] {nominal,ordinal} data
```            
```console
$ python3 krippendorff_alpha.py nominal ./data/data1.csv 
Krippendorff's alpha for nominal metric: 0.6722775059943613
```
```console
$ python3 krippendorff_alpha.py ordinal ./data/data2.csv -w ./data/weights2.txt
Krippendorff's alpha for ordinal metric: 0.3136278980049674
```

### 5. calculate percentage agreement
usage:
```console
percentage_agreement.py [-h] {weighted,unweighted} data weights
```                                                                                                  
```console
$ python3 percentage_agreement.py unweighted ./data/data1.csv ./data/weights1.txt
Percentage Agreement: 0.8070866141732284
```
```console
$ python3 percentage_agreement.py unweighted ./data/data2.csv ./data/weights2.txt 
Percentage Agreement: 0.39
```
```console
$ python3 percentage_agreement.py weighted ./data/data1.csv ./data/weights1.txt
Weighted Percentage Agreement: 0.9247594050743658
```
```console
$ python3 percentage_agreement.py weighted ./data/data2.csv ./data/weights2.txt
Weighted Percentage Agreement: 0.72
```
### 6. calculate Scott's Pi
usage:
```console
scott_pi.py [-h] {weighted,unweighted} data weights
```
```console
$ python3 scott_pi.py unweighted ./data/data1.csv ./data/weights1.txt 
Scott's Pi: 0.6720623237921253
```
```console
$ python3 scott_pi.py unweighted ./data/data2.csv ./data/weights2.txt
Scott's Pi: 0.21741884529188435
```
```console
$ python3 scott_pi.py weighted ./data/data1.csv ./data/weights1.txt
Weighted Scott's Pi: 0.7495375634891724
```
```console
$ python3 scott_pi.py weighted ./data/data2.csv ./data/weights2.txt
Weighted Scott's Pi: 0.2894020984844277
```
