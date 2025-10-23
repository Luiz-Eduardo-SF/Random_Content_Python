c = [   
    '\033[0;30m',
    '\033[0;31m',       
    '\033[0;32m',     
    '\033[0;33m',    
    '\033[0;34m',
    '\033[0;35m',
    '\033[0;36m',
    '\033[0;37m'
]
def colorprint(txt,num=0):
    """
    -> retorna uma cor dependendo do valor 

        0 - cinza      (gray)\n
        1 - vermelho    (red)\n       
        2 - verde       (green)\n        
        3 - amarelo     (yellow)\n        
        4 - azul        (blue)\n        
        5 - roxo        (purple)\n        
        6 - ciano       (cian)\n        
        7 - branco       (white , vscode default)\n
    """
    return print(f'{c[num]}{txt}{c[7]}')