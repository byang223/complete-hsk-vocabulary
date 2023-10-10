# Complete HSK Vocabulary

This project is an attempt to provide complete vocabulary lists for the HSK tests (Hanyu Shuiping Kaoshi - 汉语水平考试), both the previous version (2.0) and the newer one (3.0).

The data is presented in different files. 

The main, `complete.json` features ALL words appearing in any level, either of the HSK 2.0 tests or the HSK 3.0 ones - thus, it's the complete list.

Each entry includes different types of information:

### Example
```json
{
    "simplified":"爱好",
    "level":[
        "new-1",
        "old-3"
    ],
    "forms":[
        {
            "traditional":"愛好",
            "meaning":[
                "to like; to be fond of; to take pleasure in; to be keen on",
                "interest; hobby"
            ],
            "transcriptions":{
                "pinyin":"ài hào",
                "numeric":"ai4 hao4",
                "bopomofo":"ㄞˋ ㄏㄠˋ",
                "romatzyh":"ay haw"
            },
            "classifiers":[
                "个"
            ]
        }
    ],
    "frequency":4902
}
```

- **simplified:** [abbr: *s*] corresponds to the main word/entry in Simplified Chinese characters (简化字)
- **level:** [abbr: *l*] includes information about the HSK levels in which the word in question appears (in the above example, it's new HSK 1, and the old HSK 3)
- **forms:** [abbr: *f*] the different "forms" of the word
    - **traditional:** [abbr: *t*] corresponds to the main word in Traditional Chinese characters (正體字)
    - **meaning:** [abbr: *m*] a list of dictionary definitions for the current words
    - **transcriptions:** [abbr: *i*] different transliterations/transcriptions
        - **pinyin:** [abbr: *p*] the [Hanyu Pinyin](https://en.wikipedia.org/wiki/Pinyin) (汉语拼音) romanization with tone marks
        - **numeric:** [abbr: *n*] same as above, only with numeric notation for the tones
        - **bopomofo:** [abbr: *b*] transliteration of the word in [Bopomofo/Zhuyin](https://en.wikipedia.org/wiki/Bopomofo) (注音)
        - **romatzyh:** [abbr: *g*] transliteration of the word in [Gwoyeu Romatzyh](https://en.wikipedia.org/wiki/Gwoyeu_Romatzyh) (国语罗马字)
    - **classifiers:** [abbr: *c*] the list of [measure words](https://en.wikipedia.org/wiki/Chinese_classifier) (classifiers) associated with the word form in question
- **frequency:** [abbr: *q*] the word's relative "frequency" ranking (the lower this number, the more common the word)

-----

ℹ️ The exact same date exists in the minified/compressed `complete.min.json`, only without pretty-printing and with the above abbreviations used instead of the full field names.
