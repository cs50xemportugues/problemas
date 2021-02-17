import check50
import check50.c

@check50.check()
def existe():
    """ola.c existe"""
    check50.existe("ola.c")

@check50.check(existe)
def compila():
    """ola.c compila"""
    check50.c.compile("ola.c", lcs50=True)

@check50.check(compila)
def ramon():
    """responde ao nome Ramon"""
    check50.run("./ola").stdin("Ramon").stdout("Ramon").exit()

@check50.check(compila)
def david():
    """responde ao nome David"""
    check50.run("./ola").stdin("David").stdout("David").exit()