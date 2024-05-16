# -------------
# -- Numbers --
# -------------
#intger

print(type(0))       # <class 'int'>
print(type(831))     # <class 'int'>
print(type(-831))    # <class 'int'>


#float

print(type(0.5))        # <class 'float'>
print(type(113.35))     # <class 'float'>
print(type(-124.354))   # <class 'float'>


#complex

cmplx = 7 + 4j
print(type(cmplx))     # <class 'complex'>
print(f"real part : {cmplx.real} and the imaginary part : {cmplx.imag}")   # real part : 7.0 and the imaginary part : 4.0

# [1] you can convert from int to float or complex
# [2] you can convert form float to int or comlpex
# [3] you can't convert complex to any type

x = 100
print(float(x))     # 100.0
print(complex(x))   # (100+0j)

y = 100.69
print(int(y))        # 100
print(complex(y))    # (100.69+0j)

c = 5 + 7j
#print(int(c)) #error
print(int(c.real))    # 5
print(float(c.imag))  # 7.0


# --------------------------
# -- Arithmetic Operators --
# --------------------------
#addition (+)
#subtraction (-)
#multiplication (*)
#division (/)
#modulus (%)
#exponent (**)
#floor division (//)

print(100 / 20)      # 5.0
print(int(110/20))   # 5
print(110 // 20)     # 5

#---------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------

x = 10  # Var One
y = 20  # Var Two

# Var One = Self [Operator] Var Two
# Var One [Operator]= Var Two

# x += y
x -= y

print(x)    # -10

