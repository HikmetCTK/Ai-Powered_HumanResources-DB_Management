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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-28 16:14:13
