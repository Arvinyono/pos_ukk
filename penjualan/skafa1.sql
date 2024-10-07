-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 07, 2024 at 05:02 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `skafa1`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_barang`
--

CREATE TABLE `tb_barang` (
  `idBarang` int(11) NOT NULL,
  `namaBarang` varchar(250) NOT NULL,
  `kategori` varchar(250) NOT NULL,
  `hargaBeli` int(11) NOT NULL,
  `hargaJual` int(11) NOT NULL,
  `stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_barang`
--

INSERT INTO `tb_barang` (`idBarang`, `namaBarang`, `kategori`, `hargaBeli`, `hargaJual`, `stok`) VALUES
(1, 'Soklin', 'sabun', 1300, 1500, 90),
(3, 'LUX', 'sabun', 2000, 2300, 50),
(7, 'PANTENE', 'Sampo', 1200, 1500, 100),
(8, 'Blue band', 'margarin', 2000, 3000, 15);

-- --------------------------------------------------------

--
-- Table structure for table `tb_pelanggan`
--

CREATE TABLE `tb_pelanggan` (
  `idPelanggan` int(11) NOT NULL,
  `noPelanggan` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `alamat` varchar(250) NOT NULL,
  `telp` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_pelanggan`
--

INSERT INTO `tb_pelanggan` (`idPelanggan`, `noPelanggan`, `name`, `alamat`, `telp`) VALUES
(9, '1212312344121231', 'Jhoni', 'Parakancanggah Banjarnegara', '08587787777'),
(12, '81231923012838', 'Budi', 'Semarang RT02 RW 03 BANJARNEGARA', '089645666262');

-- --------------------------------------------------------

--
-- Table structure for table `tb_pengeluaran`
--

CREATE TABLE `tb_pengeluaran` (
  `idPengeluaran` int(11) NOT NULL,
  `pengeluaran` varchar(200) NOT NULL,
  `nominal` int(11) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_pengeluaran`
--

INSERT INTO `tb_pengeluaran` (`idPengeluaran`, `pengeluaran`, `nominal`, `status`) VALUES
(424234, 'Bensin', 10000, 'hutang');

-- --------------------------------------------------------

--
-- Table structure for table `tb_suplier`
--

CREATE TABLE `tb_suplier` (
  `idSuplier` int(11) NOT NULL,
  `namaSuplier` varchar(250) NOT NULL,
  `alamat` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_suplier`
--

INSERT INTO `tb_suplier` (`idSuplier`, `namaSuplier`, `alamat`, `phone`) VALUES
(980984293, 'PT. BUDI UTAMA', 'Bandung Jawa Barat', '086773773');

-- --------------------------------------------------------

--
-- Table structure for table `tb_users`
--

CREATE TABLE `tb_users` (
  `id` int(11) NOT NULL,
  `username` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `level` enum('Admin','Petugas') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_users`
--

INSERT INTO `tb_users` (`id`, `username`, `email`, `password`, `level`) VALUES
(1, 'apin', 'apin@gmail.com', 'scrypt:32768:8:1$vYELQFG12ht9QvEt$88a418ead88aea98e4191ed2e2c02f62f293c6cf27993409768ea28d684ca32d6999dc33510cb79c2536e41583e64c402da696e12b2de1de6038e190fee96480', 'Petugas'),
(2, 'apin2', 'apin2@gmail.com', 'scrypt:32768:8:1$55ZfddoFnD0xKRgQ$88183cafc326ee70a123e1c2de7716a111bec9d0ff817a3e521c054eaa65fea4a80e22ed36ffee9953f644815df17befe881b2b4bd07771eaee0810d2d4110af', 'Admin'),
(3, 'bambang', 'bambang@gmail.com', 'scrypt:32768:8:1$8PiXa97SUAqgErGO$71fb1d14d16c894b02fb7651130d0e528a0d2728ff69f5fb188428d87c7455eed9b50fa7e4d94a57a67481ceeb0348cdd70110f085fe67a7d39869697fd83713', 'Petugas'),
(4, 'uus', 'uus@gmail.com', 'scrypt:32768:8:1$yt33J34jAyQUhfyr$7cf8dac9416fcb2d3fd62a031c975274462faf60df27f7c5623248efe2ee1e9dda2c6b39e3302dbad1acf750c64ccedf425384fc4d5e33ef7632b502f3c64ffd', 'Petugas'),
(5, 'chika', 'chika@gmail.com', 'scrypt:32768:8:1$HyJsMpr3q7Ay5voo$f03bf6424c5cc97a12f87f2ca3b2bb9d8d003a9772481b16429c7121b1251ecd7c3facff102afe43f6e05360b3bd5fb18bdac0387d8603e1ab2e3161722f1eff', 'Petugas'),
(6, 'desti', 'desti@gmail.com', 'scrypt:32768:8:1$jXaL7fkldeHDkNl5$e8aa5054305c5b225ba292637ae3f0d71fa44ed7c4233c063f0e68f1c6903d0e8c60258e6d8f1f58114348a50999768680d1241964a970a7b94578fc4e9d21dc', 'Petugas'),
(7, 'adnan', 'adnan@gmail.com', 'scrypt:32768:8:1$x85kI8qtVfWUPgEH$f1cf524b5554c171424a0dfc1c37f484b4fe06b3f625549c58232b2c42eb48a72db86cff0ce98c368faae559c2262f3b6b16a9f4eed8ebf70d6b2a9b2e49583a', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_barang`
--
ALTER TABLE `tb_barang`
  ADD PRIMARY KEY (`idBarang`);

--
-- Indexes for table `tb_pelanggan`
--
ALTER TABLE `tb_pelanggan`
  ADD PRIMARY KEY (`idPelanggan`);

--
-- Indexes for table `tb_pengeluaran`
--
ALTER TABLE `tb_pengeluaran`
  ADD PRIMARY KEY (`idPengeluaran`);

--
-- Indexes for table `tb_suplier`
--
ALTER TABLE `tb_suplier`
  ADD PRIMARY KEY (`idSuplier`);

--
-- Indexes for table `tb_users`
--
ALTER TABLE `tb_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_barang`
--
ALTER TABLE `tb_barang`
  MODIFY `idBarang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tb_pelanggan`
--
ALTER TABLE `tb_pelanggan`
  MODIFY `idPelanggan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `tb_pengeluaran`
--
ALTER TABLE `tb_pengeluaran`
  MODIFY `idPengeluaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=424235;

--
-- AUTO_INCREMENT for table `tb_suplier`
--
ALTER TABLE `tb_suplier`
  MODIFY `idSuplier` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT for table `tb_users`
--
ALTER TABLE `tb_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
