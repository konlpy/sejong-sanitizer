# Sejong sanitizer

This is a simple sanitizer for the Sejong Corpus.

## Requirements

- python2
- `pip install lxml`

## Morpheme corpus for modern spoken language

### Data acquisition

- If you have the Sejong corpus CD: `cd1/02_말뭉치/현대/구어/현대구어_말뭉치/형태분석_말뭉치`
- If you don't have the Sejong corpus CD:
    - Go to https://ithub.korean.go.kr/user/total/referenceManager.do
    - Search for "현대구어 - 형태분석 말뭉치"
    - Download "현대구어_형태분석_말뭉치.zip" (You will need to login first)

### Sanitize

Input:

    # Data sample
    $ cd ./sejong/cd1/02_말뭉치/현대/구어/현대구어_말뭉치/형태분석_말뭉치
    $ iconv -f utf-16 -t utf-8 5CT_0013.txt | sed -n 115,135p
    </teiHeader>
    <text>
    5CT_0013-0000010        <u who="P1">
    5CT_0013-0000020        <s n="00001">
    5CT_0013-0000030        뭐      뭐/NP
    5CT_0013-0000040        타고    타/VV+고/EC
    5CT_0013-0000050        가?     가/VV+ㅏ/EF+?/SF
    5CT_0013-0000060        </s>
    5CT_0013-0000070        <s n="00002">
    5CT_0013-0000080        <vocal desc="웃음"/>
    5CT_0013-0000090        </s>
    5CT_0013-0000100        </u>
    5CT_0013-0000110        <u who="P2">
    5CT_0013-0000120        <s n="00003">
    5CT_0013-0000130        지하철. 지하철/NNG+./SF
    5CT_0013-0000140        </s>
    5CT_0013-0000150        </u>
    5CT_0013-0000160        <u who="P1">
    5CT_0013-0000170        <s n="00004">
    5CT_0013-0000180        기차?   기차/NNG+?/SF
    5CT_0013-0000190        </s>

    # Number of input files
    $ ls | wc -l
    200

Execute script:

    $ python sanitizer.py

Output:

    # Data sample
    $ head word_to_morph.txt
    뭐      뭐
    타고    타 고
    가?     가 ㅏ ?
    지하철. 지하철 .
    기차?   기차 ?
    아침에  아침 에
    몇      몇
    시에    시 에
    타고    타 고
    가는데? 가 는데 ?

## Simple statistics

    # Number of words
    $ wc -l word_to_morph.txt
    747729

    # Number of word types
    $ cut -f1 word_to_morph.txt | sort -u | wc -l
    136908

    # Number of characters (including spaces)
    $ cut -f1 word_to_morph.txt | sed 's/\(.\)/\1 /g' | tr ' ' '\n' | wc -l
    2844345

    # Number of character types
    $ cut -f1 word_to_morph.txt | sed 's/\(.\)/\1 /g' | tr ' ' '\n' | sort -u | wc -l
    1709
