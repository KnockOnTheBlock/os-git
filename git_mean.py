def mean(kor, math, eng, sci):
    mean = (kor+math+eng+sci)/4
    return round(mean, 1)

kor = int(input('국어 성적: '))
math = int(input('수학 성적: '))
eng = int(input('영어 성적: '))
sci = int(input('과학 성적: '))

print(mean(kor, math, eng, sci))
