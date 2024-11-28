CREATE DATABASE  IF NOT EXISTS `human_resources` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `human_resources`;
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
-- Table structure for table `employee_items`
--

DROP TABLE IF EXISTS `employee_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_items` (
  `employee_id` int NOT NULL,
  `item_id` int NOT NULL,
  `assignment_date` datetime NOT NULL,
  PRIMARY KEY (`employee_id`,`item_id`,`assignment_date`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `employee_items_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `employee_items_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_items`
--

LOCK TABLES `employee_items` WRITE;
/*!40000 ALTER TABLE `employee_items` DISABLE KEYS */;
INSERT INTO `employee_items` VALUES (2,1,'1967-11-16 19:35:06'),(3,1,'1976-12-13 23:05:54'),(6,1,'2008-07-19 16:27:45'),(7,1,'1920-06-03 16:50:42'),(7,1,'1948-07-28 08:16:14'),(7,1,'2005-04-25 06:24:27'),(9,1,'1948-12-09 16:46:26'),(9,1,'1961-07-26 23:42:38'),(9,1,'1985-07-04 04:09:55'),(12,1,'1960-02-27 19:21:41'),(12,1,'1993-09-23 10:10:21'),(15,1,'1971-12-06 13:36:46'),(16,1,'1934-04-01 16:23:53'),(17,1,'1947-12-14 10:47:19'),(20,1,'2020-09-14 03:34:11'),(22,1,'1902-03-20 12:39:55'),(22,1,'1985-10-22 13:15:17'),(22,1,'2014-07-07 17:15:13'),(24,1,'1968-05-03 01:15:14'),(24,1,'2018-12-27 14:00:53'),(25,1,'1901-05-07 07:38:37'),(26,1,'1919-08-05 01:32:28'),(27,1,'1903-04-09 15:42:35'),(27,1,'1926-10-20 16:32:47'),(27,1,'2001-08-16 07:57:41'),(28,1,'1909-01-24 04:41:21'),(31,1,'1906-04-19 22:24:41'),(31,1,'1979-04-15 02:03:53'),(32,1,'1963-10-01 17:51:33'),(33,1,'1937-02-26 12:24:00'),(33,1,'1944-06-07 06:36:08'),(33,1,'1959-05-29 23:53:53'),(35,1,'1936-10-26 17:04:02'),(35,1,'1964-08-10 16:11:24'),(35,1,'1992-10-01 20:33:50'),(38,1,'1954-07-02 14:23:02'),(38,1,'1989-03-28 21:14:08'),(40,1,'1977-05-07 15:33:02'),(41,1,'1932-01-12 22:34:38'),(42,1,'1905-09-03 15:49:39'),(42,1,'1967-11-16 19:35:06'),(43,1,'1947-03-16 15:36:38'),(44,1,'2011-12-24 10:59:57'),(46,1,'1918-12-11 12:52:34'),(47,1,'1907-09-29 07:12:47'),(48,1,'1903-06-15 21:20:39'),(50,1,'1923-11-25 01:19:07'),(50,1,'1999-04-02 17:52:48'),(5,2,'1959-11-03 22:47:23'),(7,2,'1921-07-20 13:50:43'),(7,2,'1967-01-20 14:28:27'),(7,2,'1974-05-21 00:33:53'),(8,2,'1967-01-29 00:03:00'),(9,2,'1930-04-04 22:34:44'),(9,2,'1962-08-20 23:56:22'),(12,2,'2017-07-26 14:31:18'),(13,2,'1928-10-12 02:56:37'),(15,2,'1920-12-07 21:18:40'),(15,2,'1922-05-31 02:24:14'),(16,2,'1966-08-29 18:26:51'),(16,2,'1972-05-03 02:38:37'),(17,2,'1941-07-18 10:26:26'),(17,2,'2016-02-11 11:55:03'),(18,2,'2023-10-04 06:05:12'),(19,2,'1918-07-11 08:21:29'),(21,2,'1928-08-06 06:22:16'),(22,2,'1942-09-08 11:31:48'),(22,2,'1994-05-24 14:49:26'),(23,2,'2007-10-07 01:12:55'),(24,2,'1987-09-12 00:57:25'),(26,2,'1931-05-09 10:02:17'),(26,2,'1999-02-15 13:21:26'),(29,2,'1959-03-09 22:11:14'),(29,2,'1998-07-14 14:02:07'),(31,2,'1923-06-18 01:43:31'),(34,2,'1915-11-10 01:09:58'),(34,2,'1999-11-12 17:07:41'),(35,2,'1914-01-07 13:01:40'),(35,2,'2003-12-21 14:14:55'),(36,2,'1939-03-28 03:15:41'),(37,2,'1905-10-31 07:31:44'),(40,2,'1952-05-07 03:16:44'),(40,2,'1985-06-25 14:12:39'),(40,2,'2022-11-06 06:53:00'),(41,2,'1901-09-22 13:42:15'),(41,2,'1994-07-17 17:33:47'),(42,2,'1922-07-12 07:22:42'),(42,2,'1977-06-28 09:55:29'),(43,2,'1978-07-02 16:57:55'),(43,2,'1981-06-07 17:02:09'),(44,2,'1975-02-20 00:19:13'),(46,2,'1940-10-25 03:14:08'),(46,2,'1955-07-19 00:57:22'),(47,2,'1915-10-23 19:40:28'),(47,2,'1981-03-01 15:15:38'),(47,2,'2007-10-04 18:44:00'),(48,2,'1989-11-13 20:55:48'),(49,2,'2016-05-01 01:42:33'),(49,2,'2019-03-12 18:36:38'),(1,3,'1948-05-22 02:24:37'),(2,3,'1950-03-03 17:58:52'),(2,3,'2014-12-07 03:17:59'),(2,3,'2023-03-26 10:35:22'),(3,3,'1941-10-12 03:08:17'),(3,3,'1969-07-15 15:34:44'),(4,3,'1956-08-01 15:30:15'),(4,3,'2004-09-02 08:07:59'),(4,3,'2007-07-29 23:43:20'),(5,3,'1932-05-24 11:10:46'),(5,3,'2020-05-01 09:38:32'),(6,3,'1934-12-21 05:00:31'),(6,3,'1977-01-08 19:27:43'),(6,3,'1984-04-21 21:28:06'),(7,3,'1903-03-10 07:52:07'),(7,3,'1991-12-31 11:57:48'),(9,3,'1961-03-19 14:36:48'),(10,3,'1954-01-08 11:18:53'),(10,3,'1993-01-24 17:19:01'),(11,3,'1954-12-18 10:23:56'),(12,3,'1910-01-12 04:19:51'),(12,3,'1956-03-09 05:44:23'),(12,3,'1961-06-21 05:20:25'),(13,3,'1971-12-31 08:23:12'),(13,3,'1984-04-28 06:49:20'),(14,3,'1912-02-10 07:56:04'),(14,3,'2017-02-17 20:56:22'),(16,3,'1920-09-27 16:10:01'),(16,3,'2014-07-10 01:07:40'),(18,3,'1902-08-27 20:16:39'),(18,3,'1931-08-10 18:34:43'),(18,3,'1960-07-19 07:14:48'),(18,3,'1996-05-25 01:48:17'),(19,3,'2022-12-28 05:22:15'),(20,3,'2023-04-13 09:33:54'),(21,3,'2001-06-17 02:12:30'),(22,3,'1950-12-30 17:04:18'),(22,3,'1964-03-04 06:03:24'),(24,3,'1959-03-25 03:00:21'),(25,3,'1944-02-05 03:55:20'),(25,3,'1998-12-28 01:55:15'),(26,3,'1981-10-30 01:37:01'),(27,3,'1956-07-14 13:31:44'),(27,3,'1969-07-15 15:34:44'),(29,3,'1984-09-16 11:15:37'),(31,3,'1955-12-01 17:58:38'),(32,3,'1977-05-03 12:59:39'),(32,3,'1980-11-25 14:45:36'),(33,3,'1989-07-11 17:09:29'),(33,3,'2011-12-26 00:29:53'),(36,3,'2011-12-21 01:34:40'),(37,3,'1950-01-19 00:37:51'),(38,3,'1950-03-04 04:30:25'),(38,3,'1998-05-02 11:35:16'),(39,3,'1954-05-16 14:09:00'),(40,3,'1964-10-31 09:19:32'),(41,3,'1991-12-11 05:29:45'),(42,3,'2015-08-13 03:15:30'),(43,3,'1910-08-16 23:57:04'),(43,3,'2014-10-29 20:53:04'),(43,3,'2017-04-16 08:33:05'),(43,3,'2020-05-01 09:38:32'),(44,3,'1982-10-14 21:12:47'),(45,3,'1986-12-04 09:34:20'),(46,3,'1919-10-14 14:45:16'),(46,3,'1951-03-20 12:56:43'),(46,3,'1973-01-25 00:11:32'),(47,3,'1948-08-02 21:22:09'),(50,3,'2001-10-01 22:20:11'),(1,4,'2024-10-26 15:37:12'),(2,4,'1913-10-02 16:05:59'),(2,4,'2008-02-15 10:11:43'),(3,4,'1920-09-11 19:56:13'),(3,4,'1988-12-11 08:15:33'),(4,4,'1971-03-21 08:43:55'),(4,4,'1996-02-09 18:18:51'),(6,4,'1912-03-12 22:36:04'),(6,4,'2019-06-25 19:35:53'),(9,4,'1920-11-02 13:18:26'),(10,4,'1973-02-11 16:06:03'),(10,4,'2019-10-14 05:41:13'),(11,4,'1936-05-09 14:38:49'),(13,4,'1965-11-28 01:59:49'),(14,4,'1938-12-22 05:41:03'),(14,4,'1960-10-11 18:34:32'),(16,4,'2009-02-25 16:57:54'),(17,4,'2008-08-08 23:10:39'),(17,4,'2017-02-24 08:41:18'),(18,4,'1911-04-28 00:13:48'),(21,4,'1986-03-03 05:35:33'),(22,4,'1968-05-17 11:35:53'),(25,4,'1929-10-30 05:02:43'),(28,4,'1920-04-30 00:43:15'),(28,4,'1974-10-18 04:34:59'),(29,4,'1901-05-13 21:46:26'),(30,4,'1908-01-04 01:07:55'),(30,4,'1915-07-24 18:10:16'),(30,4,'2005-03-16 00:56:15'),(31,4,'1923-07-29 18:37:59'),(31,4,'1977-04-12 05:55:44'),(34,4,'1980-07-06 01:12:28'),(36,4,'1915-06-06 16:02:10'),(37,4,'1906-11-29 19:16:16'),(37,4,'1971-04-14 21:38:57'),(38,4,'1946-09-01 08:58:01'),(41,4,'1956-01-15 20:55:15'),(42,4,'1974-12-25 11:35:50'),(43,4,'1912-09-17 02:59:35'),(44,4,'1921-05-01 14:17:45'),(45,4,'1995-10-06 04:51:11'),(48,4,'1900-03-14 02:46:06'),(48,4,'1949-07-12 18:20:25'),(48,4,'1996-02-09 18:18:51'),(50,4,'1965-08-30 04:33:45'),(1,5,'2010-07-27 11:54:10'),(2,5,'1932-02-28 05:48:46'),(4,5,'1960-09-18 00:35:36'),(5,5,'1931-07-13 10:44:59'),(6,5,'1922-01-30 02:30:38'),(8,5,'1960-02-11 21:54:01'),(10,5,'1967-02-12 02:33:35'),(13,5,'1933-02-06 12:17:42'),(13,5,'1963-10-22 06:41:58'),(15,5,'1991-10-10 05:01:30'),(18,5,'1956-11-28 10:55:01'),(19,5,'1903-06-19 10:01:56'),(21,5,'1921-01-08 15:23:34'),(21,5,'1995-07-28 23:46:13'),(22,5,'1952-08-26 02:59:16'),(23,5,'1919-09-20 05:40:59'),(23,5,'1957-10-22 01:54:27'),(24,5,'2002-09-24 01:48:17'),(25,5,'1930-02-14 08:03:06'),(29,5,'1953-09-02 05:03:36'),(30,5,'1945-11-15 02:20:28'),(33,5,'1974-04-28 14:56:58'),(33,5,'1983-07-27 19:15:09'),(34,5,'1972-09-21 21:05:21'),(37,5,'1951-12-26 12:58:41'),(37,5,'2015-08-20 08:04:00'),(38,5,'1946-12-03 13:32:39'),(41,5,'1911-03-17 02:54:57'),(43,5,'1928-02-02 00:48:44'),(43,5,'2011-06-16 22:28:46'),(43,5,'2017-08-03 00:00:51'),(44,5,'1927-04-12 17:27:47'),(46,5,'1908-02-10 01:22:40'),(47,5,'1916-12-26 06:04:19'),(47,5,'1961-06-20 21:20:44'),(47,5,'1994-12-14 10:22:52'),(48,5,'1901-12-21 16:20:43'),(49,5,'1963-12-08 01:16:42'),(49,5,'1969-02-23 07:48:05'),(49,5,'1995-07-04 12:44:09'),(50,5,'1940-02-23 04:56:25'),(50,5,'1954-06-14 13:55:43'),(2,6,'1952-07-09 22:48:19'),(2,6,'2013-04-11 23:14:29'),(2,6,'2022-10-05 06:24:09'),(3,6,'1901-05-19 08:57:34'),(5,6,'1991-06-01 19:47:55'),(6,6,'1919-03-19 07:39:15'),(6,6,'1994-08-19 08:51:40'),(6,6,'2022-10-29 14:10:41'),(7,6,'1920-01-03 05:04:15'),(7,6,'1928-07-12 01:52:39'),(9,6,'1982-07-17 21:40:50'),(16,6,'1956-02-15 08:19:01'),(16,6,'2009-08-10 14:30:45'),(16,6,'2022-06-29 14:01:54'),(17,6,'1989-01-04 17:24:33'),(18,6,'1989-09-20 16:46:03'),(18,6,'2007-11-12 10:18:18'),(19,6,'1934-12-23 19:49:34'),(20,6,'1938-08-06 01:13:00'),(20,6,'1942-04-05 09:44:15'),(20,6,'1964-06-01 23:25:17'),(24,6,'2011-11-25 09:04:32'),(27,6,'1982-03-28 19:57:31'),(28,6,'1900-08-13 09:19:23'),(29,6,'1964-10-09 21:58:43'),(29,6,'2005-10-04 00:09:48'),(30,6,'1988-11-08 11:06:41'),(31,6,'2020-05-14 19:57:37'),(32,6,'1902-12-29 02:32:44'),(33,6,'1949-04-17 17:17:05'),(35,6,'1925-03-26 19:30:32'),(35,6,'1952-10-04 14:47:22'),(36,6,'1932-05-31 21:25:38'),(36,6,'1942-02-04 11:52:49'),(37,6,'1960-07-18 00:07:14'),(37,6,'2009-11-04 08:55:40'),(37,6,'2024-03-03 04:53:14'),(40,6,'1946-03-21 00:07:58'),(41,6,'2014-08-23 09:05:33'),(44,6,'1937-07-30 22:08:42'),(44,6,'1963-06-24 09:12:15'),(44,6,'1985-04-26 13:27:41'),(44,6,'1995-07-15 23:53:53'),(45,6,'2012-07-10 21:33:06'),(47,6,'1969-09-10 17:29:19'),(48,6,'1935-10-20 09:56:21'),(48,6,'1946-09-18 22:21:02'),(49,6,'1929-03-26 14:37:35'),(49,6,'1983-11-29 07:55:05');
/*!40000 ALTER TABLE `employee_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `employee_items_with_names`
--

DROP TABLE IF EXISTS `employee_items_with_names`;
/*!50001 DROP VIEW IF EXISTS `employee_items_with_names`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `employee_items_with_names` AS SELECT 
 1 AS `employee_id`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `item_id`,
 1 AS `item_name`,
 1 AS `assignment_date`*/;
SET character_set_client = @saved_cs_client;

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
  `department` varchar(25) DEFAULT NULL,
  `salary` decimal(8,2) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Alvin','Fernier','1967-09-18','Male','Human resources','IT',31980.52,'2017-09-07','hikmetcatak99@gmail.com','243-979-3929','123',1),(2,'Hikmet','Catak','1963-11-26','Female','Human resources','Finance',47864.14,'2012-07-28','hikmetcatak26@gmail.com','829-856-3632','5858',1),(3,'Bradan','Beisley','1996-03-06','Male','Research Associate','IT',78908.10,'2014-08-16','bbeisley2@bloomberg.com','574-899-3148','728=xy{X',1),(4,'Sibylle','Houtby','1965-11-12','Female','Senior Cost Accountant','IT',70327.65,'2017-09-24','shoutby3@slate.com','773-887-2470','409_8`',1),(5,'Bail','Frere','1960-08-06','Male','Data Coordinator','Finance',66197.04,'2014-10-01','bfrere4@ucla.edu','576-305-4297','150{d',1),(6,'Bondie','Astbury','1952-08-10','Male','VP Marketing','IT',80845.46,'2021-02-04','bastbury5@dedecms.com','176-693-2633','907$_WZ4',1),(7,'Monti','Kruschev','1965-05-11','Male','Assistant Professor','IT',149131.56,'2011-08-12','mkruschev6@ibm.com','167-124-3782','650*0',1),(8,'Trudie','Tomasz','1998-05-27','Genderfluid','Human Resources Assistant IV','Finance',103946.56,'2021-02-24','ttomasz7@usnews.com','106-659-6709','724)|>F',1),(9,'Corilla','Cornejo','1978-11-14','Female','Operator','IT',122954.69,'2018-08-17','ccornejo8@e-recht24.de','439-323-9275','848%e',1),(10,'Felipa','Helder','1998-09-20','Female','Biostatistician III','HR',43567.00,'2021-12-24','fhelder9@slashdot.org','771-921-9341','007,|M',1),(11,'Erik','Aust','1999-02-04','Male','Nurse Practicioner','Finance',42007.45,'2012-10-13','eausta@google.ca','588-526-2977','330(Fj!_',1),(12,'Mallory','Dodimead','1964-01-01','Male','Database Administrator III','HR',52762.67,'2018-03-11','mdodimeadb@washington.edu','143-595-9744','149`D',1),(13,'Trina','Boig','1972-05-08','Female','VP Product Management','IT',127888.09,'2013-01-02','tboigc@slate.com','740-247-6386','450$ges$',1),(14,'Neill','Swannick','1955-06-02','Male','Senior Developer','HR',108875.91,'2013-10-31','nswannickd@biblegateway.com','549-873-7290','279<g>J',1),(15,'Brynne','Rorke','1997-04-10','Female','Cost Accountant','Marketing',98048.83,'2017-09-20','brorkee@latimes.com','332-403-3897','462}l',1),(16,'Elwood','Crandon','1989-11-17','Male','Food Chemist','IT',66636.20,'2019-03-10','ecrandonf@mac.com','404-549-5846','436.&+kC',1),(17,'Eddie','Hutcheon','1971-09-08','Female','Statistician I','Finance',38029.90,'2012-03-02','ehutcheong@sitemeter.com','716-204-5986','852\"l',1),(18,'Adriaens','Tulk','1969-09-12','Female','Professor','Finance',127113.96,'2019-11-21','atulkh@washington.edu','853-213-2079','683~LIw',1),(19,'Ruth','Peile','1986-08-13','Female','Associate Professor','Finance',54493.58,'2015-10-04','rpeilei@simplemachines.org','810-894-1351','978!*iu',1),(20,'Aggie','Weedall','1979-12-13','Female','Software Engineer IV','IT',126614.33,'2015-02-24','aweedallj@chron.com','443-657-1371','030/L7Xg',1),(21,'Artur','Reah','1999-01-18','Male','VP Product Management','IT',61834.09,'2018-01-18','areahk@uol.com.br','602-429-5498','855_5Pq2',1),(22,'Joaquin','Hamal','1956-07-04','Non-binary','Speech Pathologist','HR',33981.32,'2013-03-24','jhamall@biglobe.ne.jp','251-335-2027','790=&',1),(23,'Cointon','Matterface','1980-01-24','Male','Pharmacist','HR',88803.50,'2015-06-12','cmatterfacem@opensource.org','791-744-7187','815>~,J',1),(24,'Clayton','Hail','1990-11-11','Male','Engineer IV','IT',106005.34,'2019-11-20','chailn@nsw.gov.au','815-815-9057','614*',1),(25,'Jeana','Miko','1968-08-27','Female','General Manager','Marketing',125137.33,'2017-04-29','jmikoo@cnn.com','176-813-4627','708?9B',1),(26,'Bailie','Chasier','1964-12-18','Male','Statistician IV','HR',122229.70,'2011-02-13','bchasierp@free.fr','486-170-9754','329*n%l',1),(27,'Ellyn','Plastow','1985-02-18','Agender','Payment Adjustment Coordinator','IT',89892.57,'2021-05-02','eplastowq@woothemes.com','893-170-4203','865%t',1),(28,'Jackie','Latore','1963-07-07','Female','Software Test Engineer III','IT',95901.57,'2015-08-18','jlatorer@yandex.ru','854-987-5189','984{s3',1),(29,'Derick','Pietruszka','1994-08-12','Male','Design Engineer','Marketing',135528.39,'2015-09-18','dpietruszkas@ed.gov','846-161-7792','454!',1),(30,'Frazier','Gamlyn','1988-07-17','Male','Actuary','HR',80890.83,'2010-08-29','fgamlynt@tinypic.com','842-751-6679','808<',1),(31,'Hilary','Stilldale','1968-02-23','Female','Civil Engineer','Finance',133049.25,'2010-08-19','hstilldaleu@cam.ac.uk','806-559-3774','716&/\"',1),(32,'Barth','Shotboult','1995-05-07','Male','VP Accounting','IT',142555.18,'2011-11-07','bshotboultv@wikimedia.org','228-798-1692','044{',1),(33,'Brit','Corness','1990-08-20','Female','Registered Nurse','IT',85710.66,'2011-08-02','bcornessw@ycombinator.com','483-583-9634','681&$y',1),(34,'Roth','Tildesley','1974-08-14','Male','Sales Associate','Marketing',85365.26,'2020-09-12','rtildesleyx@360.cn','359-214-7523','710$b',1),(35,'Glennie','Guiot','1971-12-19','Female','Electrical Engineer','Finance',54160.14,'2018-10-10','gguioty@qq.com','980-183-5214','618(9ji',1),(36,'Pascale','Hackleton','1982-12-09','Male','Environmental Specialist','Finance',81701.47,'2012-05-12','phackletonz@networkadvertising.org','761-186-1721','318_y%',1),(37,'Jeremias','Simonetto','1956-12-16','Male','Database Administrator III','IT',56158.66,'2019-02-16','jsimonetto10@ifeng.com','135-765-5296','675%}{',1),(38,'Frederick','Amberson','1958-05-18','Male','Community Outreach Specialist','Finance',147484.16,'2013-08-28','famberson11@cloudflare.com','985-743-3183','412,',1),(39,'Alfie','Cabera','1959-08-15','Male','Senior Editor','Finance',105968.46,'2012-08-28','acabera12@dyndns.org','541-440-9286','490(S4ID',1),(40,'Prudi','Stedson','1990-09-22','Female','Senior Sales Associate','IT',143289.36,'2010-11-09','pstedson13@wikimedia.org','305-799-0966','185?i0R',1),(41,'Whit','Smillie','1952-02-24','Male','Paralegal','IT',133678.81,'2018-07-26','wsmillie14@hc360.com','668-572-6929','029\'W\"~',1),(42,'Kym','Willoughway','1950-03-06','Female','Structural Engineer','Finance',88778.95,'2010-10-15','kwilloughway15@stanford.edu','963-458-6607','676.*qj',1),(43,'Myranda','Bride','1976-02-04','Female','Operator','HR',141390.23,'2020-06-28','mbride16@phoca.cz','612-127-7010','960+',1),(44,'Jennilee','Derl','1962-01-26','Female','Software Test Engineer III','IT',102476.94,'2019-05-25','jderl17@discuz.net','853-471-6296','378#y8',1),(45,'Lin','Dummigan','1972-06-13','Female','VP Accounting','IT',73384.59,'2016-08-18','ldummigan18@weebly.com','561-330-7465','656.JG_6',1),(46,'Miran','Tue','1967-08-17','Female','Clinical Specialist','Finance',42920.66,'2021-04-05','mtue19@arizona.edu','746-719-9185','154!',1),(47,'Sophi','Rudham','1973-11-20','Female','Recruiter','IT',71368.48,'2011-01-26','srudham1a@squarespace.com','128-967-1986','932(ig?',1),(48,'Waiter','Meach','1954-05-27','Male','Accountant II','Marketing',101022.29,'2019-05-10','wmeach1b@cnet.com','399-250-7740','307|klh{',1),(49,'Shayne','Pringuer','1999-03-29','Male','Nuclear Power Engineer','HR',48510.98,'2015-12-16','springuer1c@cyberchimps.com','113-464-9734','741\"WL|C',1),(50,'Sascha','Gamage','1982-04-01','Male','Database Administrator IV','Marketing',75412.34,'2014-02-26','sgamage1d@slashdot.org','630-640-2184','061|?G\'',1),(51,'ali','San','1967-09-18','Male','Human Resources','IT',31980.52,'2017-09-07','alisan@gmail.com','243-979-3929','5588',NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_`
--

DROP TABLE IF EXISTS `events_`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(255) DEFAULT NULL,
  `event_text` text,
  `event_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_`
--

LOCK TABLES `events_` WRITE;
/*!40000 ALTER TABLE `events_` DISABLE KEYS */;
INSERT INTO `events_` VALUES (1,'party','come to party this saturday','2024-12-26 20:30:34'),(2,'football','come to foootball this saturday','2024-12-02 20:30:34');
/*!40000 ALTER TABLE `events_` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(20) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'hammer',192),(2,'helmet',400),(3,'gloves',400),(4,'safety shoes',566),(5,'Welding Machine',288),(6,'Drill',335),(7,'truck',10),(8,'laptop',200),(9,'Desk',100),(15,'Chip',250);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_emp_id` int DEFAULT NULL,
  `to_emp_id` int DEFAULT NULL,
  `message_text` text,
  `is_read` tinyint(1) DEFAULT '0',
  `message_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `from_emp_id` (`from_emp_id`),
  KEY `to_emp_id` (`to_emp_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`from_emp_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`to_emp_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,2,'Hello, this is a test message!',0,'2024-11-26 20:30:34'),(2,2,3,'Reminder for the team meeting tomorrow.',0,'2024-11-26 20:30:34'),(3,3,4,'this is for testing11',0,'2024-11-27 00:06:46'),(4,3,5,'this is for testing11',0,'2024-11-27 00:06:46'),(5,3,6,'this is for testing11',0,'2024-11-27 00:06:46'),(6,3,7,'this is single message attempting',0,'2024-11-27 00:07:24'),(7,3,7,'this is single message attempting',0,'2024-11-27 00:18:44'),(10,3,8,'this is single message attempting',0,'2024-11-27 00:34:44');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pending_email`
--

DROP TABLE IF EXISTS `pending_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pending_email` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email_title` varchar(255) DEFAULT NULL,
  `email_description` text,
  `from_emp_id` int DEFAULT NULL,
  `to_emp_id` int DEFAULT NULL,
  `send_date` datetime DEFAULT NULL,
  `is_sent` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `from_emp_id` (`from_emp_id`),
  KEY `to_emp_id` (`to_emp_id`),
  CONSTRAINT `pending_email_ibfk_1` FOREIGN KEY (`from_emp_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `pending_email_ibfk_2` FOREIGN KEY (`to_emp_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pending_email`
--

LOCK TABLES `pending_email` WRITE;
/*!40000 ALTER TABLE `pending_email` DISABLE KEYS */;
INSERT INTO `pending_email` VALUES (1,'Dikkat!!','bugün saat 4 te buluşmaya ben de gelicem',2,1,'2024-11-28 15:30:00',1),(2,'toplantı','saat 5 te toplandı ofiste',2,1,'2024-11-29 15:30:00',0),(4,'toplantı','saat 5 te toplandı ofiste',1,2,'2024-10-29 15:30:00',1);
/*!40000 ALTER TABLE `pending_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `employee_items_with_names`
--

/*!50001 DROP VIEW IF EXISTS `employee_items_with_names`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `employee_items_with_names` AS select `e`.`employee_id` AS `employee_id`,`e`.`first_name` AS `first_name`,`e`.`last_name` AS `last_name`,`ei`.`item_id` AS `item_id`,`i`.`item_name` AS `item_name`,`ei`.`assignment_date` AS `assignment_date` from ((`employees` `e` left join `employee_items` `ei` on((`e`.`employee_id` = `ei`.`employee_id`))) left join `items` `i` on((`ei`.`item_id` = `i`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-28 16:24:33
