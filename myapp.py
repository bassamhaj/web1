def main():
    f=open("q4.html", "w+")
    upper = """<!DOCTYPE html>
<html lang="en">
<head>
    <style>
    body {
        width: 100vw;
        height: 100vh;
        display:inline-flex;
    }
    .blue {
        width: 33.3%;
        height: 100%;
        background-color: blue;
        float: left;
    }

    .red {
        width: 33.3%;
        height: 100%;
        background-color: red;
        float: right;
    }

    .green {
        width: 33.3%;
        height: 100%;
        background-color: green;
        float: right;
    }
</style>
</head>
<body>"""
    f.write(upper)
    color1 = """<div class="blue"></div>
    """
    color2 = """<div class="red"></div>
    """
    color3 = """<div class="green"></div></div>
    """
    num = int(input("enter num between 1-50 : "))
    while (num<1 or num>50):
        print("Wrong input out of range!!")
        num = int(input("enter num between 1-50 : "))

    while (num):
        num = num-1
        f.write(color1)
        if (num == 0):
            break
        num=num-1
        f.write(color2)
        if (num == 0):
            break
        num = num - 1
        f.write(color3)
        if (num == 0):
            break

    f.write('</body></html>')
    f.close();

if __name__ == "__main__":
    main()
