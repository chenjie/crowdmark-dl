# crowdmark-dl
Command-line program to download assignments and exam results from Crowdmark, an Online Grading Software

## Install Dependencies

### conda
```
conda install --file requirements.txt
```

### pip3
```
pip3 install -r requirements.txt
```

## Usage
TBA

## Collaborators

| Name                    | GitHub                                     | Email
| ----------------------- | ------------------------------------------ | -------------------------
| Chenjie (Jack) Ni       | [jellycsc](https://github.com/jellycsc)    | nichenjie2013@gmail.com
| Runqi (KiKi) Bi         | [kiki1415926](https://github.com/kiki1415926)    | runqi.bi@mail.utoronto.ca

## Initial Example (*subject to change*)
```
$ python cm-dl.py 
**The following id's are part of the cookies, which is used for authentication purpose only.**
cm_session_id: <actual_cm_session_id>
cm_uuid: <actual_cm_uuid>
Output directory: /Users/jackni/Desktop/19sum/cm-dl

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

Please enter an index to select an assessment: 2
Title: Midterm Exam II
[1/10] Downloading ... OK
[2/10] Downloading ... OK
[3/10] Downloading ... OK
[4/10] Downloading ... OK
[5/10] Downloading ... OK
[6/10] Downloading ... OK
[7/10] Downloading ... OK
[8/10] Downloading ... OK
[9/10] Downloading ... OK
[10/10] Downloading ... OK
Title: Midterm Exam I
[1/10] Downloading ... OK
[2/10] Downloading ... OK
[3/10] Downloading ... OK
[4/10] Downloading ... OK
[5/10] Downloading ... OK
[6/10] Downloading ... OK
[7/10] Downloading ... OK
[8/10] Downloading ... OK
[9/10] Downloading ... OK
[10/10] Downloading ... OK

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

## Result (jpeg img)
![example-img](https://user-images.githubusercontent.com/25379724/58531651-11d6e000-81b1-11e9-98fc-1a468950bc81.jpeg)

## License
[MIT](LICENSE)
