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
CM Email: <UTORid Removed>@mail.utoronto.ca
CM Password: 
Email and password have been verified.

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

Please enter an index to select a course (type 'q' to quit): 3
All tests & assignments of the course linear-algebra-ii-all-sections:
[0] consent-form
[1] writing-assignment-8-b39bc
[2] writing-assignment-7-3aac4
[3] writing-assignment-6-5050a
[4] writing-assignment-5-2322f
[5] writing-assignment-4-8a9ae
[6] writing-assignment-3-d17e7
[7] writing-assignment-2-4a02c
[8] writing-assignment-1-641d9
[9] final-exam-000af
[10] midterm-exam-ii-d2022
[11] midterm-exam-i-aab0b
[12] all

Please enter an index to select an assessment: 10
Title: Midterm Exam II
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:01<00:00,  5.14it/s]

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

Please enter an index to select a course (type 'q' to quit): 1
All tests & assignments of the course 2019-winter-mat344h1-s-lec0101-20191-introduction-to-combinatorics-mat344h1-s-lec0101-20191-mat344h1-s-lec0102-20191:
[0] mat-344-ps-10
[1] mat-344-ps9
[2] mat-344-ps8
[3] mat-344-ps-7
[4] mat-344-ps6
[5] mat-344-ps-5
[6] mat-344-ps4
[7] mat-344-ps3
[8] mat-344-ps2
[9] mat-344-ps-1
[10] mat-344-final
[11] midterm-4370b
[12] all

Please enter an index to select an assessment: 12
Title: MAT 344 PS 10
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.52it/s]

Title: MAT 344 PS9
Downloading ... 
100%|████████████████████████████████████████████████████████████████████████████████████████████████| 12/12 [00:04<00:00,  2.75it/s]

Title: MAT 344 PS8
Downloading ... 
100%|████████████████████████████████████████████████████████████████████████████████████████████████| 11/11 [00:02<00:00,  5.25it/s]

Title: MAT 344 PS 7
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:01<00:00,  7.74it/s]

Title: MAT 344 PS6
Downloading ... 
100%|████████████████████████████████████████████████████████████████████████████████████████████████| 13/13 [00:02<00:00,  7.17it/s]

Title: MAT 344 PS 5
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:04<00:00,  2.09it/s]

Title: MAT 344 PS4
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:01<00:00,  6.28it/s]

Title: MAT 344 PS3
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:05<00:00,  1.78it/s]

Title: MAT 344 PS2
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:02<00:00,  3.00it/s]

Title: MAT 344 PS 1
Downloading ... 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00,  7.35it/s]

Title: MAT 344 Final
Downloading ... 
100%|████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:01<00:00,  6.00it/s]

Title: Midterm
Downloading ... 
100%|████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:01<00:00,  7.45it/s]

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

Please enter an index to select a course (type 'q' to quit): q
Bye.
```

## Example Results

![example-dir1](https://user-images.githubusercontent.com/25379724/58580262-ade90180-821a-11e9-8c84-da5cc991cc79.png)
![example-dir2](https://user-images.githubusercontent.com/25379724/58580260-ade90180-821a-11e9-9752-01a9880801c9.png)
![example-dir3](https://user-images.githubusercontent.com/25379724/58580259-ade90180-821a-11e9-8220-e0e9afa7e7f6.png)
![example-pdf](https://user-images.githubusercontent.com/25379724/58580258-ad506b00-821a-11e9-9460-4f4e12bb58c5.png)
![example-img](https://user-images.githubusercontent.com/25379724/58531651-11d6e000-81b1-11e9-98fc-1a468950bc81.jpeg)

## License
[MIT](LICENSE)
