# -------------
# -- Numbers --
# -------------
#intger

print(type(0))
print(type(831))
print(type(-831))


#float

print(type(0.5))
print(type(113.35))
print(type(-124.354))


#complex

cmplx = 7 + 4j
print(type(cmplx))
print(f"real part : {cmplx.real} and the imaginary part : {cmplx.imag}")

# [1] you can convert from int to float or complex
# [2] you can convert form float to int or comlpex
# [3] you can't convert complex to any type

x = 100
print(float(x))
print(complex(x))

y = 100.69
print(int(y))
print(complex(y))

c = 5 + 7j
#print(int(c)) #error
print(int(c.real))
print(float(c.imag))


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

print(100 / 20) #5.0
print(int(110/20)) #5
print(110 // 20) #5

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

print(x)

