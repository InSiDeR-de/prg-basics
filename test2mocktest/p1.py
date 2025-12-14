def f(p1,p2):
    dc={"A":10,"K":10,"Q":10,"J":10,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1}
    v1=0
    v2=0
    for x in p1:
        v1+=dc[x]
    for y in p2:
        v2+=dc[y]
    if v1>=v2:
        return True
    else: return False

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))