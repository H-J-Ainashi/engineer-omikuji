import random
def dic():
    mikuji = [['大吉','中吉','吉','小吉','末吉','凶'],
    ['python','C','C++','C+','C#','HTML','CSS','R','Go','PHP','java','Ruby','Swift','JS','Kotlin'],
    ['広い視野をもて','すぐに解決する','一度時間を置け','とにかく調べよ','誤字に気をつけよ','ひとまず落ち着け'],
    ['椅子を買うべし','キーボードを買うべし','モニターを買うべし','macを買うべし','そのままで良い'],
    ['積ん読を消費すべし','気になったものを買うべし','迷ったら買うべし'],
    ['Atcoderを続けるべし','英語の音読を続けるべし','タイピング練習を続けるべし','必ずコードを読むべし','githubを触るべし']]

    ans=[]
    for i in mikuji:
        ans.append(random.choice(i))

    return ans


#dic()
