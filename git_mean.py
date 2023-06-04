def mean(kor, math, eng, sci, code):
    mean = (kor+math+eng+sci+code)/5
    return round(mean, 1)

kor = int(input('국어 성적: '))
math = int(input('수학 성적: '))
eng = int(input('영어 성적: '))
sci = int(input('과학 성적: '))
code = int(input('코딩 성적: '))

print(mean(kor, math, eng, sci, code))
