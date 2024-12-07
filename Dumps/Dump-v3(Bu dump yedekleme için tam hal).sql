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
-- Table structure for table `daily_working_hours`
--

DROP TABLE IF EXISTS `daily_working_hours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_working_hours` (
  `day_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `work_date` date NOT NULL,
  `attendance` tinyint NOT NULL,
  `clock_in_time` datetime DEFAULT NULL,
  `clock_out_time` datetime DEFAULT NULL,
  `total_work_hours` decimal(7,3) DEFAULT NULL,
  `overtime_hours` decimal(5,2) DEFAULT '0.00',
  `break_duration` decimal(5,2) DEFAULT '0.00',
  `absence_hours` decimal(5,2) DEFAULT '0.00',
  `work_status` enum('Tam gün','Yarım gün','Yok') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Project_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`day_id`),
  UNIQUE KEY `daily_working_hours_unique` (`employee_id`,`work_date`),
  CONSTRAINT `daily_working_hours_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_working_hours`
--

LOCK TABLES `daily_working_hours` WRITE;
/*!40000 ALTER TABLE `daily_working_hours` DISABLE KEYS */;
/*!40000 ALTER TABLE `daily_working_hours` ENABLE KEYS */;
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
  `request_type` enum('Avans','Zam','Geri Ödeme','Diğer') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `request_amount` decimal(10,2) DEFAULT NULL,
  `request_date` date NOT NULL,
  `status_of_special_request` enum('Beklemede','Onaylandı','Reddedildi') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'Beklemede',
  `description` text,
  `approved_by` int DEFAULT NULL,
  `answer_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`request_id`),
  KEY `special_requests_employees_FK` (`employee_id`),
  CONSTRAINT `special_requests_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `special_requests`
--

LOCK TABLES `special_requests` WRITE;
/*!40000 ALTER TABLE `special_requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `special_requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monthly_work_hours`
--

DROP TABLE IF EXISTS `monthly_work_hours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monthly_work_hours` (
  `monthly_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `work_year` varchar(4) NOT NULL,
  `work_month` varchar(2) NOT NULL,
  `total_work_hours` decimal(7,2) DEFAULT '0.00',
  `total_overtime_hours` decimal(7,2) DEFAULT '0.00',
  `total_absence_hours` decimal(7,2) DEFAULT '0.00',
  `Average_Hours` decimal(7,2) DEFAULT NULL,
  `Number_of_Days_Off` int DEFAULT NULL,
  `total_work_days` decimal(5,2) DEFAULT '0.00',
  `total_worked_days` decimal(5,2) DEFAULT NULL,
  `total_half_days` decimal(5,2) DEFAULT NULL,
  `attendance_percentage` varchar(7) DEFAULT NULL,
  `paid_leave_days` int DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`monthly_id`),
  UNIQUE KEY `monthly_work_hours_unique` (`employee_id`,`work_year`,`work_month`),
  CONSTRAINT `monthly_work_hours_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthly_work_hours`
--

LOCK TABLES `monthly_work_hours` WRITE;
/*!40000 ALTER TABLE `monthly_work_hours` DISABLE KEYS */;
/*!40000 ALTER TABLE `monthly_work_hours` ENABLE KEYS */;
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
  `status_of_leave_asking` enum('Beklemede','Onaylandı','Reddedildi') NOT NULL DEFAULT 'Beklemede',
  `request_date` date DEFAULT NULL,
  `approved_by` int DEFAULT NULL,
  `answer_date` date DEFAULT NULL,
  `leave_type` enum('Yıllık İzin','Sağlık İzni','Ücretsiz İzin','Mazeret İzni') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `description` text,
  `total_dates` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`leave_request_id`),
  KEY `employee_leaves_employees_FK` (`employee_id`),
  CONSTRAINT `employee_leaves_employees_FK` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_leaves`
--

LOCK TABLES `employee_leaves` WRITE;
/*!40000 ALTER TABLE `employee_leaves` DISABLE KEYS */;
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

-- Dump completed on 2024-12-08  1:02:51
