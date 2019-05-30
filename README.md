# crowdmark-dl

📝Command-line program to download assignments and exam results from Crowdmark (an Online Grading Software)

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

## Initial Demo (*subject to change*)

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

## Example Results

![example-dir1](https://user-images.githubusercontent.com/25379724/58580262-ade90180-821a-11e9-8c84-da5cc991cc79.png)
![example-dir2](https://user-images.githubusercontent.com/25379724/58580260-ade90180-821a-11e9-9752-01a9880801c9.png)
![example-dir3](https://user-images.githubusercontent.com/25379724/58580259-ade90180-821a-11e9-8220-e0e9afa7e7f6.png)
![example-pdf](https://user-images.githubusercontent.com/25379724/58580258-ad506b00-821a-11e9-9460-4f4e12bb58c5.png)
![example-img](https://user-images.githubusercontent.com/25379724/58531651-11d6e000-81b1-11e9-98fc-1a468950bc81.jpeg)

## License
[MIT](LICENSE)
