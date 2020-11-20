nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5.0:
    print('O aluno está reprovado!')
elif 5.0 <= media <= 6.9:
    print('O aluno está de recuperação!')
else:
    print('Aprovado!!')
