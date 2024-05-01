mes = input('digite o número do seu mês de nascimento: ')

match mes:
    case '1':
        print('seu signo é Python')
    case '2':
        print('seu signo é Fortran')
    case '3':
        print('seu signo é Rust')
    case '4':
        print('seu signo é Go')
    case '5':
        print('seu signo é Java')
    case '6':
        print('seu signo é JavaScript')
    case '7':
        print('seu signo é C')
    case '8':
        print('seu signo é PHP')
    case '9':
        print('seu signo é Haskell')
    case '10':
        print('seu signo é Perl')
    case '11':
        print('seu signo é Swift')
    case '12':
        print('seu signo é Kotlin')
    case _:
        print('você não é um programador!')