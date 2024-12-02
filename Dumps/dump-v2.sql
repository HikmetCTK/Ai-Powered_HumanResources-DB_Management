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
  UNIQUE KEY `daily_working_hours_unique` (`employee_id`,`work_date`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_working_hours`
--

LOCK TABLES `daily_working_hours` WRITE;
/*!40000 ALTER TABLE `daily_working_hours` DISABLE KEYS */;
INSERT INTO `daily_working_hours` VALUES (1,101,'2024-11-30',1,'2024-11-30 08:00:00','2024-11-30 17:00:00',8.000,1.50,0.50,0.00,'Tam gün','P12345','Proje toplantısı yapıldı.','2024-12-01 18:27:09',NULL),(2,102,'2024-11-30',1,'2024-11-30 09:00:00','2024-11-30 13:00:00',4.000,0.00,0.30,0.00,'Yarım gün','P67890','Sabah eğitim verildi.','2024-12-01 18:27:09',NULL),(3,103,'2024-11-30',0,NULL,NULL,0.000,0.00,0.00,8.00,'Yok',NULL,'Hasta olduğu için gelmedi.','2024-12-01 18:27:09',NULL),(4,104,'2024-11-30',1,'2024-11-30 08:30:00','2024-11-30 18:30:00',9.500,2.00,1.00,0.00,'Tam gün','P54321','Yoğun iş günü.','2024-12-01 18:27:09',NULL),(5,105,'2024-11-30',1,'2024-11-30 07:45:00','2024-11-30 16:15:00',7.500,0.00,0.75,0.25,'Tam gün','P11223','Rutin çalışma günü.','2024-12-01 18:27:09',NULL),(6,101,'2024-11-29',1,'2024-11-29 08:15:00','2024-11-29 16:45:00',8.000,0.50,0.30,0.00,'Tam gün','P12345','Normal iş günü.','2024-12-01 18:31:54',NULL),(7,101,'2024-11-28',1,'2024-11-28 09:00:00','2024-11-28 18:30:00',8.500,1.50,0.50,0.00,'Tam gün','P12345','Proje teslim çalışması.','2024-12-01 18:31:54',NULL),(8,102,'2024-11-29',1,'2024-11-29 09:00:00','2024-11-29 13:00:00',4.000,0.00,0.20,0.00,'Yarım gün','P67890','Kısa süreli bir toplantı.','2024-12-01 18:31:54',NULL),(9,102,'2024-11-28',0,NULL,NULL,0.000,0.00,0.00,8.00,'Yok',NULL,'Katılım sağlamadı.','2024-12-01 18:31:54',NULL),(10,103,'2024-11-29',1,'2024-11-29 10:00:00','2024-11-29 14:30:00',4.000,0.00,0.50,0.00,'Yarım gün','P54321','Sağlık durumundan dolayı geç başladı.','2024-12-01 18:31:54',NULL),(11,103,'2024-11-28',0,NULL,NULL,0.000,0.00,0.00,8.00,'Yok',NULL,'İş yerinde yok.','2024-12-01 18:31:54',NULL),(12,104,'2024-11-29',1,'2024-11-29 07:30:00','2024-11-29 16:30:00',8.500,0.00,0.50,0.00,'Tam gün','P54321','Proje planlaması yapıldı.','2024-12-01 18:31:54',NULL),(13,104,'2024-11-28',1,'2024-11-28 08:00:00','2024-11-28 18:00:00',9.500,2.00,0.50,0.00,'Tam gün','P54321','Yoğun iş programı.','2024-12-01 18:31:54',NULL),(14,105,'2024-11-29',1,'2024-11-29 07:45:00','2024-11-29 15:45:00',7.500,0.00,0.75,0.00,'Tam gün','P11223','Normal iş günü.','2024-12-01 18:31:54',NULL),(15,105,'2024-11-28',1,'2024-11-28 08:00:00','2024-11-28 16:30:00',8.000,0.50,0.50,0.00,'Tam gün','P11223','Rutin iş günü.','2024-12-01 18:31:54',NULL),(16,106,'2024-11-29',1,'2024-11-29 08:15:00','2024-11-29 16:45:00',8.000,0.50,0.00,0.00,'Tam gün','P12345','Normal iş günü.','2024-12-01 19:24:50',NULL),(17,107,'2024-11-29',1,'2024-11-29 08:15:00','2024-11-29 16:45:00',8.000,0.50,0.80,0.00,'Tam gün','P12445','Normal iş günü.','2024-12-01 19:54:06',NULL),(18,109,'2024-11-30',1,'2024-11-30 08:15:00','2024-11-30 15:55:00',7.670,0.50,0.80,0.00,'Yarım gün','P12445','Yarım iş günü.','2024-12-01 20:38:08','2024-12-01 20:47:37');
/*!40000 ALTER TABLE `daily_working_hours` ENABLE KEYS */;
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
  KEY `employee_leaves_employees_FK` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_leaves`
--

LOCK TABLES `employee_leaves` WRITE;
/*!40000 ALTER TABLE `employee_leaves` DISABLE KEYS */;
INSERT INTO `employee_leaves` VALUES (1,199,'Onaylandı',NULL,201,NULL,'Yıllık İzin','2024-07-01','2024-07-10','İzin talebi onaylandı',10,NULL),(2,199,'Beklemede',NULL,NULL,NULL,'Yıllık İzin','2024-07-01','2024-07-10','Yaz tatili için izin talebi',10,NULL),(3,199,'Onaylandı',NULL,203,'2024-11-30','Yıllık İzin','2024-07-01','2024-07-10','İzin talebi onaylandı',10,NULL),(4,199,'Beklemede',NULL,NULL,NULL,'Yıllık İzin','2024-07-01','2024-07-10','Yaz tatili için izin talebi',10,NULL),(5,199,'Beklemede',NULL,NULL,NULL,'Yıllık İzin','2024-07-01','2024-07-10','Yaz tatili için izin talebi',10,NULL),(6,255,'Beklemede',NULL,NULL,NULL,'Ücretsiz İzin','2024-07-01','2024-10-10','Hamilelik için izin talebi',102,NULL),(7,255,'Beklemede',NULL,NULL,NULL,'Ücretsiz İzin','2024-07-01','2024-10-10','Hamilelik için izin talebi',102,NULL),(8,255,'Onaylandı',NULL,198,'2024-12-01','Ücretsiz İzin','2024-07-01','2024-10-10','İzin talebi onaylandı',102,NULL),(9,222,'Beklemede','2024-11-30',NULL,NULL,'Sağlık İzni','2024-08-03','2024-08-06','Ameliyat İzni',4,NULL),(10,232,'Onaylandı','2024-11-30',203,'2024-11-30','Sağlık İzni','2024-09-03','2024-09-03','İzin talebi onaylandı',1,'2024-11-30 16:46:40'),(11,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 13:51:11'),(12,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:44:09'),(13,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:44:53'),(14,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:45:38'),(15,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:46:41'),(16,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:47:03'),(17,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:53:47'),(18,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:54:35'),(19,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:55:02'),(20,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:57:44'),(21,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 14:58:18'),(22,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 15:00:42'),(23,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 15:01:06'),(24,245,'Beklemede','2024-12-01',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-01 15:03:25'),(25,245,'Beklemede','2024-12-02',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-02 00:29:58'),(26,245,'Beklemede','2024-12-02',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-02 00:32:19'),(27,245,'Beklemede','2024-12-02',NULL,NULL,'Yıllık İzin','2024-07-03','2024-07-18','Tatil İzni',16,'2024-12-02 00:32:38');
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
  `department` varchar(90) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `salary` decimal(8,2) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `is_activate` tinyint DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=221 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (191,'Alice','Smith','1985-06-15','Female','Soware','IT',75000.00,NULL,NULL,'1234567890','password123',NULL),(192,'Bob','Johnson','1990-03-22','Male','Data','Anals',68000.00,NULL,NULL,'0987654321','securepass456',NULL),(193,'Carol','Williams','1988-11-08','Female','Project','Manat',82000.00,NULL,NULL,'1112223333','project123',NULL),(194,'David','Brown','1992-01-30','Male','System ','IT',71000.00,NULL,NULL,'2223334444','sysadmin789',NULL),(195,'Eva','Davis','1986-04-17','Female','UXr','Design',69000.00,NULL,NULL,'3334445555','designpass',NULL),(196,'Frank','Miller','1983-07-25','Male','Marke','Marketing',63000.00,NULL,NULL,'4445556666','marketpass',NULL),(197,'Grace','Wilson','1995-12-12','Female','Accout','Finance',67000.00,NULL,NULL,'5556667777','finance789',NULL),(198,'Henry','Moore','1989-05-09','Male','HR','Human',64000.00,NULL,NULL,'6667778888','hrsecure',NULL),(199,'Ivy','Taylor','1993-09-23','Female','Legalr','Legal',55000.00,NULL,NULL,'7778889999','legalpass123',NULL),(200,'Jack','Anderson','1987-02-11','Male','Sales ','Sales',99999.00,NULL,NULL,'8889990000','salespass456',NULL),(201,'Alice','Smith','1985-06-15','Female','Soware','IT',75000.00,NULL,NULL,'1234567890','password123',NULL),(202,'Bob','Johnson','1990-03-22','Male','Data','Anals',68000.00,NULL,NULL,'0987654321','securepass456',NULL),(203,'Carol','Williams','1988-11-08','Female','Project','Manat',82000.00,NULL,NULL,'1112223333','project123',NULL),(204,'David','Brown','1992-01-30','Male','System ','IT',71000.00,NULL,NULL,'2223334444','sysadmin789',NULL),(205,'Eva','Davis','1986-04-17','Female','UXr','Design',69000.00,NULL,NULL,'3334445555','designpass',NULL),(206,'Frank','Miller','1983-07-25','Male','Marke','Marketing',63000.00,NULL,NULL,'4445556666','marketpass',NULL),(207,'Grace','Wilson','1995-12-12','Female','Accout','Finance',67000.00,NULL,NULL,'5556667777','finance789',NULL),(208,'Henry','Moore','1989-05-09','Male','HR','Human',64000.00,NULL,NULL,'6667778888','hrsecure',NULL),(209,'Ivy','Taylor','1993-09-23','Female','Legalr','Legal',85000.00,NULL,NULL,'7778889999','legalpass123',NULL),(210,'Jack','Anderson','1987-02-11','Male','Sales ','Sales',78000.00,NULL,NULL,'8889990000','salespass456',NULL),(211,'Alice','Smith','1985-06-15','Female','Soware','IT',75000.00,NULL,NULL,'1234567890','password123',NULL),(212,'Bob','Johnson','1990-03-22','Male','Data','Anals',68000.00,NULL,NULL,'0987654321','securepass456',NULL),(213,'Carol','Williams','1988-11-08','Female','Project','Mana',82000.00,NULL,NULL,'1112223333','project123',NULL),(214,'David','Brown','1992-01-30','Male','System ','IT',71000.00,NULL,NULL,'2223334444','sysadmin789',NULL),(215,'Eva','Davis','1986-04-17','Female','UXr','Design',69000.00,NULL,NULL,'3334445555','designpass',NULL),(216,'Frank','Miller','1983-07-25','Male','Marke','Marketing',63000.00,NULL,NULL,'4445556666','marketpass',NULL),(217,'Grace','Wilson','1995-12-12','Female','Accout','Finance',67000.00,NULL,NULL,'5556667777','finance789',NULL),(218,'Henry','Moore','1989-05-09','Male','HR','Human',64000.00,NULL,NULL,'6667778888','hrsecure',NULL),(219,'Ivy','Taylor','1993-09-23','Female','Legalr','Legal',85000.00,NULL,NULL,'7778889999','legalpass123',NULL),(220,'Jack','Anderson','1987-02-11','Male','Sales ','Sales',78000.00,NULL,NULL,'8889990000','salespass456',NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
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
  UNIQUE KEY `monthly_work_hours_unique` (`employee_id`,`work_year`,`work_month`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthly_work_hours`
--

LOCK TABLES `monthly_work_hours` WRITE;
/*!40000 ALTER TABLE `monthly_work_hours` DISABLE KEYS */;
INSERT INTO `monthly_work_hours` VALUES (1,101,'2024','11',24.50,3.50,0.00,8.17,0,30.00,3.00,0.00,'10.00',NULL,NULL,'2024-12-01 21:46:44','2024-12-01 21:46:44'),(2,102,'2024','11',8.00,0.00,8.00,8.00,1,30.00,1.00,2.00,'3.33333',NULL,NULL,'2024-12-01 21:47:27','2024-12-01 21:47:27'),(3,105,'2024','11',23.00,0.50,0.25,7.67,0,30.00,3.00,0.00,'10.00',NULL,NULL,'2024-12-01 21:53:55','2024-12-01 21:53:55'),(4,104,'2024','11',27.50,4.00,0.00,0.00,3,30.00,0.00,0.00,'0.00',NULL,NULL,'2024-12-01 22:25:41','2024-12-01 22:25:41'),(5,101,'2024','12',160.00,20.50,8.75,28.50,3,20.00,4.00,1.00,'95.75',2,'Excellent performance','2024-12-01 05:00:00','2024-12-01 15:00:00'),(6,102,'2024','12',168.00,15.25,5.50,31.00,4,21.00,5.00,0.00,'98.25',1,'Met all targets','2024-12-01 05:00:00','2024-12-01 15:00:00'),(7,117,'2024','12',165.00,32.50,5.00,1.00,5,14.00,6.00,20.00,'97.00',2,'Exceeded expectations','2024-12-01 23:38:47','2024-12-01 23:38:47'),(9,103,'2024','11',4.00,0.00,16.00,0.00,3,30.00,0.00,0.00,'0.00',NULL,NULL,'2024-12-01 23:40:10','2024-12-01 23:40:10'),(23,118,'2024','12',125.00,32.50,5.00,1.00,5,13.00,5.00,20.00,'94',2,'Exceeded expectations','2024-12-02 01:53:27','2024-12-02 01:53:27');
/*!40000 ALTER TABLE `monthly_work_hours` ENABLE KEYS */;
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
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `special_requests`
--

LOCK TABLES `special_requests` WRITE;
/*!40000 ALTER TABLE `special_requests` DISABLE KEYS */;
INSERT INTO `special_requests` VALUES (1,199,'Avans',5000.00,'2024-11-28','Reddedildi','Avans talebi Reddedildi',200,'2024-11-30','2024-11-28 20:11:52'),(2,210,'Avans',15000.00,'2024-11-30','Reddedildi','Avans talebi Reddedildi',200,'2024-11-30','2024-11-30 16:11:50'),(3,210,'Avans',15000.00,'2024-11-30','Beklemede','Acil harcama için avans talebi',NULL,NULL,'2024-11-30 16:39:12'),(4,222,'Zam',25000.00,'2024-12-01','Reddedildi','Zam talebi Reddedildi',200,'2024-12-01','2024-12-01 14:02:43');
/*!40000 ALTER TABLE `special_requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'dump'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-02  5:01:54
