-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2020 at 09:30 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scoala`
--

-- --------------------------------------------------------

--
-- Table structure for table `absente`
--

CREATE TABLE `absente` (
  `id` bigint(20) NOT NULL,
  `code` bigint(20) UNSIGNED NOT NULL,
  `codd` bigint(11) UNSIGNED NOT NULL,
  `dataa` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `absente`
--

INSERT INTO `absente` (`id`, `code`, `codd`, `dataa`) VALUES
(16, 3, 5, '2018-03-02'),
(17, 2, 6, '2018-01-10');

-- --------------------------------------------------------

--
-- Table structure for table `disciplina`
--

CREATE TABLE `disciplina` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nume_disciplina` text NOT NULL,
  `profesor` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disciplina`
--

INSERT INTO `disciplina` (`id`, `nume_disciplina`, `profesor`) VALUES
(5, 'AIBD', 'Munteanu Dan'),
(6, 'PCLJ', 'Cocu Adina');

-- --------------------------------------------------------

--
-- Table structure for table `elev`
--

CREATE TABLE `elev` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nume_elev` text NOT NULL,
  `clasa` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `elev`
--

INSERT INTO `elev` (`id`, `nume_elev`, `clasa`) VALUES
(2, 'Urse Horia-Cristian', '12-b'),
(3, 'Popescu Ion', '8-c'),
(9, 'Vasi', '9-a');

-- --------------------------------------------------------

--
-- Table structure for table `elev_disciplina`
--

CREATE TABLE `elev_disciplina` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `code` bigint(11) UNSIGNED NOT NULL,
  `codd` bigint(11) UNSIGNED NOT NULL,
  `data` date NOT NULL,
  `nota` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `elev_disciplina`
--

INSERT INTO `elev_disciplina` (`id`, `code`, `codd`, `data`, `nota`) VALUES
(16, 2, 5, '2018-05-18', 9),
(17, 3, 6, '2018-04-24', 7);

-- --------------------------------------------------------

--
-- Table structure for table `hibernate_sequence`
--

CREATE TABLE `hibernate_sequence` (
  `next_val` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hibernate_sequence`
--

INSERT INTO `hibernate_sequence` (`next_val`) VALUES
(14),
(14),
(14),
(14);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absente`
--
ALTER TABLE `absente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dataa` (`dataa`),
  ADD KEY `coddd` (`codd`),
  ADD KEY `codee` (`code`);

--
-- Indexes for table `disciplina`
--
ALTER TABLE `disciplina`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `elev`
--
ALTER TABLE `elev`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `elev_disciplina`
--
ALTER TABLE `elev_disciplina`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `code` (`code`),
  ADD KEY `codd` (`codd`),
  ADD KEY `code_2` (`code`,`codd`),
  ADD KEY `data` (`data`),
  ADD KEY `nota` (`nota`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `absente`
--
ALTER TABLE `absente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `disciplina`
--
ALTER TABLE `disciplina`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `elev`
--
ALTER TABLE `elev`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `elev_disciplina`
--
ALTER TABLE `elev_disciplina`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `absente`
--
ALTER TABLE `absente`
  ADD CONSTRAINT `absente_fk1` FOREIGN KEY (`codd`) REFERENCES `disciplina` (`id`),
  ADD CONSTRAINT `absente_fk2` FOREIGN KEY (`code`) REFERENCES `elev` (`id`);

--
-- Constraints for table `elev_disciplina`
--
ALTER TABLE `elev_disciplina`
  ADD CONSTRAINT `fk_disciplina` FOREIGN KEY (`codd`) REFERENCES `disciplina` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_elev` FOREIGN KEY (`code`) REFERENCES `elev` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
