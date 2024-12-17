-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: dump
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

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
  `status_of_request` enum('Pending','Approved','Rejected') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'Pending',
  `approved_by` int DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `answer_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`request_id`),
  KEY `special_requests_employees_FK` (`employee_id`),
  CONSTRAINT `special_requests_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `special_requests`
--

LOCK TABLES `special_requests` WRITE;
/*!40000 ALTER TABLE `special_requests` DISABLE KEYS */;
INSERT INTO `special_requests` VALUES (17,199,'Other',1200.50,'2024-03-05','Rejected',199,'Seyahat gideri geri ödemesi','2024-12-17','2024-12-16 23:11:50'),(20,220,'Payback',25000.00,'2024-12-17','Rejected',199,'Para İstiyorum Lan','2024-12-17','2024-12-17 17:40:07');
/*!40000 ALTER TABLE `special_requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_leaves`
--

DROP TABLE IF EXISTS `employee_leaves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_leaves` (
  `leave_request_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `status_of_request` enum('Pending','Approved','Rejected') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'Pending',
  `request_date` date DEFAULT NULL,
  `approved_by` int DEFAULT NULL,
  `answer_date` date DEFAULT NULL,
  `leave_type` enum('Annual Leave','Health Leave','Unpaid Leave','Excuse Leave') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `total_dates` int NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`leave_request_id`),
  KEY `employee_leaves_employees_FK` (`employee_id`),
  CONSTRAINT `employee_leaves_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_leaves`
--

LOCK TABLES `employee_leaves` WRITE;
/*!40000 ALTER TABLE `employee_leaves` DISABLE KEYS */;
INSERT INTO `employee_leaves` VALUES (29,215,'Pending','2024-12-17',198,'2024-12-17','Annual Leave','2024-07-03','2024-07-18',16,'İzin talebi Ret','2024-12-16 23:45:25'),(30,215,'Rejected','2024-12-17',199,'2024-12-17','Health Leave','2024-07-03','2024-07-18',16,'Hatalı Talep','2024-12-16 23:45:41'),(31,191,'Rejected','2024-12-17',193,'2024-12-17','Annual Leave','2024-07-03','2024-07-18',16,'Hatalı Talep','2024-12-17 17:35:45');
/*!40000 ALTER TABLE `employee_leaves` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-17 23:42:14
