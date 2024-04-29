-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2024 at 05:05 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecommerceguvi`
--

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `oid` int(11) NOT NULL,
  `products` varchar(1000) NOT NULL,
  `price` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `deliveryStatus` varchar(100) NOT NULL,
  `timeStamp` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`oid`, `products`, `price`, `email`, `address`, `pincode`, `deliveryStatus`, `timeStamp`) VALUES
(1, '[\"Camera\",\"camera dslr\",\"Earbuds\"]', '61500.00', 'ark@gmail.com', 'Bangalore', '560032', 'Not Delivered', '2024-04-27 19:56:02.271147');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `pid` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `productname` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `stock` varchar(100) NOT NULL,
  `pimage` varchar(1000) NOT NULL,
  `timestamp` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`pid`, `email`, `productname`, `price`, `category`, `description`, `stock`, `pimage`, `timestamp`) VALUES
(1, 'ark@gmail.com', 'Camera', '15000', 'DSLR', 'Best Camera in the market', '150', 'Dslrr.jpg', '2024-04-23 20:51:43.591581'),
(2, 'ark@gmail.com', 'Shoes', '450', 'Bata', 'Best shoes in the market', '100', 'shoe.jpg', '2024-04-24 20:04:58.079797'),
(3, 'ark@gmail.com', 'camera dslr', '45000', 'dslr', 'Best camera for zooming', '14', 'cam2.jpg', '2024-04-24 20:14:19.204264'),
(4, 'ark@gmail.com', 'Earbuds', '1500', 'boat', 'Best aipods for listening music', '150', 'e2.jpg', '2024-04-24 20:14:58.233458');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `userid` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` text NOT NULL,
  `phone` varchar(12) NOT NULL,
  `isAdmin` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`userid`, `firstname`, `lastname`, `email`, `password`, `phone`, `isAdmin`) VALUES
(5, 'anees', 'khan', 'ark@gmail.com', 'scrypt:32768:8:1$TBgme915tkIIj43h$9652138b89400b7629f4c187da9cb32b5af869b64b3d36488a863603fd4b7a6136dc51edea6296ef1ddc1c2e68ee24f274a50904d3f88fa65c8a172a9904dbff', '9874569874', 'True'),
(6, 'aadithya', 'rajat', 'arg@gmail.com', 'scrypt:32768:8:1$iclX5aP9TriexzF4$311f496e479043d11ba8a2cefd78bed44afe8682e0ed0418e8718e7a37b8e7edbe9fa6775944b7dd1d1110ff30bff20e5c2cc49b88b70e4a2f08345819260154', '8574963214', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'ark'),
(2, 'pro');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `signup`
--
ALTER TABLE `signup`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `oid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `signup`
--
ALTER TABLE `signup`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
