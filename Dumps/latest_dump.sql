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
-- Table structure for table `email`
--

DROP TABLE IF EXISTS `email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `email` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email_title` varchar(255) DEFAULT NULL,
  `email_description` text,
  `from_emp_id` int DEFAULT NULL,
  `to_emp_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_emp_id` (`from_emp_id`),
  KEY `to_emp_id` (`to_emp_id`),
  CONSTRAINT `email_ibfk_1` FOREIGN KEY (`from_emp_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `email_ibfk_2` FOREIGN KEY (`to_emp_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email`
--

LOCK TABLES `email` WRITE;
/*!40000 ALTER TABLE `email` DISABLE KEYS */;
INSERT INTO `email` VALUES (1,'vay kardeş','yarın buluşalım 6 da',1,1),(2,'DENEME-title','deneme123456-description',2,1),(3,'DENEMEv2-title','denev2-description',3,1);
/*!40000 ALTER TABLE `email` ENABLE KEYS */;
UNLOCK TABLES;

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
  `quantity` int DEFAULT '1',
  `assign_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`assign_id`),
  KEY `employee_items_ibfk_2` (`item_id`),
  KEY `employee_items_ibfk_1` (`employee_id`),
  CONSTRAINT `employee_items_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `employee_items_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=319 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_items`
--

LOCK TABLES `employee_items` WRITE;
/*!40000 ALTER TABLE `employee_items` DISABLE KEYS */;
INSERT INTO `employee_items` VALUES (2,1,'1967-11-16 19:35:06',1,1),(2,3,'1950-03-03 17:58:52',1,2),(2,3,'2014-12-07 03:17:59',1,3),(2,3,'2023-03-26 10:35:22',1,4),(2,4,'1913-10-02 16:05:59',1,5),(2,4,'2008-02-15 10:11:43',1,6),(2,5,'1932-02-28 05:48:46',1,7),(2,6,'1952-07-09 22:48:19',1,8),(2,6,'2013-04-11 23:14:29',1,9),(2,6,'2022-10-05 06:24:09',1,10),(3,1,'1976-12-13 23:05:54',1,11),(3,2,'2024-12-09 00:34:36',50,12),(3,2,'2024-12-13 22:54:22',50,13),(3,3,'1941-10-12 03:08:17',1,14),(3,3,'1969-07-15 15:34:44',1,15),(3,3,'2024-12-15 19:19:51',50,16),(3,3,'2024-12-15 19:21:13',50,17),(3,3,'2024-12-15 19:31:21',55,18),(3,4,'1920-09-11 19:56:13',1,19),(3,4,'1988-12-11 08:15:33',1,20),(3,6,'1901-05-19 08:57:34',1,21),(4,3,'1956-08-01 15:30:15',1,22),(4,3,'2004-09-02 08:07:59',1,23),(4,3,'2007-07-29 23:43:20',1,24),(4,4,'1971-03-21 08:43:55',1,25),(4,4,'1996-02-09 18:18:51',1,26),(4,5,'1960-09-18 00:35:36',1,27),(5,2,'1959-11-03 22:47:23',1,28),(5,3,'1932-05-24 11:10:46',1,29),(5,3,'2020-05-01 09:38:32',1,30),(5,5,'1931-07-13 10:44:59',1,31),(5,6,'1991-06-01 19:47:55',1,32),(6,1,'2008-07-19 16:27:45',1,33),(6,3,'1934-12-21 05:00:31',1,34),(6,3,'1977-01-08 19:27:43',1,35),(6,3,'1984-04-21 21:28:06',1,36),(6,4,'1912-03-12 22:36:04',1,37),(6,4,'2019-06-25 19:35:53',1,38),(6,5,'1922-01-30 02:30:38',1,39),(6,6,'1919-03-19 07:39:15',1,40),(6,6,'1994-08-19 08:51:40',1,41),(6,6,'2022-10-29 14:10:41',1,42),(7,1,'1920-06-03 16:50:42',1,43),(7,1,'1948-07-28 08:16:14',1,44),(7,1,'2005-04-25 06:24:27',1,45),(7,2,'1921-07-20 13:50:43',1,46),(7,2,'1967-01-20 14:28:27',1,47),(7,2,'1974-05-21 00:33:53',1,48),(7,3,'1903-03-10 07:52:07',1,49),(7,3,'1991-12-31 11:57:48',1,50),(7,6,'1920-01-03 05:04:15',1,51),(7,6,'1928-07-12 01:52:39',1,52),(8,2,'1967-01-29 00:03:00',1,53),(8,5,'1960-02-11 21:54:01',1,54),(9,1,'1948-12-09 16:46:26',1,55),(9,1,'1961-07-26 23:42:38',1,56),(9,1,'1985-07-04 04:09:55',1,57),(9,2,'1930-04-04 22:34:44',1,58),(9,2,'1962-08-20 23:56:22',1,59),(9,3,'1961-03-19 14:36:48',1,60),(9,4,'1920-11-02 13:18:26',1,61),(9,6,'1982-07-17 21:40:50',1,62),(10,3,'1954-01-08 11:18:53',1,63),(10,3,'1993-01-24 17:19:01',1,64),(10,4,'1973-02-11 16:06:03',1,65),(10,4,'2019-10-14 05:41:13',1,66),(10,5,'1967-02-12 02:33:35',1,67),(11,3,'1954-12-18 10:23:56',1,68),(11,4,'1936-05-09 14:38:49',1,69),(12,1,'1960-02-27 19:21:41',1,70),(12,1,'1993-09-23 10:10:21',1,71),(12,2,'2017-07-26 14:31:18',1,72),(12,3,'1910-01-12 04:19:51',1,73),(12,3,'1956-03-09 05:44:23',1,74),(12,3,'1961-06-21 05:20:25',1,75),(13,2,'1928-10-12 02:56:37',1,76),(13,3,'1971-12-31 08:23:12',1,77),(13,3,'1984-04-28 06:49:20',1,78),(13,4,'1965-11-28 01:59:49',1,79),(13,5,'1933-02-06 12:17:42',1,80),(13,5,'1963-10-22 06:41:58',1,81),(14,3,'1912-02-10 07:56:04',1,82),(14,3,'2017-02-17 20:56:22',1,83),(14,4,'1938-12-22 05:41:03',1,84),(14,4,'1960-10-11 18:34:32',1,85),(15,1,'1971-12-06 13:36:46',1,86),(15,2,'1920-12-07 21:18:40',1,87),(15,2,'1922-05-31 02:24:14',1,88),(15,5,'1991-10-10 05:01:30',1,89),(16,1,'1934-04-01 16:23:53',1,90),(16,2,'1966-08-29 18:26:51',1,91),(16,2,'1972-05-03 02:38:37',1,92),(16,3,'1920-09-27 16:10:01',1,93),(16,3,'2014-07-10 01:07:40',1,94),(16,4,'2009-02-25 16:57:54',1,95),(16,6,'1956-02-15 08:19:01',1,96),(16,6,'2009-08-10 14:30:45',1,97),(16,6,'2022-06-29 14:01:54',1,98),(17,1,'1947-12-14 10:47:19',1,99),(17,2,'1941-07-18 10:26:26',1,100),(17,2,'2016-02-11 11:55:03',1,101),(17,4,'2008-08-08 23:10:39',1,102),(17,4,'2017-02-24 08:41:18',1,103),(17,6,'1989-01-04 17:24:33',1,104),(18,2,'2023-10-04 06:05:12',1,105),(18,3,'1902-08-27 20:16:39',1,106),(18,3,'1931-08-10 18:34:43',1,107),(18,3,'1960-07-19 07:14:48',1,108),(18,3,'1996-05-25 01:48:17',1,109),(18,4,'1911-04-28 00:13:48',1,110),(18,5,'1956-11-28 10:55:01',1,111),(18,6,'1989-09-20 16:46:03',1,112),(18,6,'2007-11-12 10:18:18',1,113),(19,2,'1918-07-11 08:21:29',1,114),(19,3,'2022-12-28 05:22:15',1,115),(19,5,'1903-06-19 10:01:56',1,116),(19,6,'1934-12-23 19:49:34',1,117),(20,1,'2020-09-14 03:34:11',1,118),(20,3,'2023-04-13 09:33:54',1,119),(20,6,'1938-08-06 01:13:00',1,120),(20,6,'1942-04-05 09:44:15',1,121),(20,6,'1964-06-01 23:25:17',1,122),(21,2,'1928-08-06 06:22:16',1,123),(21,3,'2001-06-17 02:12:30',1,124),(21,4,'1986-03-03 05:35:33',1,125),(21,5,'1921-01-08 15:23:34',1,126),(21,5,'1995-07-28 23:46:13',1,127),(22,1,'1902-03-20 12:39:55',1,128),(22,1,'1985-10-22 13:15:17',1,129),(22,1,'2014-07-07 17:15:13',1,130),(22,2,'1942-09-08 11:31:48',1,131),(22,2,'1994-05-24 14:49:26',1,132),(22,3,'1950-12-30 17:04:18',1,133),(22,3,'1964-03-04 06:03:24',1,134),(22,4,'1968-05-17 11:35:53',1,135),(22,5,'1952-08-26 02:59:16',1,136),(23,2,'2007-10-07 01:12:55',1,137),(23,5,'1919-09-20 05:40:59',1,138),(23,5,'1957-10-22 01:54:27',1,139),(24,1,'1968-05-03 01:15:14',1,140),(24,1,'2018-12-27 14:00:53',1,141),(24,2,'1987-09-12 00:57:25',1,142),(24,3,'1959-03-25 03:00:21',1,143),(24,5,'2002-09-24 01:48:17',1,144),(24,6,'2011-11-25 09:04:32',1,145),(25,1,'1901-05-07 07:38:37',1,146),(25,3,'1944-02-05 03:55:20',1,147),(25,3,'1998-12-28 01:55:15',1,148),(25,4,'1929-10-30 05:02:43',1,149),(25,5,'1930-02-14 08:03:06',1,150),(26,1,'1919-08-05 01:32:28',1,151),(26,2,'1931-05-09 10:02:17',1,152),(26,2,'1999-02-15 13:21:26',1,153),(26,3,'1981-10-30 01:37:01',1,154),(27,1,'1903-04-09 15:42:35',1,155),(27,1,'1926-10-20 16:32:47',1,156),(27,1,'2001-08-16 07:57:41',1,157),(27,3,'1956-07-14 13:31:44',1,158),(27,3,'1969-07-15 15:34:44',1,159),(27,6,'1982-03-28 19:57:31',1,160),(28,1,'1909-01-24 04:41:21',1,161),(28,4,'1920-04-30 00:43:15',1,162),(28,4,'1974-10-18 04:34:59',1,163),(28,6,'1900-08-13 09:19:23',1,164),(29,2,'1959-03-09 22:11:14',1,165),(29,2,'1998-07-14 14:02:07',1,166),(29,3,'1984-09-16 11:15:37',1,167),(29,4,'1901-05-13 21:46:26',1,168),(29,5,'1953-09-02 05:03:36',1,169),(29,6,'1964-10-09 21:58:43',1,170),(29,6,'2005-10-04 00:09:48',1,171),(30,4,'1908-01-04 01:07:55',1,172),(30,4,'1915-07-24 18:10:16',1,173),(30,4,'2005-03-16 00:56:15',1,174),(30,5,'1945-11-15 02:20:28',1,175),(30,6,'1988-11-08 11:06:41',1,176),(31,1,'1906-04-19 22:24:41',1,177),(31,1,'1979-04-15 02:03:53',1,178),(31,2,'1923-06-18 01:43:31',1,179),(31,3,'1955-12-01 17:58:38',1,180),(31,4,'1923-07-29 18:37:59',1,181),(31,4,'1977-04-12 05:55:44',1,182),(31,6,'2020-05-14 19:57:37',1,183),(32,1,'1963-10-01 17:51:33',1,184),(32,3,'1977-05-03 12:59:39',1,185),(32,3,'1980-11-25 14:45:36',1,186),(32,6,'1902-12-29 02:32:44',1,187),(33,1,'1937-02-26 12:24:00',1,188),(33,1,'1944-06-07 06:36:08',1,189),(33,1,'1959-05-29 23:53:53',1,190),(33,3,'1989-07-11 17:09:29',1,191),(33,3,'2011-12-26 00:29:53',1,192),(33,5,'1974-04-28 14:56:58',1,193),(33,5,'1983-07-27 19:15:09',1,194),(33,6,'1949-04-17 17:17:05',1,195),(34,2,'1915-11-10 01:09:58',1,196),(34,2,'1999-11-12 17:07:41',1,197),(34,4,'1980-07-06 01:12:28',1,198),(34,5,'1972-09-21 21:05:21',1,199),(35,1,'1936-10-26 17:04:02',1,200),(35,1,'1964-08-10 16:11:24',1,201),(35,1,'1992-10-01 20:33:50',1,202),(35,2,'1914-01-07 13:01:40',1,203),(35,2,'2003-12-21 14:14:55',1,204),(35,6,'1925-03-26 19:30:32',1,205),(35,6,'1952-10-04 14:47:22',1,206),(36,2,'1939-03-28 03:15:41',1,207),(36,3,'2011-12-21 01:34:40',1,208),(36,4,'1915-06-06 16:02:10',1,209),(36,6,'1932-05-31 21:25:38',1,210),(36,6,'1942-02-04 11:52:49',1,211),(37,2,'1905-10-31 07:31:44',1,212),(37,3,'1950-01-19 00:37:51',1,213),(37,4,'1906-11-29 19:16:16',1,214),(37,4,'1971-04-14 21:38:57',1,215),(37,5,'1951-12-26 12:58:41',1,216),(37,5,'2015-08-20 08:04:00',1,217),(37,6,'1960-07-18 00:07:14',1,218),(37,6,'2009-11-04 08:55:40',1,219),(37,6,'2024-03-03 04:53:14',1,220),(38,1,'1954-07-02 14:23:02',1,221),(38,1,'1989-03-28 21:14:08',1,222),(38,3,'1950-03-04 04:30:25',1,223),(38,3,'1998-05-02 11:35:16',1,224),(38,4,'1946-09-01 08:58:01',1,225),(38,5,'1946-12-03 13:32:39',1,226),(39,3,'1954-05-16 14:09:00',1,227),(40,1,'1977-05-07 15:33:02',1,228),(40,2,'1952-05-07 03:16:44',1,229),(40,2,'1985-06-25 14:12:39',1,230),(40,2,'2022-11-06 06:53:00',1,231),(40,3,'1964-10-31 09:19:32',1,232),(40,6,'1946-03-21 00:07:58',1,233),(41,1,'1932-01-12 22:34:38',1,234),(41,2,'1901-09-22 13:42:15',1,235),(41,2,'1994-07-17 17:33:47',1,236),(41,3,'1991-12-11 05:29:45',1,237),(41,4,'1956-01-15 20:55:15',1,238),(41,5,'1911-03-17 02:54:57',1,239),(41,6,'2014-08-23 09:05:33',1,240),(42,1,'1905-09-03 15:49:39',1,241),(42,1,'1967-11-16 19:35:06',1,242),(42,2,'1922-07-12 07:22:42',1,243),(42,2,'1977-06-28 09:55:29',1,244),(42,3,'2015-08-13 03:15:30',1,245),(42,4,'1974-12-25 11:35:50',1,246),(43,1,'1947-03-16 15:36:38',1,247),(43,2,'1978-07-02 16:57:55',1,248),(43,2,'1981-06-07 17:02:09',1,249),(43,3,'1910-08-16 23:57:04',1,250),(43,3,'2014-10-29 20:53:04',1,251),(43,3,'2017-04-16 08:33:05',1,252),(43,3,'2020-05-01 09:38:32',1,253),(43,4,'1912-09-17 02:59:35',1,254),(43,5,'1928-02-02 00:48:44',1,255),(43,5,'2011-06-16 22:28:46',1,256),(43,5,'2017-08-03 00:00:51',1,257),(44,1,'2011-12-24 10:59:57',1,258),(44,2,'1975-02-20 00:19:13',1,259),(44,3,'1982-10-14 21:12:47',1,260),(44,4,'1921-05-01 14:17:45',1,261),(44,5,'1927-04-12 17:27:47',1,262),(44,6,'1937-07-30 22:08:42',1,263),(44,6,'1963-06-24 09:12:15',1,264),(44,6,'1985-04-26 13:27:41',1,265),(44,6,'1995-07-15 23:53:53',1,266),(45,3,'1986-12-04 09:34:20',1,267),(45,4,'1995-10-06 04:51:11',1,268),(45,6,'2012-07-10 21:33:06',1,269),(46,1,'1918-12-11 12:52:34',1,270),(46,2,'1940-10-25 03:14:08',1,271),(46,2,'1955-07-19 00:57:22',1,272),(46,3,'1919-10-14 14:45:16',1,273),(46,3,'1951-03-20 12:56:43',1,274),(46,3,'1973-01-25 00:11:32',1,275),(46,5,'1908-02-10 01:22:40',1,276),(47,1,'1907-09-29 07:12:47',1,277),(47,2,'1915-10-23 19:40:28',1,278),(47,2,'1981-03-01 15:15:38',1,279),(47,2,'2007-10-04 18:44:00',1,280),(47,3,'1948-08-02 21:22:09',1,281),(47,5,'1916-12-26 06:04:19',1,282),(47,5,'1961-06-20 21:20:44',1,283),(47,5,'1994-12-14 10:22:52',1,284),(47,6,'1969-09-10 17:29:19',1,285),(48,1,'1903-06-15 21:20:39',1,286),(48,2,'1989-11-13 20:55:48',1,287),(48,4,'1900-03-14 02:46:06',1,288),(48,4,'1949-07-12 18:20:25',1,289),(48,4,'1996-02-09 18:18:51',1,290),(48,5,'1901-12-21 16:20:43',1,291),(48,6,'1935-10-20 09:56:21',1,292),(48,6,'1946-09-18 22:21:02',1,293),(49,2,'2016-05-01 01:42:33',1,294),(49,2,'2019-03-12 18:36:38',1,295),(49,5,'1963-12-08 01:16:42',1,296),(49,5,'1969-02-23 07:48:05',1,297),(49,5,'1995-07-04 12:44:09',1,298),(49,6,'1929-03-26 14:37:35',1,299),(49,6,'1983-11-29 07:55:05',1,300),(50,1,'1923-11-25 01:19:07',1,301),(50,1,'1999-04-02 17:52:48',1,302),(50,3,'2001-10-01 22:20:11',1,303),(50,4,'1965-08-30 04:33:45',1,304),(50,5,'1940-02-23 04:56:25',1,305),(50,5,'1954-06-14 13:55:43',1,306),(1,3,'2024-12-15 20:07:12',75,307),(2,1,'2024-12-15 21:03:25',50,308),(4,1,'2024-12-15 21:03:53',50,309),(4,1,'2024-12-15 22:05:36',50,310),(5,1,'2024-12-15 22:05:45',5,311),(2,2,'2024-12-17 00:49:19',2,312),(2,3,'2024-12-17 00:49:19',2,313),(3,2,'2024-12-17 00:49:19',2,314),(3,3,'2024-12-17 00:49:19',2,315),(3,2,'2024-12-19 21:28:39',3,316),(3,1,'2024-12-19 21:28:59',5,317),(3,2,'2024-12-19 21:28:59',5,318);
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
 1 AS `quantity`,
 1 AS `assign_id`,
 1 AS `assignment_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `employee_leaves`
--

DROP TABLE IF EXISTS `employee_leaves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_leaves` (
  `leave_request_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `status_of_leave_asking` enum('Pending','Accepted','Rejected') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'Pending',
  `request_date` date DEFAULT NULL,
  `approved_by` int DEFAULT NULL,
  `answer_date` date DEFAULT NULL,
  `leave_type` enum('Annual Leave','Health Leave','Unpaid Leave','Excuse Leave') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `total_dates` int NOT NULL,
  `desc_request` text,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`leave_request_id`),
  KEY `employee_leaves_employees_FK` (`employee_id`),
  CONSTRAINT `employee_leaves_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_leaves`
--

LOCK TABLES `employee_leaves` WRITE;
/*!40000 ALTER TABLE `employee_leaves` DISABLE KEYS */;
INSERT INTO `employee_leaves` VALUES (28,23,'Accepted','2022-03-28',23,'2021-12-29','Unpaid Leave','2021-11-17','2021-03-12',26,'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.\n\nMorbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.\n\nFusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.','2020-02-24 12:47:36'),(29,10,'Accepted','2021-11-03',15,'2022-09-30','Unpaid Leave','2022-11-25','2020-10-30',24,'In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.\n\nSuspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.','2022-05-19 14:25:12'),(30,23,'Accepted','2022-01-23',15,'2020-01-06','Health Leave','2021-01-24','2020-01-17',5,'In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.\n\nSuspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.','2021-06-22 03:19:46'),(31,20,'Accepted','2022-01-22',26,'2021-05-20','Unpaid Leave','2022-07-12','2021-03-26',13,'Sed ante. Vivamus tortor. Duis mattis egestas metus.','2022-05-09 01:34:03'),(32,29,'Accepted','2022-01-08',10,'2022-06-15','Annual Leave','2021-12-12','2020-08-19',28,'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.\n\nMaecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.','2020-08-06 07:22:42'),(33,5,'Accepted','2020-05-24',25,'2020-11-02','Unpaid Leave','2022-05-27','2020-08-25',5,'In congue. Etiam justo. Etiam pretium iaculis justo.\n\nIn hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.','2020-07-11 04:29:14'),(34,19,'Accepted','2020-09-04',20,'2021-10-28','Health Leave','2021-12-31','2020-06-20',6,'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.\n\nDuis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.','2020-09-25 14:13:06'),(35,25,'Accepted','2022-07-31',30,'2022-05-10','Excuse Leave','2020-11-08','2020-03-10',4,'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.\n\nMorbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.','2022-02-18 17:07:23'),(36,15,'Accepted','2020-08-06',26,'2020-08-08','Unpaid Leave','2022-05-01','2022-04-19',9,'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.','2022-06-13 12:21:27'),(37,24,'Accepted','2022-07-18',28,'2022-11-30','Unpaid Leave','2022-05-14','2021-07-03',29,'In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.\n\nAliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.\n\nSed ante. Vivamus tortor. Duis mattis egestas metus.','2021-03-06 10:31:28'),(38,30,'Accepted','2020-06-30',5,'2022-07-16','Unpaid Leave','2021-02-02','2021-08-25',27,'Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.','2021-11-05 15:19:10'),(39,1,'Accepted','2021-07-24',21,'2022-01-10','Unpaid Leave','2020-12-12','2022-09-03',25,'Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.','2022-07-21 19:42:40'),(40,18,'Accepted','2021-02-04',1,'2022-04-10','Excuse Leave','2022-05-16','2022-04-29',24,'Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.\n\nCurabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.','2020-08-15 05:14:24'),(41,4,'Accepted','2020-01-26',7,'2022-11-10','Annual Leave','2020-06-17','2022-11-25',9,'Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.','2021-01-02 12:32:33'),(42,25,'Accepted','2020-02-24',2,'2020-08-01','Annual Leave','2020-11-29','2021-11-27',3,'Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.\n\nIn hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.\n\nAliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.','2022-07-24 13:04:19'),(43,24,'Accepted','2020-12-19',21,'2022-11-07','Unpaid Leave','2022-11-09','2022-06-13',15,'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.\n\nMaecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.\n\nCurabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.','2022-07-10 21:48:52'),(44,3,'Accepted','2020-07-17',22,'2022-05-30','Excuse Leave','2020-01-24','2022-08-20',14,'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.\n\nDuis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.\n\nIn sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.','2022-04-26 09:54:33'),(45,7,'Accepted','2022-03-14',5,'2021-08-05','Unpaid Leave','2020-11-23','2021-01-04',11,'Sed ante. Vivamus tortor. Duis mattis egestas metus.\n\nAenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.\n\nQuisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.','2020-09-09 09:58:29'),(46,27,'Accepted','2022-03-02',16,'2020-12-19','Health Leave','2020-07-16','2020-04-29',29,'Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.\n\nQuisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.\n\nVestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.','2021-08-08 21:29:16'),(47,18,'Accepted','2020-06-24',17,'2021-12-10','Health Leave','2020-11-27','2022-02-09',14,'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.\n\nMaecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.','2021-03-08 07:40:10'),(48,30,'Accepted','2021-08-24',20,'2022-05-11','Health Leave','2020-06-01','2021-11-02',30,'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nEtiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.','2020-11-04 04:29:06'),(49,21,'Accepted','2020-12-21',15,'2021-12-23','Unpaid Leave','2021-12-10','2020-03-04',18,'Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.','2020-05-27 11:30:45'),(50,29,'Accepted','2020-02-06',4,'2020-07-16','Unpaid Leave','2021-07-05','2021-10-14',8,'Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.','2021-07-22 17:24:51'),(51,15,'Accepted','2020-01-24',23,'2022-04-29','Health Leave','2021-11-27','2021-05-10',7,'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.\n\nPraesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.\n\nCras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.','2020-11-02 07:43:55'),(52,22,'Accepted','2021-07-19',13,'2021-12-15','Annual Leave','2021-12-25','2022-11-22',10,'Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.\n\nPraesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.\n\nMorbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.','2021-02-12 17:03:55'),(53,14,'Accepted','2021-03-10',26,'2021-07-18','Unpaid Leave','2020-04-11','2022-02-19',20,'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.\n\nMaecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.\n\nCurabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.','2020-07-10 15:20:36'),(54,3,'Accepted','2021-08-17',30,'2021-10-09','Unpaid Leave','2020-12-31','2020-06-09',27,'Sed ante. Vivamus tortor. Duis mattis egestas metus.\n\nAenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.','2022-09-05 00:30:26'),(55,25,'Accepted','2022-03-14',24,'2022-11-27','Annual Leave','2021-11-11','2022-02-06',12,'Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.\n\nCras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.','2021-08-03 14:03:11'),(56,3,'Accepted','2022-04-01',18,'2020-11-07','Excuse Leave','2022-05-04','2020-09-22',24,'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.\n\nPraesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.\n\nCras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.','2020-01-01 04:10:45'),(57,23,'Accepted','2020-12-16',23,'2020-07-19','Unpaid Leave','2021-11-02','2022-11-15',27,'Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.\n\nNullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.','2020-10-02 06:51:45'),(58,26,'Pending','2021-07-03',16,'2022-11-11','Unpaid Leave','2022-10-14','2020-04-04',14,'Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.\n\nCum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nEtiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.','2020-08-10 12:31:59'),(59,15,'Pending','2021-08-16',15,'2021-11-02','Unpaid Leave','2022-10-06','2020-04-25',29,'Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.\n\nIn hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.\n\nAliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.','2021-03-15 10:44:32'),(60,29,'Pending','2020-05-12',5,'2021-10-03','Unpaid Leave','2022-01-30','2021-06-08',24,'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.\n\nMorbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.','2022-11-05 01:32:20'),(61,20,'Pending','2022-01-22',26,'2021-05-20','Unpaid Leave','2022-07-12','2021-03-26',13,'Sed ante. Vivamus tortor. Duis mattis egestas metus.','2022-05-09 01:34:03');
/*!40000 ALTER TABLE `employee_leaves` ENABLE KEYS */;
UNLOCK TABLES;

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
  `is_active` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Alvin','Fernier','1967-09-18','Male','Human resources','IT',40000.00,'2017-09-07','hikmetcatak99@gmail.com','243-979-3929','123',1),(2,'Hikmet','Catak','1963-11-18','Male','Human resources','engineer',41564.14,'2012-07-18','hikmetcatak26@gmail.com','829-856-3658','5858',1),(3,'Fevzi','Fid','1996-03-11','Male','Engineer','IT',888888.10,'2014-08-11','bbeisley2@bloomberg.com','574-899-5588','728=xy{X',1),(4,'Sibylle','Houtby','1965-11-12','Female','Senior Cost Accountant','IT',70327.65,'2017-09-24','shoutby3@slate.com','773-887-2470','409_8`',1),(5,'Bail','Frere','1960-08-06','Male','Data Coordinator','Finance',66197.04,'2014-10-01','bfrere4@ucla.edu','576-305-4297','150{d',0),(6,'Bondie','Astbury','1952-08-10','Male','VP Marketing','IT',80845.46,'2021-02-04','bastbury5@dedecms.com','176-693-2633','907$_WZ4',0),(7,'nikita','nikitaa','1965-05-01','female','Assistant ','IT',5555.56,'2011-08-02','mkruschev6@ibm.com','167-124-1111','650*0',0),(8,'ömer','faruk','1988-08-18','Male','engineer','Finance',44444.00,'2012-07-28','ttomasz7@usnews.com','555-899-3148','8585',1),(9,'Corilla','Cornejo','1978-11-14','Female','Operator','IT',122954.69,'2018-08-17','ccornejo8@e-recht24.de','439-323-9275','848%e',1),(10,'Felipa','Helder','1998-09-20','Female','Biostatistician III','HR',43567.00,'2021-12-24','fhelder9@slashdot.org','771-921-9341','007,|M',1),(11,'Erik','Aust','1999-02-04','Male','Nurse Practicioner','Finance',42007.45,'2012-10-13','eausta@google.ca','588-526-2977','330(Fj!_',0),(12,'Mallory','Dodimead','1964-01-01','Male','Database Administrator III','HR',52762.67,'2018-03-11','mdodimeadb@washington.edu','143-595-9744','149`D',0),(13,'Trina','Boig','1972-05-08','Female','VP Product Management','IT',127888.09,'2013-01-02','tboigc@slate.com','740-247-6386','450$ges$',0),(14,'Neill','Swannick','1955-06-02','Male','Senior Developer','HR',108875.91,'2013-10-31','nswannickd@biblegateway.com','549-873-7290','279<g>J',1),(15,'Brynne','Rorke','1997-04-10','Female','Cost Accountant','Marketing',98048.83,'2017-09-20','brorkee@latimes.com','332-403-3897','462}l',1),(16,'Elwood','Crandon','1989-11-17','Male','Food Chemist','IT',66636.20,'2019-03-10','ecrandonf@mac.com','404-549-5846','436.&+kC',1),(17,'Eddie','Hutcheon','1971-09-08','Female','Statistician I','Finance',38029.90,'2012-03-02','ehutcheong@sitemeter.com','716-204-5986','852\"l',1),(18,'Adriaens','Tulk','1969-09-12','Female','Professor','Finance',127113.96,'2019-11-21','atulkh@washington.edu','853-213-2079','683~LIw',1),(19,'Ruth','Peile','1986-08-13','Female','Associate Professor','Finance',54493.58,'2015-10-04','rpeilei@simplemachines.org','810-894-1351','978!*iu',1),(20,'Aggie','Weedall','1979-12-13','Female','Software Engineer IV','IT',126614.33,'2015-02-24','aweedallj@chron.com','443-657-1371','030/L7Xg',1),(21,'Artur','Reah','1999-01-18','Male','VP Product Management','IT',61834.09,'2018-01-18','areahk@uol.com.br','602-429-5498','855_5Pq2',1),(22,'Joaquin','Hamal','1956-07-04','Non-binary','Speech Pathologist','HR',33981.32,'2013-03-24','jhamall@biglobe.ne.jp','251-335-2027','790=&',1),(23,'Cointon','Matterface','1980-01-24','Male','Pharmacist','HR',88803.50,'2015-06-12','cmatterfacem@opensource.org','791-744-7187','815>~,J',1),(24,'Clayton','Hail','1990-11-11','Male','Engineer IV','IT',106005.34,'2019-11-20','chailn@nsw.gov.au','815-815-9057','614*',1),(25,'Jeana','Miko','1968-08-27','Female','General Manager','Marketing',125137.33,'2017-04-29','jmikoo@cnn.com','176-813-4627','708?9B',1),(26,'Bailie','Chasier','1964-12-18','Male','Statistician IV','HR',122229.70,'2011-02-13','bchasierp@free.fr','486-170-9754','329*n%l',1),(27,'Ellyn','Plastow','1985-02-18','Agender','Payment Adjustment Coordinator','IT',89892.57,'2021-05-02','eplastowq@woothemes.com','893-170-4203','865%t',1),(28,'Jackie','Latore','1963-07-07','Female','Software Test Engineer III','IT',95901.57,'2015-08-18','jlatorer@yandex.ru','854-987-5189','984{s3',1),(29,'Derick','Pietruszka','1994-08-12','Male','Design Engineer','Marketing',135528.39,'2015-09-18','dpietruszkas@ed.gov','846-161-7792','454!',1),(30,'Frazier','Gamlyn','1988-07-17','Male','Actuary','HR',80890.83,'2010-08-29','fgamlynt@tinypic.com','842-751-6679','808<',1),(31,'Hilary','Stilldale','1968-02-23','Female','Civil Engineer','Finance',133049.25,'2010-08-19','hstilldaleu@cam.ac.uk','806-559-3774','716&/\"',1),(32,'Barth','Shotboult','1995-05-07','Male','VP Accounting','IT',142555.18,'2011-11-07','bshotboultv@wikimedia.org','228-798-1692','044{',1),(33,'Brit','Corness','1990-08-20','Female','Registered Nurse','IT',85710.66,'2011-08-02','bcornessw@ycombinator.com','483-583-9634','681&$y',1),(34,'Roth','Tildesley','1974-08-14','Male','Sales Associate','Marketing',85365.26,'2020-09-12','rtildesleyx@360.cn','359-214-7523','710$b',1),(35,'Glennie','Guiot','1971-12-19','Female','Electrical Engineer','Finance',54160.14,'2018-10-10','gguioty@qq.com','980-183-5214','618(9ji',1),(36,'Pascale','Hackleton','1982-12-09','Male','Environmental Specialist','Finance',81701.47,'2012-05-12','phackletonz@networkadvertising.org','761-186-1721','318_y%',1),(37,'Jeremias','Simonetto','1956-12-16','Male','Database Administrator III','IT',56158.66,'2019-02-16','jsimonetto10@ifeng.com','135-765-5296','675%}{',1),(38,'Frederick','Amberson','1958-05-18','Male','Community Outreach Specialist','Finance',147484.16,'2013-08-28','famberson11@cloudflare.com','985-743-3183','412,',1),(39,'Alfie','Cabera','1959-08-15','Male','Senior Editor','Finance',105968.46,'2012-08-28','acabera12@dyndns.org','541-440-9286','490(S4ID',1),(40,'Prudi','Stedson','1990-09-22','Female','Senior Sales Associate','IT',143289.36,'2010-11-09','pstedson13@wikimedia.org','305-799-0966','185?i0R',1),(41,'Whit','Smillie','1952-02-24','Male','Paralegal','IT',133678.81,'2018-07-26','wsmillie14@hc360.com','668-572-6929','029\'W\"~',1),(42,'Kym','Willoughway','1950-03-06','Female','Structural Engineer','Finance',88778.95,'2010-10-15','kwilloughway15@stanford.edu','963-458-6607','676.*qj',1),(43,'Myranda','Bride','1976-02-04','Female','Operator','HR',141390.23,'2020-06-28','mbride16@phoca.cz','612-127-7010','960+',1),(44,'Jennilee','Derl','1962-01-26','Female','Software Test Engineer III','IT',102476.94,'2019-05-25','jderl17@discuz.net','853-471-6296','378#y8',1),(45,'Lin','Dummigan','1972-06-13','Female','VP Accounting','IT',73384.59,'2016-08-18','ldummigan18@weebly.com','561-330-7465','656.JG_6',1),(46,'Miran','Tue','1967-08-17','Female','Clinical Specialist','Finance',42920.66,'2021-04-05','mtue19@arizona.edu','746-719-9185','154!',1),(47,'Sophi','Rudham','1973-11-20','Female','Recruiter','IT',71368.48,'2011-01-26','srudham1a@squarespace.com','128-967-1986','932(ig?',1),(48,'Waiter','Meach','1954-05-27','Male','Accountant II','Marketing',101022.29,'2019-05-10','wmeach1b@cnet.com','399-250-7740','307|klh{',1),(49,'Shayne','Pringuer','1999-03-29','Male','Nuclear Power Engineer','HR',48510.98,'2015-12-16','springuer1c@cyberchimps.com','113-464-9734','741\"WL|C',1),(50,'Sascha','Gamage','1982-04-01','Male','Database Administrator IV','Marketing',75412.34,'2014-02-26','sgamage1d@slashdot.org','630-640-2184','061|?G\'',1),(51,'ali','San','1967-09-18','Male','Human Resources','IT',31980.52,'2017-09-07','alisan@gmail.com','243-979-3929','5588',1),(52,'ali','Sai','1967-03-18','Male','Human Resources','IT',31980.52,'2017-09-07','ali@gmail.com','243-979-3929','5858',1),(53,'ali','ali','1967-03-18','Male','Human Resources','IT',31980.52,'2017-09-07','aliali@gmail.com','243-979-3929','ali',1),(54,'emin','emin','2005-04-15','Male','engineer','it',555555.00,'2024-12-17','email','+213(5555)-555-555','me967lDx',1),(55,'user','user','2008-04-15','Male','c+','software',7878.00,'2024-12-17','23123123@gmail.com','+213(5555)-555-555','wcCppapf',1),(56,'asd','dsa','1900-01-01','Male','software','it',111111.00,'2024-12-17','hkmt@gmail.com','+9055345454727','moiftdJZ',1),(57,'asdsdsa','sdsadsa','1900-01-01','Male','software','it',111111.00,'2024-12-17','hkmt@gmail.com','+9055345454727','iVr4rWJH',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_`
--

LOCK TABLES `events_` WRITE;
/*!40000 ALTER TABLE `events_` DISABLE KEYS */;
INSERT INTO `events_` VALUES (1,'party','come to party this saturday','2024-12-26 20:30:34'),(2,'football','come to foootball this saturday','2024-12-02 20:30:34'),(3,'fun','Eğlence var saat 20','2024-08-11 00:00:00'),(4,'fun','Eğlence var saat 3','2025-08-11 00:00:00');
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
INSERT INTO `items` VALUES (1,'hammer',175),(2,'helmet',288),(3,'gloves',66),(4,'safety shoes',567),(5,'Welding Machine',289),(6,'Drill',335),(7,'truck',10),(8,'laptop',200),(9,'Desk',100),(15,'Chip',250);
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
  `subject` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_emp_id` (`from_emp_id`),
  KEY `to_emp_id` (`to_emp_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`from_emp_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`to_emp_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,2,'Hello, this is a test message!',1,'2024-11-26 20:30:34',NULL),(2,2,3,'Reminder for the team meeting tomorrow.',0,'2024-11-26 20:30:34',NULL),(3,3,4,'this is for testing11',0,'2024-11-27 00:06:46',NULL),(4,3,5,'this is for testing11',0,'2024-11-27 00:06:46',NULL),(5,3,6,'this is for testing11',0,'2024-11-27 00:06:46',NULL),(6,3,7,'this is single message attempting',0,'2024-11-27 00:07:24',NULL),(7,3,7,'this is single message attempting',0,'2024-11-27 00:18:44',NULL),(10,3,8,'this is single message attempting',0,'2024-11-27 00:34:44',NULL),(19,3,8,'this is single message attempting2',0,'2024-12-03 00:56:01','acil!!'),(20,3,4,'this is single message attempting2',0,'2024-12-03 00:56:01','acil!!'),(21,1,8,'toplantı 7da',0,'2024-12-16 23:56:51','toplantı'),(22,1,8,'toplantı 7da',0,'2024-12-16 23:57:00','toplantı'),(23,1,2,'6 da gel',1,'2024-12-16 23:58:08','gel'),(24,2,1,'come to office',0,'2024-12-17 00:14:15','warning'),(25,2,1,'5te',0,'2024-12-17 00:40:22',''),(26,2,3,'5te',0,'2024-12-17 00:40:22',''),(27,2,4,'5te',0,'2024-12-17 00:40:22',''),(28,2,5,'5te',0,'2024-12-17 00:40:22','');
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
INSERT INTO `pending_email` VALUES (1,'Dikkat!!','bugün saat 4 te buluşmaya ben de gelicem',2,1,'2024-11-28 15:30:00',1),(2,'toplantı','saat 5 te toplandı ofiste',2,1,'2024-11-29 15:30:00',1),(4,'toplantı','saat 5 te toplandı ofiste',1,2,'2024-10-29 15:30:00',1);
/*!40000 ALTER TABLE `pending_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `special_requests`
--

DROP TABLE IF EXISTS `special_requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `special_requests` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `request_type` enum('Advance','Salary Increase','Payback','Other') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `request_amount` decimal(10,2) DEFAULT NULL,
  `request_date` date NOT NULL,
  `status_of_special_request` enum('Pending','Accepted','Rejected') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'Pending',
  `approved_by` int DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `answer_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`request_id`),
  KEY `special_requests_employees_FK` (`employee_id`),
  CONSTRAINT `special_requests_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `special_requests`
--

LOCK TABLES `special_requests` WRITE;
/*!40000 ALTER TABLE `special_requests` DISABLE KEYS */;
INSERT INTO `special_requests` VALUES (5,1,'Advance',1500.00,'2024-02-15','Accepted',2,'Acil tıbbi harcamalar için finansal destek ihtiyacı','2024-12-17','2024-12-16 23:16:52'),(6,2,'Salary Increase',NULL,'2024-03-01','Rejected',2,'Son performansa bağlı maaş değerlendirmesi','2024-12-17','2024-12-16 23:16:52'),(7,3,'Payback',2000.50,'2024-01-20','Rejected',5,'Önceki şirket kredisini geri ödeme talebi','2024-01-25','2024-12-16 23:16:52'),(8,4,'Other',500.75,'2024-02-28','Rejected',6,'Mesleki gelişim kursu için finansman','2024-03-05','2024-12-16 23:16:52'),(9,5,'Advance',1000.00,'2024-03-10','Rejected',2,'Acil kişisel finansal ihtiyaç','2024-12-17','2024-12-16 23:16:52'),(10,6,'Salary Increase',NULL,'2024-02-05','Rejected',5,'Performansa bağlı maaş ayarlaması','2024-02-15','2024-12-16 23:16:52'),(11,7,'Other',750.25,'2024-01-15','Rejected',2,'Uzaktan çalışma ekipmanı talebi','2024-12-17','2024-12-16 23:16:52'),(12,8,'Payback',3000.00,'2024-03-20','Accepted',2,'Şirket kredisi için taksit planı','2024-12-17','2024-12-16 23:16:52'),(13,9,'Advance',2500.00,'2024-02-10','Rejected',6,'Büyük tutarlı finansal yardım talebi','2024-02-20','2024-12-16 23:16:52'),(14,10,'Other',1200.50,'2024-03-05','Rejected',5,'Seyahat gideri geri ödemesi','2024-03-12','2024-12-16 23:16:52');
/*!40000 ALTER TABLE `special_requests` ENABLE KEYS */;
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
/*!50001 VIEW `employee_items_with_names` AS select `e`.`employee_id` AS `employee_id`,`e`.`first_name` AS `first_name`,`e`.`last_name` AS `last_name`,`ei`.`item_id` AS `item_id`,`i`.`item_name` AS `item_name`,`ei`.`quantity` AS `quantity`,`ei`.`assign_id` AS `assign_id`,`ei`.`assignment_date` AS `assignment_date` from ((`employee_items` `ei` join `employees` `e` on((`ei`.`employee_id` = `e`.`employee_id`))) join `items` `i` on((`ei`.`item_id` = `i`.`id`))) order by `ei`.`assignment_date` desc */;
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

-- Dump completed on 2024-12-20 12:37:26
