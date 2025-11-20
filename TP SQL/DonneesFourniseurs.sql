BEGIN TRANSACTION;
/*--- rajout données par table 
-- CLIENTs qui n'ont rien acheté ou qui ont acheté qu'on seule fois
*/
insert into FOURNISSEUR (FRS_NUM, FRS_NOM) values ('FRS00', 'Pour vos Cours');
insert into FOURNISSEUR (FRS_NUM, FRS_NOM) values ('FRS01', 'Pour vos Cours');
insert into FOURNISSEUR (FRS_NUM, FRS_NOM) values ('FRS02', 'Les Bureaux');
insert into FOURNISSEUR (FRS_NUM, FRS_NOM) values ('FRS03', 'Tout pour vous');


insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A01', 'FRS01', 'CRAYON', 3,1.5, 'ROUGE', 3.5);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A02', 'FRS01', 'CRAYON', 3.8,2,'VERT', 3.5);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA,ART_POIDS) values ('A03', 'FRS01', 'CAHIER', 6,5, 2);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A04', 'FRS02', 'CRAYON', 5,4,'VERT', 3);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A05', 'FRS02', 'CRAYON', 5.5,5,'VERT', 3);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A06', 'FRS03', 'TABLE_C',100 ,80,'NOIR', 200);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A07', 'FRS03', 'TABLE_R',250 ,200,'ROUGE', 200);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA,ART_POIDS) values ('A08', 'FRS02', 'CAHIER', 5,3, 3.5);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A09', 'FRS02', 'CAHIER', 7,7,'NOIR', 3);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A10', 'FRS03', 'CAHIER', 7,7,'BLANC', 3);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A11', 'FRS02', 'TABLEAU', 150,120,'BLANC', 135);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A12', 'FRS03', 'TABLEAU', 155,135,'NOIR', 30);
insert into ARTICLE ( ART_NUM, ART_FRS, ART_NOM, ART_PV,ART_PA, ART_COUL,ART_POIDS) values ('A13', 'FRS03', 'CAHIER', 7,7,'ROUGE', 3);





insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO1','Jackson','Marie', 'PARIS') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO2','Jackson','Pierre', 'PARIS') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO3','Jackson','Marie', 'LYON') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO4','Rodriguez','Sara', 'GRENOBLE') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO5','Jablonowski','Saskia', 'PARIS') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO6','NonCosom','Atti', 'LYON') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO7','Martin','Monique', 'PARIS') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO8','Harrak','Fatima', 'LYON') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('CO9','Harrak','Pierre', 'MONTPELLIER') ;
insert into CLIENT (CLT_NUM,CLT_NOM,CLT_PRENOM, CLT_LOC) values ('C10','Maginot','Camila', 'GRENOBLE') ;



insert into MAGASIN (MAG_NUM, MAG_LOC) values ('M01','PARIS');
insert into MAGASIN (MAG_NUM, MAG_LOC) values ('M02','LYON');
insert into MAGASIN (MAG_NUM, MAG_LOC) values ('M03','MONTPELLIER');
insert into MAGASIN (MAG_NUM, MAG_LOC) values ('M04','PARIS');
insert into MAGASIN (MAG_NUM, MAG_LOC) values ('M05','MARSEILLE');



insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD01','CO1','M01','2021-06-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD02','CO1','M01','2021-06-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD03','C10','M01','2021-11-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD04','CO1','M01','2020-06-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD05','CO2','M02','2021-06-16');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD06','CO2','M01','2021-06-07');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD07','CO2','M01','2021-07-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD08','CO3','M01','2021-01-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD09','CO3','M02','2021-02-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD10','CO3','M03','2021-03-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD11','CO3','M04','2021-04-06');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD12','CO3','M05','2021-06-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD13','CO4','M01','2020-11-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD14','CO4','M01','2021-06-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD15','CO5','M01','2021-02-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD16','CO5','M01','2021-06-01');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD17','CO7','M03','2021-05-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD18','CO7','M04','2020-12-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD19','CO8','M01','2021-02-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD20','CO9','M03','2021-03-10');
insert into COMMANDE (CMD_NUM, CMD_CLT, CMD_MAG, CMD_DATE) values ('CMD21','CO9','M01','2021-12-10');



-- rajouter des articles roujes achetes par des client de lyon
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A01', 'CMD01', 5, 10);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A02', 'CMD01', 3.5, 10);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A03', 'CMD02', 6, 3);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A02', 'CMD03', 4, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A13', 'CMD03', 7.5, 3);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A06', 'CMD04', 90, 4);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A11', 'CMD05', 150, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A06', 'CMD05', 100, 2);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A02', 'CMD06', 4, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A08', 'CMD07', 5, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A09', 'CMD07', 7, 2);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A07', 'CMD08', 220, 2);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A02', 'CMD09', 5, 1);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A04', 'CMD10', 5.24, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A05', 'CMD11', 6, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A02', 'CMD12', 4, 5);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A10', 'CMD13', 7, 25);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A10', 'CMD14', 7, 50);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A12', 'CMD14', 150, 1);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A12', 'CMD15', 155, 2);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A01', 'CMD16', 4, 50);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A09', 'CMD17', 7, 50);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A10', 'CMD18', 7, 20);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A13', 'CMD19', 7.5, 50);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A09', 'CMD20', 7, 50);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A10', 'CMD20', 7, 50);
insert into LIG_CMD(LCD_ART, LCD_CMD, LCD_QTE, LCD_PU) values ('A10', 'CMD21', 7, 50);









commit;

