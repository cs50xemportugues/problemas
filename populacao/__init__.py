import check50
import check50.c

@check50.check()
def existe():
    """populacao.c existe"""
    check50.existe("populacao.c")

@check50.check(existe)
def compila():
    """populacao.c compila"""
    check50.c.compile("populacao.c", lcs50=True)

@check50.check(compila)
def start_less():
    """rejeita população inicial menor do que 9"""
    check50.run("./populacao").stdin("8").stdin("8").reject()

@check50.check(compila)
def end_less():
    """rejeita população final menor do que população inicial"""
    check50.run("./populacao").stdin("50").stdin("49").reject()

@check50.check(compila)
def decimal_truncation():
    """manipula número decimal de lhamas"""
    check50.run("./populacao").stdin("1100").stdin("1192").stdout("Anos: 2").exit(0)

@check50.check(compila)
def same_value():
    """lida com o caso de população inicial e final com mesmo valor"""
    check50.run("./populacao").stdin("100").stdin("100").stdout("Anos: 0").exit(0)

@check50.check(compila)
def test1():
    """calcula população final com população inicial igual a 1200"""
    check50.run("./populacao").stdin("1200").stdin("1300").stdout("Anos: 1").exit(0)

@check50.check(compila)
def test2():
    """rejeita valores de população inicial inválidos e em seguida aceita população inicial igual a 9"""
    check50.run("./populacao").stdin("-5").stdin("3").stdin("9").stdin("5").stdin("18").stdout("Anos: 8").exit(0)

@check50.check(compila)
def test3():
    """rejeita valores de população final inválidos e em seguida aceita população final igual a 100"""
    check50.run("./populacao").stdin("20").stdin("1").stdin("10").stdin("100").stdout("Anos: 20").exit(0)

@check50.check(compila)
def test4():
    """calcula população final a partir de população inicial igual a 100"""
    check50.run("./populacao").stdin("100").stdin("1000000").stdout("Anos: 115").exit(0)