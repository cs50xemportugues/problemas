import check50
import check50.c


@check50.check()
def existe():
    """dinheiro.c existe"""
    check50.exists("dinheiro.c")


@check50.check(existe)
def compila():
    """dinheiro.c compila"""
    check50.c.compile("dinheiro.c", lcs50=True)


@check50.check(compila)
def teste041():
    """uma entrada de dados igual a 0.41 produz uma saída de dados igual a 4"""
    check50.run("./dinheiro").stdin("0.41").stdout(moedas(4), "4\n").exit(0)


@check50.check(compila)
def teste001():
    """uma entrada de dados igual a 0.01 produz uma saída de dados igual a 1"""
    check50.run("./dinheiro").stdin("0.01").stdout(moedas(1), "1\n").exit(0)


@check50.check(compila)
def teste015():
    """uma entrada de dados igual a 0.15 produz uma saída de dados igual a 2"""
    check50.run("./dinheiro").stdin("0.15").stdout(moedas(2), "2\n").exit(0)


@check50.check(compila)
def teste160():
    """uma entrada de dados igual a 1.6 produz uma saída de dados igual a 7"""
    check50.run("./dinheiro").stdin("1.6").stdout(moedas(7), "7\n").exit(0)


@check50.check(compila)
def teste230():
    """uma entrada de dados igual a 23 produz uma saída de dados igual a 92"""
    check50.run("./dinheiro").stdin("23").stdout(moedas(92), "92\n").exit(0)


@check50.check(compila)
def teste420():
    """uma entrada de dados igual a 4.2 produz uma saída de dados igual a 18"""
    from re import search
    expected = "18\n"
    actual = check50.run("./dinheiro").stdin("4.2").stdout()
    if not search(moedas(18), actual):
        help = None
        if search(moedas(22), actual):
            help = "você esqueceu de arredondar sua entrada de dados para o centavo mais próximo?"
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(compila)
def teste_rejeita_negativo():
    """rejeita uma entrada de dados negativa igual a -1"""
    check50.run("./dinheiro").stdin("-1").reject()


@check50.check(compila)
def teste_rejeita_foo():
    """rejeita uma entrada de dados não numérica igual a "foo" """
    check50.run("./dinheiro").stdin("foo").reject()


@check50.check(compila)
def teste_rejeita_vazio():
    """rejeita uma entrada de dados não-numérica igual a "" """
    check50.run("./dinheiro").stdin("").reject()


def moedas(num):
    # expressão regular que checa se `num` não está envolvido por outros números (dessa maneira moedas(2) não vai equivaler a, por exemplo, 123)

    # regex that matches `num` not surrounded by any other numbers (so moedas(2) won't match e.g. 123)

    return fr"(?<!\d){num}(?!\d)"
