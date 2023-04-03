class lab03:
    def pwrSet(self,L):
        n = len(L)
        if n == 0:
            return[[]]
        else :
            base = self.pwrSet(L[:-1])
            print('\n pre-recursive, L= ', L)
            operator = L[-1:]
            print("operator:",operator)
            print("base:",base)
            print("\n post-recursive, L= ",base + [(b+operator) for b in base])
            return base + [(b+operator) for b in base]
        
#main
a = lab03()
a.pwrSet([1,2,3,4,5])