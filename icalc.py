import pegpy

peg = pegpy.grammar("""
Expression=Product(^{’+’Product#Add})*
Product=Value(^{’*’Value#Mul})*
Value={[0-9]+#Int}
""")

parser = pegpy.generate(peg)

def calc(t):
    if t == ’Int’:
        return int(str(t))
    elif t == ’Add’:
        return calc(t[0]) + calc(t[1])
    elif t == ’Mul’:
        return calc(t[0]) * calc(t[1])
    else:
        print(f’TODO {t.tag})’
        return 0
        
def main():
    s = input('$ ')
    t = parser(s)
    print(calc(t))

