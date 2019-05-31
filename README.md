# crowdmark-dl

[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

📝Command-line program to download assignments and exam results from Crowdmark (an Online Grading Software)

## [Demo PDF](https://nbviewer.jupyter.org/github/jellycsc/crowdmark-dl/blob/master/demo/winter-2016-mat223h1-s-lec0301-lec5101-lec0201-le/Midterm%20Exam%20I.pdf)

<a href="https://nbviewer.jupyter.org/github/jellycsc/crowdmark-dl/blob/master/demo/winter-2016-mat223h1-s-lec0301-lec5101-lec0201-le/Midterm%20Exam%20I.pdf"><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png" 
      width="109" height="20"></a><br>

## Prerequisites

* Python3

## Install Dependencies

* [Pillow](https://python-pillow.org/)
* [requests](https://2.python-requests.org//en/latest/)
* [tqdm](https://tqdm.github.io/)
* [arrow](https://arrow.readthedocs.io/en/latest/)

### conda

```
conda install --file requirements.txt
```

### pip3

```
pip3 install -r requirements.txt
```

## Usage (*subject to change*)

```
python3 cm-dl.py
```

## Collaborators

| Name                    | GitHub                                     | Email
| ----------------------- | ------------------------------------------ | -------------------------
| Chenjie (Jack) Ni       | [jellycsc](https://github.com/jellycsc)    | nichenjie2013@gmail.com
| Runqi (KiKi) Bi         | [kiki1415926](https://github.com/kiki1415926)    | runqi.bi@mail.utoronto.ca

## CLI Demo (*subject to change*)

```
$ python cm-dl.py
CM Email: <UTORid>@mail.utoronto.ca
CM Password: 🔑
✔ Email and password have been verified.

Output directory: download
All the courses records on Crowdmark:
[0] mat-tas-2018-2019
[1] 2019-winter-mat344h1-s-lec0101-20191-introduction-to-combinatorics-mat344h1-s-lec0101-20191-mat344h1-s-lec0102-20191
[2] stats-for-comp-sci
[3] linear-algebra-ii-all-sections
[4] microeconomic-theory-cb755
[5] intro-to-theory-comp-intro-to-theory-comp
[6] advanced-calculus-advanced-calculus
[7] prob-comp-appl
[8] winter-2016-mat223h1-s-lec0301-lec5101-lec0201-le
[9] fall-2015-mat137y1-y-tut0202-tut0201-tut5103-tut5
[10] fall-2015-eco100y1-y-lec0301

Please enter an index to select a course (type 'q' to quit): 8
All tests & assignments of the course winter-2016-mat223h1-s-lec0301-lec5101-lec0201-le:
[0] midterm-exam-ii
[1] midterm-exam-i-95db8
[2] all

Please enter an index to select an assessment: 1
Title: Midterm Exam I
Downloading ... 
100%|████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:02<00:00,  5.33it/s]
```

## Test By Eyeballing

![all-pdfs](https://user-images.githubusercontent.com/25379724/58685592-4d58e200-834a-11e9-90e5-6844e0b51563.png)

## License

[MIT](LICENSE)
