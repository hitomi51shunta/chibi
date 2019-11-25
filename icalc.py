import pegpy

peg = pegpy.grammar("""
Expression=Product(^{’+’Product#Add})*
Product=Value(^{’*’Value#Mul})*
Value={[0-9]+#Int}
""")

parser = pegpy.generate(peg)

def calc(t):
    if t.tag == ’Int’:
        return int(str(t))
    elif t.tag == ’Add’:
        return calc(t[0]) + calc(t[1])
    elif t.tag == ’Mul’:
        return calc(t[0]) * calc(t[1])
    else:
        print(f’TODO {t.tag})’
        return 0
        
t=parser(’1+2*3+4*5’)
print(calc(t))