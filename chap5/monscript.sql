CREATE TABLE employes (
  employe_id INT NOT NULL,
  prenom VARCHAR(255),
  nom VARCHAR(255),
  naissance DATE,
  sexe VARCHAR(1),
  salaire INT,
  succursale_id INT,
  superviseur_id INT,
  PRIMARY KEY (employe_id)
  FOREIGN KEY (succursale_id) REFERENCES succursales(succursale_id)
  FOREIGN KEY (superviseur_id) REFERENCES employes(employe_id)
) ;


CREATE TABLE succursales (
  succursale_id INT NOT NULL,
  ville VARCHAR(255),
  manager_id INT,
  PRIMARY KEY (succursale_id)
  FOREIGN KEY (manager_id) REFERENCES employes(employe_id)
) ;


CREATE TABLE fournisseurs (
  succursale_id INT NOT NULL,
  fournisseur VARCHAR(255) NOT NULL,
  fourniture VARCHAR(255),
  PRIMARY KEY (succursale_id, fournisseur)
  FOREIGN KEY (succursale_id) REFERENCES succursales(succursale_id)
) ;

INSERT INTO EMPLOYES (employe_id, prenom, nom, naissance, sexe, salaire, succursale_id, superviseur_id)
VALUES (100, 'Bruce', 'Salmons', '1967-04-10', 'M', 118000, 1, 100);
INSERT INTO EMPLOYES (employe_id, prenom, nom, naissance, sexe, salaire, succursale_id, superviseur_id)
VALUES (101, 'Mirabelle', 'Beauchesne', '1969-09-17', 'F', 75000, 3, 100);
INSERT INTO EMPLOYES (employe_id, prenom, nom, naissance, sexe, salaire, succursale_id, superviseur_id)
VALUES (102, 'Marius', 'Mikkelsen', '1993-05-11', 'M', 70000, 2, 103);
INSERT INTO EMPLOYES (employe_id, prenom, nom, naissance, sexe, salaire, succursale_id, superviseur_id)
VALUES (103, 'Samawah', 'Hadad', '1979-02-24', 'F', 80000, 2, 100);
INSERT INTO EMPLOYES (employe_id, prenom, nom, naissance, sexe, salaire, succursale_id, superviseur_id)
VALUES (104, 'Andy', 'Bernard', '2000-01-06', 'M', 62000, 3, 101);


INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (2, 'Hooper', 'papier');
INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (2, 'Kurihara', 'stylos');
INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (3, 'Nikolic', 'papier');
INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (2, 'Comejo', 'formulaires');
INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (3, 'Kurihara', 'stylos');
INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (3, 'Hooper', 'papiers');
INSERT INTO fournisseurs (succursale_id, fournisseur, fourniture)
VALUES (3, 'Ulyanova', 'formulaires');

INSERT INTO succursales (succursale_id, ville, manager_id)
VALUES (1, 'Paris', 100);
INSERT INTO succursales (succursale_id, ville, manager_id)
VALUES (2, 'Lyon', 103);
INSERT INTO succursales (succursale_id, ville, manager_id)
VALUES (3, 'Marseille', 101);
