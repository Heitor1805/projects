a=[2,2,4,5,6]
b=[]
def func(b):
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
            
func(b)
#O código irá ler uma lista e passar os elementos para outra lista, sem repetir as duplicatas