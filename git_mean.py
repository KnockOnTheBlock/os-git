def mean(kor, math, eng):
    mean = (kor+math+eng)/3
    return round(mean, 1)

kor = int(input('국어 성적: '))
math = int(input('수학 성적: '))
eng = int(input('영어 성적: '))

print(mean(kor, math, eng))
