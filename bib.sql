PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "sudoc_library" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "library_name" varchar(200) NOT NULL, "library_id" varchar(10) NOT NULL UNIQUE, "library_rcr" varchar(10) NOT NULL UNIQUE, "institution" varchar(5) NOT NULL);
INSERT INTO sudoc_library VALUES(1,'Bib. Droit privé','1102700000','333182205','UB');
INSERT INTO sudoc_library VALUES(2,'Bib. droit public','1102800000','333182210','UB');
INSERT INTO sudoc_library VALUES(3,'Bib. Ecole Nationale Supérieure de Cognitique','2000200000','335222111','INP');
INSERT INTO sudoc_library VALUES(4,'Bib. économie','1102500000','333182102','UB');
INSERT INTO sudoc_library VALUES(5,'Bib. Histoire du droit','1102600000','333182208','UB');
INSERT INTO sudoc_library VALUES(6,'Bib. pluridisciplinaire','1402200000','330632103','UB');
INSERT INTO sudoc_library VALUES(7,'BMI','1201000000','335222209','UB');
INSERT INTO sudoc_library VALUES(8,'BU Droit sc. politique économie','1103300000','335222102','UB');
INSERT INTO sudoc_library VALUES(9,'BU Santé','1302100000','330632101','UB');
INSERT INTO sudoc_library VALUES(10,'BU Sc. et techniques','1201300000','335222101','UB');
INSERT INTO sudoc_library VALUES(11,'BU Sciences de l''homme','1402300000','330632102','UB');
INSERT INTO sudoc_library VALUES(12,'BU STAPS','1402400000','335222105','UB');
INSERT INTO sudoc_library VALUES(13,'Centres de recherche en droit','1103400000','330632209','UB');
INSERT INTO sudoc_library VALUES(14,'Centres de recherche en économie','1103500000','333182201','UB');
INSERT INTO sudoc_library VALUES(15,'CRDEI','1103200000','333182101','UB');
INSERT INTO sudoc_library VALUES(16,'CRPP','1201100000','333182213','UB');
INSERT INTO sudoc_library VALUES(17,'Diophante d''Alexandrie','1201600000','335222230','UB');
INSERT INTO sudoc_library VALUES(18,'Droit-langues Agen','1103000000','470012101','UB');
INSERT INTO sudoc_library VALUES(19,'ENSCBP','2000400000','333182103','INP');
INSERT INTO sudoc_library VALUES(20,'ENSEGID','2000300000','335222221','INP');
INSERT INTO sudoc_library VALUES(21,'ENSEIRB-MATHMECA','2000100000','335222306','INP');
INSERT INTO sudoc_library VALUES(22,'EPOC Arcachon','1201400000','330092101','UB');
INSERT INTO sudoc_library VALUES(23,'EPOC Talence','1201800000','335222201','UB');
INSERT INTO sudoc_library VALUES(24,'ESPE Bordeaux','1500300000','330632212','UB');
INSERT INTO sudoc_library VALUES(25,'ESPE Mérignac','1500400000','332812201','UB');
INSERT INTO sudoc_library VALUES(26,'ESPE Mont-de-Marsan','1500600000','401922201','UB');
INSERT INTO sudoc_library VALUES(27,'ESPE Pau','1500500000','644452201','UB');
INSERT INTO sudoc_library VALUES(28,'ESPE Périgueux','1500700000','243222203','UB');
INSERT INTO sudoc_library VALUES(29,'ICMCB','1201200000','333182204','UB');
INSERT INTO sudoc_library VALUES(30,'Infothèque PUSG','1601900000','330632201','UB');
INSERT INTO sudoc_library VALUES(31,'Institut droit et économie Périgueux','1103100000','243222202','UB');
INSERT INTO sudoc_library VALUES(32,'Institut du travail','1102900000','333182211','UB');
INSERT INTO sudoc_library VALUES(33,'Institut thermalisme Dax','1302000000','400882201','UB');
INSERT INTO sudoc_library VALUES(34,'ISVV','1201500000','335502201','UB');
INSERT INTO sudoc_library VALUES(35,'IUT Bordeaux-Gradignan','1200900000','331922101','UB');
INSERT INTO sudoc_library VALUES(36,'LAB','1201700000','331672201','UB');
INSERT INTO sudoc_library VALUES(37,'Médiaquitaine','1000200000','331922302','UB');
INSERT INTO sudoc_library VALUES(38,'Michel Serres Agen','1500800000','470012102','UB');
INSERT INTO sudoc_library VALUES(39,'Sciences Po Bordeaux','4000100000','335222203','IEP');
INSERT INTO sudoc_library VALUES(40,'Géographie/Cartothèque','3300200000','335222107','UBM');
INSERT INTO sudoc_library VALUES(41,'Franco-allemande','3200600000','330635106','UBM');
INSERT INTO sudoc_library VALUES(42,'L.E./L.E.A.','3200800000','335222109','UBM');
INSERT INTO sudoc_library VALUES(43,'IATU/ISIC (Aménagement/Communication)','3300700000','333182207','UBM');
INSERT INTO sudoc_library VALUES(44,'Etudes ibériques','3200100000','335222106','UBM');
INSERT INTO sudoc_library VALUES(45,'Robert Etienne','3101000000','335222205','UBM');
INSERT INTO sudoc_library VALUES(46,'Histoire/Histoire de l''art','3100500000','335222110','UBM');
INSERT INTO sudoc_library VALUES(47,'Lettres et Sciences humaines','3100400000','335222103','UBM');
INSERT INTO sudoc_library VALUES(48,'IUT/IJBA','3400900000','335222216','UBM');
INSERT INTO sudoc_library VALUES(49,'Henri Guillemin','3200300000','335222108','UBM');
INSERT INTO sudoc_library VALUES(50,'Bib. du PJJ (CERCCLE-ISCJ)','1103600000','330632213','UB');
INSERT INTO sudoc_library VALUES(51,'Bib. Electronique (UB)','1000300000','335229901','UB');
INSERT INTO sudoc_library VALUES(52,'Bib. Electronique (UBM)','3000100000','335229906','UBM');
INSERT INTO sudoc_library VALUES(53,'Bib. Electronique (IEP)','4000200000','335229907','IEP');
COMMIT;