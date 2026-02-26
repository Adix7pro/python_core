import math

def yuzi_1(base, height):
    return 0.5 * base * height

def yuzi_2(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Bunday tomonlar bilan uchburchak hosil bo'lmaydi.")
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def yuzi_3(x1, y1, x2, y2, x3, y3):
    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
    return area

if __name__ == "__main__":
    print("=== Uchburchak yuzini hisoblash dasturi ===")
    print("1) Asos va balandlik orqali")
    print("2) Uchte tomon orqali)")
    print("3) Uchta nuqta koordinatasi orqali")
    
    tanlov = input("Usulni tanlang (1/2/3): ").strip()

    try:
        if tanlov == "1":
            b = float(input("Asosni kiriting: "))
            h = float(input("Balandlikni kiriting: "))
            print("Uchburchak yuzi:", yuzi_1(b, h))

        elif tanlov == "2":
            a = float(input("a tomon: "))
            b = float(input("b tomon: "))
            c = float(input("c tomon: "))
            print("Uchburchak yuzi:", yuzi_2(a, b, c))

        elif tanlov == "3":
            x1, y1 = map(float, input("1-nuqta (x1 y1): ").split())
            x2, y2 = map(float, input("2-nuqta (x2 y2): ").split())
            x3, y3 = map(float, input("3-nuqta (x3 y3): ").split())
            yuzi = yuzi_3(x1, y1, x2, y2, x3, y3)
            if yuzi == 0:
                print("Nuqtalar bir to'g'ri chiziqda bu haqiqiy uchburchak emas")
            else:
                print("Uchburchak yuzi:", yuzi)
        else:
            print("Error choice!")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("What's wrong:", e)


