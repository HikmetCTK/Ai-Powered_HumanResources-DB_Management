-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: human_resources
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `department` varchar(9) DEFAULT NULL,
  `salary` decimal(8,2) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Alvin','Fernier','1967-09-18','Male','Human Resources Assistant III','IT',31980.52,'2017-09-07','123@gmail.com','243-979-3929','123'),(2,'Chelsey','Gummary','1963-11-26','Female','Tax Accountant','Finance',47864.14,'2012-07-28','helahehikmet@gmail.com','829-856-3632','hiko5858'),(3,'Bradan','Beisley','1996-03-06','Male','Research Associate','IT',78908.10,'2014-08-16','bbeisley2@bloomberg.com','574-899-3148','728=xy{X'),(4,'Sibylle','Houtby','1965-11-12','Female','Senior Cost Accountant','IT',70327.65,'2017-09-24','shoutby3@slate.com','773-887-2470','409_8`'),(5,'Bail','Frere','1960-08-06','Male','Data Coordinator','Finance',66197.04,'2014-10-01','bfrere4@ucla.edu','576-305-4297','150{d'),(6,'Bondie','Astbury','1952-08-10','Male','VP Marketing','IT',80845.46,'2021-02-04','bastbury5@dedecms.com','176-693-2633','907$_WZ4'),(7,'Monti','Kruschev','1965-05-11','Male','Assistant Professor','IT',149131.56,'2011-08-12','mkruschev6@ibm.com','167-124-3782','650*0'),(8,'Trudie','Tomasz','1998-05-27','Genderfluid','Human Resources Assistant IV','Finance',103946.56,'2021-02-24','ttomasz7@usnews.com','106-659-6709','724)|>F'),(9,'Corilla','Cornejo','1978-11-14','Female','Operator','IT',122954.69,'2018-08-17','ccornejo8@e-recht24.de','439-323-9275','848%e'),(10,'Felipa','Helder','1998-09-20','Female','Biostatistician III','HR',43567.00,'2021-12-24','fhelder9@slashdot.org','771-921-9341','007,|M'),(11,'Erik','Aust','1999-02-04','Male','Nurse Practicioner','Finance',42007.45,'2012-10-13','eausta@google.ca','588-526-2977','330(Fj!_'),(12,'Mallory','Dodimead','1964-01-01','Male','Database Administrator III','HR',52762.67,'2018-03-11','mdodimeadb@washington.edu','143-595-9744','149`D'),(13,'Trina','Boig','1972-05-08','Female','VP Product Management','IT',127888.09,'2013-01-02','tboigc@slate.com','740-247-6386','450$ges$'),(14,'Neill','Swannick','1955-06-02','Male','Senior Developer','HR',108875.91,'2013-10-31','nswannickd@biblegateway.com','549-873-7290','279<g>J'),(15,'Brynne','Rorke','1997-04-10','Female','Cost Accountant','Marketing',98048.83,'2017-09-20','brorkee@latimes.com','332-403-3897','462}l'),(16,'Elwood','Crandon','1989-11-17','Male','Food Chemist','IT',66636.20,'2019-03-10','ecrandonf@mac.com','404-549-5846','436.&+kC'),(17,'Eddie','Hutcheon','1971-09-08','Female','Statistician I','Finance',38029.90,'2012-03-02','ehutcheong@sitemeter.com','716-204-5986','852\"l'),(18,'Adriaens','Tulk','1969-09-12','Female','Professor','Finance',127113.96,'2019-11-21','atulkh@washington.edu','853-213-2079','683~LIw'),(19,'Ruth','Peile','1986-08-13','Female','Associate Professor','Finance',54493.58,'2015-10-04','rpeilei@simplemachines.org','810-894-1351','978!*iu'),(20,'Aggie','Weedall','1979-12-13','Female','Software Engineer IV','IT',126614.33,'2015-02-24','aweedallj@chron.com','443-657-1371','030/L7Xg'),(21,'Artur','Reah','1999-01-18','Male','VP Product Management','IT',61834.09,'2018-01-18','areahk@uol.com.br','602-429-5498','855_5Pq2'),(22,'Joaquin','Hamal','1956-07-04','Non-binary','Speech Pathologist','HR',33981.32,'2013-03-24','jhamall@biglobe.ne.jp','251-335-2027','790=&'),(23,'Cointon','Matterface','1980-01-24','Male','Pharmacist','HR',88803.50,'2015-06-12','cmatterfacem@opensource.org','791-744-7187','815>~,J'),(24,'Clayton','Hail','1990-11-11','Male','Engineer IV','IT',106005.34,'2019-11-20','chailn@nsw.gov.au','815-815-9057','614*'),(25,'Jeana','Miko','1968-08-27','Female','General Manager','Marketing',125137.33,'2017-04-29','jmikoo@cnn.com','176-813-4627','708?9B'),(26,'Bailie','Chasier','1964-12-18','Male','Statistician IV','HR',122229.70,'2011-02-13','bchasierp@free.fr','486-170-9754','329*n%l'),(27,'Ellyn','Plastow','1985-02-18','Agender','Payment Adjustment Coordinator','IT',89892.57,'2021-05-02','eplastowq@woothemes.com','893-170-4203','865%t'),(28,'Jackie','Latore','1963-07-07','Female','Software Test Engineer III','IT',95901.57,'2015-08-18','jlatorer@yandex.ru','854-987-5189','984{s3'),(29,'Derick','Pietruszka','1994-08-12','Male','Design Engineer','Marketing',135528.39,'2015-09-18','dpietruszkas@ed.gov','846-161-7792','454!'),(30,'Frazier','Gamlyn','1988-07-17','Male','Actuary','HR',80890.83,'2010-08-29','fgamlynt@tinypic.com','842-751-6679','808<'),(31,'Hilary','Stilldale','1968-02-23','Female','Civil Engineer','Finance',133049.25,'2010-08-19','hstilldaleu@cam.ac.uk','806-559-3774','716&/\"'),(32,'Barth','Shotboult','1995-05-07','Male','VP Accounting','IT',142555.18,'2011-11-07','bshotboultv@wikimedia.org','228-798-1692','044{'),(33,'Brit','Corness','1990-08-20','Female','Registered Nurse','IT',85710.66,'2011-08-02','bcornessw@ycombinator.com','483-583-9634','681&$y'),(34,'Roth','Tildesley','1974-08-14','Male','Sales Associate','Marketing',85365.26,'2020-09-12','rtildesleyx@360.cn','359-214-7523','710$b'),(35,'Glennie','Guiot','1971-12-19','Female','Electrical Engineer','Finance',54160.14,'2018-10-10','gguioty@qq.com','980-183-5214','618(9ji'),(36,'Pascale','Hackleton','1982-12-09','Male','Environmental Specialist','Finance',81701.47,'2012-05-12','phackletonz@networkadvertising.org','761-186-1721','318_y%'),(37,'Jeremias','Simonetto','1956-12-16','Male','Database Administrator III','IT',56158.66,'2019-02-16','jsimonetto10@ifeng.com','135-765-5296','675%}{'),(38,'Frederick','Amberson','1958-05-18','Male','Community Outreach Specialist','Finance',147484.16,'2013-08-28','famberson11@cloudflare.com','985-743-3183','412,'),(39,'Alfie','Cabera','1959-08-15','Male','Senior Editor','Finance',105968.46,'2012-08-28','acabera12@dyndns.org','541-440-9286','490(S4ID'),(40,'Prudi','Stedson','1990-09-22','Female','Senior Sales Associate','IT',143289.36,'2010-11-09','pstedson13@wikimedia.org','305-799-0966','185?i0R'),(41,'Whit','Smillie','1952-02-24','Male','Paralegal','IT',133678.81,'2018-07-26','wsmillie14@hc360.com','668-572-6929','029\'W\"~'),(42,'Kym','Willoughway','1950-03-06','Female','Structural Engineer','Finance',88778.95,'2010-10-15','kwilloughway15@stanford.edu','963-458-6607','676.*qj'),(43,'Myranda','Bride','1976-02-04','Female','Operator','HR',141390.23,'2020-06-28','mbride16@phoca.cz','612-127-7010','960+'),(44,'Jennilee','Derl','1962-01-26','Female','Software Test Engineer III','IT',102476.94,'2019-05-25','jderl17@discuz.net','853-471-6296','378#y8'),(45,'Lin','Dummigan','1972-06-13','Female','VP Accounting','IT',73384.59,'2016-08-18','ldummigan18@weebly.com','561-330-7465','656.JG_6'),(46,'Miran','Tue','1967-08-17','Female','Clinical Specialist','Finance',42920.66,'2021-04-05','mtue19@arizona.edu','746-719-9185','154!'),(47,'Sophi','Rudham','1973-11-20','Female','Recruiter','IT',71368.48,'2011-01-26','srudham1a@squarespace.com','128-967-1986','932(ig?'),(48,'Waiter','Meach','1954-05-27','Male','Accountant II','Marketing',101022.29,'2019-05-10','wmeach1b@cnet.com','399-250-7740','307|klh{'),(49,'Shayne','Pringuer','1999-03-29','Male','Nuclear Power Engineer','HR',48510.98,'2015-12-16','springuer1c@cyberchimps.com','113-464-9734','741\"WL|C'),(50,'Sascha','Gamage','1982-04-01','Male','Database Administrator IV','Marketing',75412.34,'2014-02-26','sgamage1d@slashdot.org','630-640-2184','061|?G\'');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-18 21:23:38
