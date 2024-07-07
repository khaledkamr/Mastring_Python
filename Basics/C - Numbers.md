# Numbers
### integer
```python []
print(type(0))        
print(type(831))      
print(type(-831))    
```
### Output
```
<class 'int'>
<class 'int'>
<class 'int'>
```

### float
```python []
print(type(0.5))         
print(type(113.35))      
print(type(-124.354))    
```
### Output
```
<class 'float'>
<class 'float'>
<class 'float'>
```

### complex
```python []
cmplx = 7 + 4j
print(type(cmplx))      
print(f"real part : {cmplx.real} and the imaginary part : {cmplx.imag}")   
```
### Output
```
<class 'complex'>
real part : 7.0 and the imaginary part : 4.0
```
you can convert from int to float or complex

you can convert form float to int or comlpex

you can't convert complex to any type
```python []
x = 100
print(float(x))     
print(complex(x))   

y = 100.69
print(int(y))        
print(complex(y))    

c = 5 + 7j
print(int(c)) 
print(int(c.real))    
print(float(c.imag))  
```
### Output
```
100.0
(100+0j)
100
(100.69+0j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
5
7.0
```

# Arithmetic Operators 
- addition (+)
- subtraction (-)
- multiplication (*)
- division (/)
- modulus (%)
- exponent (**)
- floor division (//)
```python []
print(100 / 20)      
print(int(110/20))   
print(110 // 20)     
```
### Output
```
5.0
5
5
```
# Assignment Operators 
- =
- +=
- -=
- *=
- /=
- **=
- %=
- //=
```python []
x = 10  # Var One
y = 20  # Var Two

# Syntax:
# Var One = Self [Operator] Var Two
# Var One [Operator]= Var Two

x += y

print(x)   
```
### Output
```
30
```

