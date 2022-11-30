# Créer une base, s'y connecter et créer un curseur sur la connection pour du sql.

import sqlite3
MABASE = "mabase.db"
MONSCRIPT = "monscript.sql"
connector = sqlite3.connect(MABASE)
cursor = connector.cursor()


# Import d'un script sql externe :
script = ""
with open(MONSCRIPT) as script_file :
    script = script_file.read()

# execution du cript : cursor.executescript(script) 
#    != cursor.execute (1 instruction)
#    connector.commit() pour réaliser la transaction avec la base
#    fetchall pour afficher tous les résultats
try :
    cursor.executescript(script)
    connector.commit()
    cursor.fetchall()
except Exception as exc :
    print(exc)

# SELECT : exemple ; attention CONCAT s'écrit ||


requetes = {
    "ex 8.1" : "SELECT nom || ' ' || prenom AS personne FROM employes ORDER BY personne ASC ;", # Attention : CONCAT s'écrit ||
    "ex 8.2" : "SELECT AVG(salaire) FROM employes ;",
    "ex 8.3" : "SELECT AVG(salaire) FROM employes WHERE sexe='M' ;",
    "ex 8.4" : "SELECT AVG(salaire) FROM employes WHERE sexe='F' ;",
    "ex 8.5" : "SELECT COUNT(DISTINCT superviseur_id) FROM employes ;",
    "ex 9.1" : "SELECT DISTINCT e.nom,e.prenom,s.ville FROM employes AS e, succursales AS s ;",
    "ex 9.4" : "SELECT DISTINCT e1.nom,e2.prenom,s.ville FROM employes AS e1, employes AS e2, succursales AS s ;",
    "ex 10"  : "SELECT DISTINCT e.prenom FROM employes AS e WHERE UPPER(e.nom) LIKE '%B%_' ;",
    "ex 11"  : "SELECT employes.nom, fournisseurs.fournisseur FROM employes JOIN succursales ON employes.employe_id = succursales.manager_id JOIN fournisseurs ON succursales.succursale_id = fournisseurs.succursale_id ;",
    "tables" : "SELECT name FROM sqlite_master ;",
    }

def demo(requetes:dict=requetes, connector=connector, cursor=cursor) :
    for ex, req in requetes.items() :
        print(f"\nREQUETE {ex} :\n{50*'-'}")
        print(f"mysqlite3> {req}")
        input()
        print(cursor.execute(req).fetchall())



def prompt(cursor=cursor, connector=connector) :
    req = ""
    while req != "exit" :
        req = input("mysqlite3> ")
        try :
            print(cursor.execute(req).fetchall())
        except Exception as exc :
            print(exc)


if __name__ == "__main__":
    print("demo() ou prompt() ?")
    pass


