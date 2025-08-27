from file_opp_fortest import read_storage
from file_opp_fortest import write_storage

#test code for read_storage function
print(read_storage())

t = ["gfuhgwdkhw",
"hdilwgdoiwdg",
"lcbjLKHDHV",
"LJCBDHVCKJH"]
f = read_storage()


def read_test(t,f):
    for i in f:
        if i in t:
            print(f"success : of storage : {i} = of test : {t[f.index(i)]}")
        else:
            print(f"failed : {i} =not {t[f.index(i)]}")


print(read_storage("sub"))

t = ["abcd",
"ABCD",
"EFGH",
"ijkl"]
f = read_storage("sub")
for i in f:
    if i in t:
        print(f"success : of storage : {i} = of test : {t[f.index(i)]}")
    else:
        print(f"failed : {i} =not {t[f.index(i)]}")


# test of write_storage function

t = ['hi line1','hi line2','hi line3']

write_storage(t)
f = read_storage()
read_test(t,f)

