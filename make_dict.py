#coding:utf-8
# import trans
import csv,os,re,MeCab
import ctrans

# check word composed by only numbers
def check_word(str):
    alldigit = re.compile(ur"^[0-9]+$")
    if alldigit.search(str) != None:
        return False
    return True


re_hiragana = re.compile(ur'[ぁ-ゔ]')
def hiragana2katakana(text):
    return re_hiragana.sub(lambda x: unichr(ord(x.group(0)) + 0x60), text)


f = open('./dict.csv', 'ab')
csvWriter = csv.writer(f)
list = []
count = 0

m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
for word in open(os.environ['HOME'] + '/Downloads/jawiki-latest-all-titles-in-ns0', 'r'):
    list = []
    # word check
    word = word.rstrip()
    word = re.sub(re.compile("[!-/:-@[-`{-~]"),"", word)

    # dictionary check
    count = 0
    for chunk in m.parse(word).splitlines()[:-1]:
        count +=1
    print word
    word = word.decode('utf-8')
    if count == 1:
        print 'This word has been already registered.'
    elif len(word) >= 2 and check_word(word):
        try:
            # get 'yomigana'
            kana = ctrans.wrap_yomi(word)

            # translate hiragana to katakana
            kana = hiragana2katakana(kana)
            list.append( word.encode('utf-8') )
            list.extend(['*','*','*',u'名詞'.encode('utf-8'),'*','*','*','*','*','*'])
            list.append(kana.encode('utf-8'))
            list.append('*')
            csvWriter.writerow(list)
        except UnicodeDecodeError:
            print 'Error word: '+word
f.close
