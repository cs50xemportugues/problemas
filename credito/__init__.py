import check50
import check50.c

@check50.check()
def existe():
    """credito.c existe"""
    check50.exists("credito.c")

@check50.check(existe)
def compila():
    """credito.c compila"""
    check50.c.compile("credito.c", lcs50=True)

@check50.check(compila)
def teste1():
    """identifica 378282246310005 como AMEX"""
    check50.run("./credito").stdin("378282246310005").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste2():
    """identifica 371449635398431 como AMEX"""
    check50.run("./credito").stdin("371449635398431").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste3():
    """identifica 5555555555554444 como MASTERCARD"""
    check50.run("./credito").stdin("5555555555554444").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste4():
    """identifica 5105105105105100 como MASTERCARD"""
    check50.run("./credito").stdin("5105105105105100").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste5():
    """identifica 4111111111111111 como VISA"""
    check50.run("./credito").stdin("4111111111111111").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste6():
    """identifica 4012888888881881 como VISA"""
    check50.run("./credito").stdin("4012888888881881").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste7():
    """identifica 4222222222222 como VISA"""
    check50.run("./credito").stdin("4222222222222").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste8():
    """identifica 1234567890 como INVÁLIDO"""
    check50.run("./credito").stdin("1234567890").stdout("INVÁLIDO\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste9():
    """identifica 369421438430814 como INVÁLIDO"""
    check50.run("./credito").stdin("369421438430814").stdout("INVÁLIDO\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste10():
    """identifica 4062901840 como INVÁLIDO"""
    check50.run("./credito").stdin("4062901840").stdout("INVÁLIDO\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste11():
    """identifica 5673598276138003 como INVÁLIDO"""
    check50.run("./credito").stdin("5673598276138003").stdout("INVÁLIDO\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste12():
    """identifica 4111111111111113 como INVÁLIDO"""
    check50.run("./credito").stdin("4111111111111113").stdout("INVÁLIDO\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def teste13():
    """identifica 4222222222223 como INVÁLIDO"""
    check50.run("./credito").stdin("4222222222223").stdout("INVÁLIDO\n").stdout(check50.EOF).exit(0)
