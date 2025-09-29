#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    C = [s[0]]
    O = [1]
    for i in range(1,len(s)):
        if s[i] == C[-1]:
            O[-1] += 1
        else:
            C.append(s[i])
            O.append(1)
    
    return  list(zip(C,O))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [(s[0],1)]
    # recherche nombre de caractères identiques au premier
    for i in range(1,len(s)):
        if s[i] != s[0]:
            return [(s[0],i)] + artcode_r(s[i:])
    # Si on sort de la boucle, tous les caractères sont identiques
    return [(s[0], len(s))]
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
