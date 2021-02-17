import check50
import check50.c

@check50.check()
def existe():
    """mario.c existe"""
    check50.existe("mario.c")
    check50.include("1.txt", "2.txt", "8.txt")

@check50.check(existe)
def compila():
    """mario.c compila"""
    check50.c.compile("mario.c", lcs50=True)

@check50.check(compila)
def teste_reject_negative():
    """rejeita uma altura igual a -1"""
    check50.run("./mario").stdin("-1").reject()

@check50.check(compila)
def teste0():
    """rejeita uma altura igual a 0"""
    check50.run("./mario").stdin("0").reject()

@check50.check(compila)
def teste1():
    """cria uma pirâmide de altura igual a 1 corretamente"""
    out = check50.run("./mario").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(compila)
def teste2():
    """cria uma pirâmide de altura igual a 2 corretamente"""
    out = check50.run("./mario").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compila)
def teste8():
    """cria uma pirâmide de altura igual a 8 corretamente"""
    out = check50.run("./mario").stdin("8").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(compila)
def teste9():
    """rejeita uma altura igual a 9, e em seguida aceita uma altura igual a 2"""
    out = check50.run("./mario").stdin("9").reject().stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compila)
def teste_rejeita_foo():
    """rejeita uma altura não-numérica igual a "foo" """
    check50.run("./mario").stdin("foo").reject()

@check50.check(compila)
def teste_rejeita_vazio():
    """rejeita uma altura não-numérica igual a "" """
    check50.run("./mario").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "você adicionou muitos espaços do lado direito de cada linha da pirâmide?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "você está imprimindo caracteres adicionais no início de cada linha?"

    raise check50.Mismatch(correct, output, help=help)