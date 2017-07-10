-- on stocke tous les pays qui etait deja selectionnes
CREATE TABLE IF NOT EXISTS pays (
       id INT,
       nom VARCHAR(255),
       CONSTRAINT pays_0 PRIMARY KEY (id),
       CONSTRAINT pays_1 UNIQUE (nom)
);
-- on stocke tous les filleuls avec les infos necessaires
CREATE TABLE IF NOT EXISTS filleuls (
       id INT,
       nom VARCHAR(255),
       prenom VARCHAR(255),
       age INT,
       sexe BIT,
       email VARCHAR(255),
       date_arrivee DATE,
       id_nationalite INT,
       id_pays_origine INT,
       CONSTRAINT fil_0 PRIMARY KEY (id),
       -- une unique adresse mail par personne pour eviter les doublons
       CONSTRAINT fil_1 UNIQUE(email),
       CONSTRAINT fil_2 CHECK (age > 0),
       -- les pays sont stocker avec des identificateurs qui referencent le tableau pays
       CONSTRAINT fil_3 FOREIGN KEY (id_nationalite) REFERENCES pays(id),
       CONSTRAINT fil_4 FOREIGN KEY (id_pays_origine) REFERENCES pays(id)
);
-- on stocke tous les parrains
CREATE TABLE IF NOT EXISTS parrains (
       id INT,
       nom VARCHAR(255),
       prenom VARCHAR(255),
       age INT,
       sexe BIT,
       email VARCHAR(255),
       date_dispo DATE,
       CONSTRAINT par_0 PRIMARY KEY (id),
       CONSTRAINT par_1 UNIQUE(email),
       CONSTRAINT par_2 CHECK (age > 0)
);
-- les binomes sont formes par trois identificateurs
-- un pour le binome lui-meme
-- un pour le parrain
-- un pour le filleul
CREATE TABLE IF NOT EXISTS binomes (
       id INT,
       idf INT,
       idp INT,
       CONSTRAINT bin_0 PRIMARY KEY (id),
       -- plusieurs filleuls pour un parrain possible
       CONSTRAINT bin_1 UNIQUE(idf, idp),
       CONSTRAINT bin_2 FOREIGN KEY (idf) REFERENCES filleuls(id),
       CONSTRAINT bin_3 FOREIGN KEY (idp) REFERENCES parrains(id)
);
-- tableau de loisirs differents
CREATE TABLE IF NOT EXISTS loisirs (
       id INT,
       nom VARCHAR(255),
       CONSTRAINT loi_0 PRIMARY KEY (id),
       CONSTRAINT loi_1 UNIQUE (nom)       
);
-- les loisirs des filleuls
CREATE TABLE IF NOT EXISTS loisirs_f (
       id INT,
       id_loisir INT,
       -- un filleul peut en avoir plusieurs
       CONSTRAINT lf_0 PRIMARY KEY (id, id_loisir),
       CONSTRAINT lf_1 FOREIGN KEY (id) REFERENCES filleuls(id),
       -- un identificateur pointe vers le tableau des loisirs
       CONSTRAINT lf_2 FOREIGN KEY (id_loisir) REFERENCES loisirs(id)
);
-- les loisirs des parrains
CREATE TABLE IF NOT EXISTS loisirs_p (
       id INT,
       id_loisir INT,
       -- un parrain peut en avoir plusieurs
       CONSTRAINT lp_0 PRIMARY KEY (id, id_loisir),
       CONSTRAINT lp_1 FOREIGN KEY (id) REFERENCES parrains(id),
       -- un identificateur pointe vers le tableau des loisirs
       CONSTRAINT lp_2 FOREIGN KEY (id_loisir) REFERENCES loisirs(id)
);
-- tableau de tous les universites
CREATE TABLE IF NOT EXISTS universites (
       id int,
       nom VARCHAR(255),
       CONSTRAINT u_0 PRIMARY KEY (id),
       CONSTRAINT u_1 UNIQUE (nom)
);
-- tableau des filleuls et leurs univ
CREATE TABLE IF NOT EXISTS universite_f (
       id int,
       id_uni INT,
       -- un filleul peut appartenir a plusieurs
       CONSTRAINT uf_0 PRIMARY KEY (id, id_uni),
       CONSTRAINT uf_1 FOREIGN KEY (id) REFERENCES filleuls(id),
       CONSTRAINT uf_2 FOREIGN KEY (id_uni) REFERENCES universites(id) 
);
-- tableau des parrains et leurs univ
CREATE TABLE IF NOT EXISTS universite_p (
       id int,
       id_uni INT,
       -- un parrain peut appartenir a plusieurs
       CONSTRAINT up_0 PRIMARY KEY (id, id_uni),
       CONSTRAINT up_1 FOREIGN KEY (id) REFERENCES parrains(id),
       CONSTRAINT up_2 FOREIGN KEY (id_uni) REFERENCES universites(id) 
);
-- tableau de tous les langues
CREATE TABLE IF NOT EXISTS langues (
       id INT,
       nom VARCHAR(255),
       CONSTRAINT la_0 PRIMARY KEY (id),
       CONSTRAINT la_1 UNIQUE (nom)
);
-- tableau des parrains et les langues qu'ils parlent
CREATE TABLE IF NOT EXISTS langues_p (
       idp INT,
       id_langue INT,
       -- un parrain peut parler plusieurs
       CONSTRAINT lap_0 PRIMARY KEY (idp, id_langue),
       CONSTRAINT lap_1 FOREIGN KEY (idp) REFERENCES parrains(id),
       CONSTRAINT lap_2 FOREIGN KEY (id_langue) REFERENCES langues(id)
);
-- tableau des filieres possibles
CREATE TABLE IF NOT EXISTS filieres (
       id INT,
       nom VARCHAR(255),
       CONSTRAINT filiere_0 PRIMARY KEY (id),
       CONSTRAINT filiere_1 UNIQUE (nom)
);
-- tableau des filieres des parrains
CREATE TABLE IF NOT EXISTS filiere_p (
       idp INT,
       idfiliere INT,
       -- un parrain peut appartenir a plusieurs filieres
       CONSTRAINT filp_0 PRIMARY KEY (idp, idfiliere),
       CONSTRAINT filp_1 FOREIGN KEY (idp) REFERENCES parrains(id),
       CONSTRAINT filp_2 FOREIGN KEY (idfiliere) REFERENCES filieres(id)
);
-- tableau des filieres des filleuls
CREATE TABLE IF NOT EXISTS filiere_f (
       idf INT,
       idfiliere INT,
       -- un filleul peut appartenir a plusieurs filieres
       CONSTRAINT filf_0 PRIMARY KEY (idf, idfiliere),
       CONSTRAINT filf_1 FOREIGN KEY (idf) REFERENCES filleuls(id),
       CONSTRAINT filf_2 FOREIGN KEY (idfiliere) REFERENCES filieres(id)
);
