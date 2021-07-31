def make_division_by(x):
    def division(n: int):
        assert(n)!=0, "you cant divide by zero"
        return n/x
    return division

def run():
    divideby3 = make_division_by(3)
    divideby2 = make_division_by(2)

    print(divideby3(12))
    print(divideby2(12))

if __name__=="__main__":
    run()
