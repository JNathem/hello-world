Test = ["Test1","Test2","Test3"]

Vari = Test[0]

Test[0]="Test_neu"

print(Vari)
print(Test[0])

for i in range(0,len(Test)):
    print(Test[i])

Test[0] = "Test1"

for i in range(0,len(Test)):
    print(Test[i])

print(Test)

Test.append("Test4")

print(Test)

Test.insert(1,"Test5")

print(Test)
