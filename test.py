from vector import Vector2D

testCount = 0
testSuccess = 0

def testVector2D():
    v1 = Vector2D(2, 3)
    v2 = Vector2D(5, 7)

    testInteger(v1.x, 2)
    testInteger(v1.y, 3)
    testInteger(v2.x, 5)
    testInteger(v2.y, 7)

    v1 += v2

    testInteger(v1.x, 7)
    testInteger(v1.y, 10)

    v3 = Vector2D(6, 9)

    v3 -= v2

    testInteger(v3.x, 1)
    testInteger(v3.y, 2)

    v3 *= 8

    testInteger(v3.x, 8)
    testInteger(v3.y, 16)

def testString(a:str, b:str) -> None:
    global testCount
    global testSuccess
    testCount += 1
    if a == b:
        testSuccess += 1
        print(f"SUCCESS \tTest passed!")
    else:
        print(f"FAILED \t'{a}' differs from '{b}'")

def testInteger(a:int, b:int) -> None:
    global testCount
    global testSuccess
    testCount += 1
    if a == b:
        testSuccess += 1
        print(f"SUCCESS \tTest passed!")
    else:
        print(f"ERROR \t{str(a)} differs from {str(b)}")

def testID(a:object, b:object) -> None:
    global testCount
    global testSuccess
    testCount += 1
    if id(a) == id(b):
        testSuccess += 1
        print(f"SUCCESS \tTest passed!")
    else:
        print(f"FAILED \t{str(a)} differs from {str(b)}")

# def testSingleton():
#     TheGame().init()
#     s1 = TheGame()
#     s2 = TheGame()
#     s3 = TheGame()

#     testID(s1, s2)
#     testID(s1, s3)
#     testID(s3.surface, TheGame().surface)

if __name__ == "__main__":
    testVector2D()
    # testSingleton()
    print(f"{str(testSuccess)} out of {str(testCount)} Test(s) succeded")
    print(type(testVector2D))
