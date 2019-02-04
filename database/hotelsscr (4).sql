-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2019 at 09:35 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelsscr`
--

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `reserve_id` int(11) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `mode` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `reservations`
--

CREATE TABLE `reservations` (
  `id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  `rooms_id` int(11) NOT NULL,
  `date_in` datetime NOT NULL,
  `date_out` datetime NOT NULL,
  `child_count` int(11) NOT NULL,
  `adult_count` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `description`, `created_at`, `updated_at`) VALUES
(2, 'Superadmin', '                Admin\r\n              ', '2018-08-03 07:41:02', '0000-00-00 00:00:00'),
(3, 'Drivers', '                driver\r\n              ', '2019-01-20 16:57:20', '0000-00-00 00:00:00'),
(4, 'Conductor', 'conductor', '2018-07-27 05:34:47', '0000-00-00 00:00:00'),
(5, 'Passenger', 'Sasakay', '2018-07-27 05:34:47', '0000-00-00 00:00:00'),
(6, 'Mechanical', 'Repair', '2018-07-27 05:34:47', '0000-00-00 00:00:00'),
(7, 'Super duper adminssss', '                The head \r\n              ', '2018-08-23 02:14:07', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int(11) NOT NULL,
  `room_type` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `price` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `room_type`, `status`, `price`, `created_at`, `updated_at`) VALUES
(5, 'Deluxe', 'Vacant', 2000, '2019-01-29 07:25:01', '0000-00-00 00:00:00'),
(6, 'standard', 'vacant', 1000, '2019-01-29 07:52:01', '0000-00-00 00:00:00'),
(7, 'Suites', 'Vacant', 4000, '2019-01-29 07:52:24', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `schedules`
--

CREATE TABLE `schedules` (
  `id` int(11) NOT NULL,
  `departured_at` datetime NOT NULL,
  `arrived_at` datetime NOT NULL,
  `driver_id` int(11) NOT NULL,
  `bus_id` int(11) NOT NULL,
  `conductor_id` int(11) NOT NULL,
  `origin` varchar(255) DEFAULT NULL,
  `destination` varchar(255) DEFAULT NULL,
  `amount` float NOT NULL,
  `duration` varchar(50) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `schedules`
--

INSERT INTO `schedules` (`id`, `departured_at`, `arrived_at`, `driver_id`, `bus_id`, `conductor_id`, `origin`, `destination`, `amount`, `duration`, `status`, `created_at`, `updated_at`) VALUES
(8, '2018-08-20 00:00:00', '2018-08-14 00:00:00', 17, 17, 17, 'Manila', 'Manila', 0, '', 'On going', '2018-08-03 03:43:47', '0000-00-00 00:00:00'),
(12, '2018-08-21 00:00:00', '2018-08-10 00:00:00', 17, 17, 17, 'Manila', 'Cavite', 0, '', 'Standby', '2018-08-03 05:42:38', '0000-00-00 00:00:00'),
(13, '2018-08-21 00:00:00', '2018-08-10 00:00:00', 17, 17, 17, 'Manila', 'Cavite', 0, '', 'Standby', '2018-08-03 05:42:56', '0000-00-00 00:00:00'),
(21, '2018-08-29 00:00:00', '2018-08-23 00:00:00', 17, 17, 17, 'Manila', 'Cavite', 50000, '', 'Standby', '2018-08-07 08:03:50', '0000-00-00 00:00:00'),
(22, '2018-08-15 12:00:00', '2018-08-15 00:00:00', 27, 17, 27, '-Select-', '-Select-', 300000, '12H', 'Select', '2018-08-07 08:15:15', '0000-00-00 00:00:00'),
(23, '2018-08-24 00:12:00', '0000-00-00 00:00:00', 0, 0, 0, '-Select-', '-Select-', 0, '', 'Select', '2018-08-08 09:08:49', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `middlename` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `mobile` int(12) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `password` varchar(150) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `middlename`, `address`, `mobile`, `email`, `role`, `password`, `created_at`, `updated_at`) VALUES
(28, 'Jaebhy Rhoze', 'Baculto', 'Abad', 'Tagumpay St.', 2147483647, 'bacultojaebhyrhoze@yahoo.com', 'Cavite', '$5$rounds=535000$8YhvZ9qGaoUmTPgO$2dt5ZqBkIVRQZSKrqs8B9iym8NWgzJiibHkaIDONgRA', '2018-08-09 06:05:25', '2018-08-09 06:05:25'),
(37, 'Jp', 'trias', 'abueg', '45 ghfhfuytyutyu', 999999999, 'jptrias@yahoo.com', 'cashier', '$5$rounds=535000$C1xUNb7bsO..CYxr$3efan1MPVbqRm1N1a/6M05scUaQfMKtqzRpqbzaKaE7', '2019-01-20 16:44:39', '2019-01-20 16:44:39'),
(38, 'marian', 'ljsgdksaug', 'uuyiutuit', 'iuutiytty', 76767675, 'bahjafjhf@yahoo.com', 'cashier', '$5$rounds=535000$aWSjJmUzdcnZ1Gvp$PQe.pwVt2My11oZZVWG1l0h21.0AQVMRZ9M5DWrBRu.', '2019-01-21 01:35:04', '2019-01-21 01:35:04'),
(39, 'Dylan', 'Wang', 'A', 'Beijing,  China', 2147483647, 'cashier@yahoo.com', 'Cashier', '$5$rounds=535000$nwXhzFvY7fBPSUdN$ZVBO8wG.UKwQlPRmrPe2tZiGyK6O9MLrZP44MtB9Km1', '2019-01-29 07:57:38', '2019-01-29 07:57:38'),
(40, 'Dylan', 'Wang', 'A', 'Beijing,  China', 2147483647, 'cashier@yahoo.com', 'Cashier', '$5$rounds=535000$CVXv/RL7zNIbcafV$e57r2CKFYRB3lCjJeSYcTT2HPmlsxLZFRai92OdSGM0', '2019-01-29 07:57:43', '2019-01-29 07:57:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `schedules`
--
ALTER TABLE `schedules`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reservations`
--
ALTER TABLE `reservations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `schedules`
--
ALTER TABLE `schedules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
