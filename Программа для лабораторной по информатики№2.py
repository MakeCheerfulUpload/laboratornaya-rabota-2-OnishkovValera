sinds=["000", "001", "010", "011", "100", "101", "110", "111"]
err=["нет ошибки", "r3", "r2", "i3", "r1", "i2", "i1", "i4"]
enum=["r1", "r2", "i1", "r3", "i2", "i3", "i4"]


number=input()
elements=list(str(number))
if (number.isdigit() == False) or(int(number) >= 10000000) or (int(number) < 1000000) or ("2" in elements) or ("3" in elements) or ("4" in elements) or ("5" in elements) or ("6" in elements) or ("7" in elements) or ("8" in elements) or ("9" in elements):
    print("Ошибка")
else:
    s1=(int(elements[0])+int(elements[2])+int(elements[4])+int(elements[6]))%2
    s2=(int(elements[1])+int(elements[2])+int(elements[5])+int(elements[6]))%2
    s3=(int(elements[3])+int(elements[4])+int(elements[5])+int(elements[6]))%2
    S=str(s1*100+s2*10+s3)
    if len(S)==2:
        S="0"+S
    if len(S)==1:
        S="00"+S

    Ps=sinds.index(S)
    if Ps!=0:
        Osh=enum.index(err[Ps])

        if str(elements[Osh])=="0":
            elements[Osh]="1"
        else:
            elements[Osh]="0"
        correct= int(elements[2]) * 1000 + int(elements[4]) * 100 + int(elements[5]) * 10 + int(elements[6])
        print(correct, err[Ps])
    else:
        print("Ошибок нет")
