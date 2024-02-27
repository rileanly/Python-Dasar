def salampagi(*VarArgs):
    print("Halo")
    print("Selamat Pagi ", end= "")
    for arg in VarArgs:
        print(arg, end = " ")


salampagi("Joni", "Defan", "Dilo")


def hitungbmi(berat, tinggi):
    print("BMI: ", berat/tinggi*tinggi)


hitungbmi(50, 166)


a = 14 # variable global

def print_func():
    a = 17 #variable lokal
    print("dalam print_func a =", a)

print_func()
print("a = ", a)



a_var = 5
b_var = 10 
c_var = 15

def a_func(a_var):
    print("dalam a_func a_var =", a_var)
    b_var = 100 + a_var 
    d_var = 2 * a_var
    print("dalam a_func b_var =", b_var)
    print("dalam a_func d_var =", d_var)
    print("dalam a_func e_var =", a_var)
    return b_var + 10 

c_var = a_func(b_var)
print("c_var dalam a_func =", c_var)
print("a_var =" , a_var)
print("b_var =", b_var)
print("d_var =", d_var) #d_var tidak muncul karena d_var ada dalam fungsi a_func




