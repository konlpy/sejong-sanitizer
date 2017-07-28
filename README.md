# Sejong sanitizer

This is a simple sanitizer for morpheme data in the Sejong Corpus.

Sejong Corpus became available to the public thanks to a 10-year long project by the Korean government (1997-2007).
Despite the small size of the data, it is still one of the most widely used datasets for Korean natural language processing, due to the lack of open resources.

This repository aims to "sanitize" the XML-formatted data into a more developer-friendly format -- disregarding sentence splits, and leaving one word and its morpheme-splitted output in one line, delimited with a tab. (Examples of input/output file formats below.)
You can use `sanitizer.py` to sanitize the data for yourself, <s>or otherwise directly download and use the sanitized results from the `./output` directory.</s>
(Data was removed from the repo due to Sejong Corpus's CC BY-NC-ND 4.0 license.)

## Requirements

- python2
- `pip install lxml`

## Morpheme corpus

### Data acquisition

- If you have the Sejong corpus CD: `cd1/02_말뭉치/현대/{구어, 문어}/현대{구어, 문어}_말뭉치/형태분석_말뭉치`
- If you don't have the Sejong corpus CD:
    - Go to https://ithub.korean.go.kr/user/total/referenceManager.do
    - Search for `형태분석 말뭉치`
    - Download `{구어, 문어}_형태분석_말뭉치.zip` (You will need to login first)

### Sanitize

Input
(Yes, the encoding is utf-16):

    $ iconv -f utf-16 -t utf-8 ./sejong/cd1/02_말뭉치/현대/구어/현대구어_말뭉치/형태분석_말뭉치/5CT_0013.txt | sed -n 115,143p
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
    5CT_0013-0000200        <s n="00005">
    5CT_0013-0000210        아침에  아침/NNG+에/JKB
    5CT_0013-0000220        몇      몇/MM
    5CT_0013-0000230        시에    시/NNB+에/JKB
    5CT_0013-0000240        타고    타/VV+고/EC
    5CT_0013-0000250        가는데? 가/VV+는데/EF+?/SF
    5CT_0013-0000260        </s>
    5CT_0013-0000270        </u>

Script:

    $ python sanitizer.py

Output(s):

    $ head ./output/colloquial_word_to_morph.txt
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

    $ head ./output/colloquial_word_to_morphpos.txt
    뭐      뭐/NP
    타고    타/VV 고/EC
    가?     가/VV ㅏ/EF ?/SF
    지하철. 지하철/NNG ./SF
    기차?   기차/NNG ?/SF
    아침에  아침/NNG 에/JKB
    몇      몇/MM
    시에    시/NNB 에/JKB
    타고    타/VV 고/EC
    가는데? 가/VV 는데/EF ?/SF

## Simple statistics

    # Number of words
    $ wc -l ./output/*.txt
      747729 ./output/colloquial_word_to_morph.txt
      747729 ./output/colloquial_word_to_morphpos.txt
     5815619 ./output/written_word_to_morph.txt
     5815619 ./output/written_word_to_morphpos.txt
     13126696 total

    # Number of word types
    $ cut -f1 ./output/colloquial_word_to_morph.txt | sort -u | wc -l
    136908

    # Number of characters (including spaces)
    $ cut -f1 ./output/colloquial_word_to_morph.txt | sed 's/\(.\)/\1 /g' | tr ' ' '\n' | wc -l
    2844345

    # Number of character types
    $ cut -f1 ./output/colloquial_word_to_morph.txt | sed 's/\(.\)/\1 /g' | tr ' ' '\n' | sort -u | wc -l
    1709

# License

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
</p>

(Note that the licence for the original Sejong Corpus is [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ko).
