-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 29-08-2019 a las 00:09:49
-- Versión del servidor: 5.7.21
-- Versión de PHP: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `scabox`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo`
--

DROP TABLE IF EXISTS `articulo`;
CREATE TABLE IF NOT EXISTS `articulo` (
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_nombre` varchar(30) COLLATE latin1_spanish_ci NOT NULL COMMENT 'Nombre del artículo',
  `art_fecha_ultimo_ingreso` date NOT NULL COMMENT 'Fecha último ingreso del artículo',
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `art_cantidad` int(4) NOT NULL COMMENT 'Cantidad del articulo',
  PRIMARY KEY (`art_id`),
  KEY `tip_id` (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo_movil`
--

DROP TABLE IF EXISTS `articulo_movil`;
CREATE TABLE IF NOT EXISTS `articulo_movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_mov_cantidad` int(3) NOT NULL COMMENT 'Cantidad de articulos en el movil',
  KEY `mov_id` (`mov_id`,`art_id`),
  KEY `art_id` (`art_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo_tecnico`
--

DROP TABLE IF EXISTS `articulo_tecnico`;
CREATE TABLE IF NOT EXISTS `articulo_tecnico` (
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_tec_cantidad` int(3) NOT NULL COMMENT 'Cantidad de articulos del tecnico',
  KEY `usu_legajo` (`emp_legajo`),
  KEY `usu_legajo_2` (`emp_legajo`,`art_id`),
  KEY `art_id` (`art_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denuncias`
--

DROP TABLE IF EXISTS `denuncias`;
CREATE TABLE IF NOT EXISTS `denuncias` (
  `den_id` int(4) NOT NULL COMMENT 'ID de la denuncia',
  `den_numero_folio` int(30) NOT NULL COMMENT 'Numero de folio de la denuncia',
  `den_numero_acta` int(30) NOT NULL COMMENT 'Numero de acta de la denuncia',
  `den_comisaria` varchar(20) COLLATE latin1_spanish_ci NOT NULL COMMENT 'Nombre de la comisaria',
  `den_fecha_siniestro` date NOT NULL COMMENT 'Fecha del siniestro',
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `den_fecha_ingreso` date NOT NULL COMMENT 'Fecha de ingreso de denuncia',
  PRIMARY KEY (`den_id`),
  KEY `usu_legajo` (`emp_legajo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_denuncia_materiales`
--

DROP TABLE IF EXISTS `detalle_denuncia_materiales`;
CREATE TABLE IF NOT EXISTS `detalle_denuncia_materiales` (
  `den_id` int(4) NOT NULL COMMENT 'ID de la denuncia',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `det_den_mat_cantidad` int(3) NOT NULL COMMENT 'Cantidad de materiales denunciados',
  PRIMARY KEY (`den_id`),
  KEY `art_id` (`art_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_denuncia_serializables`
--

DROP TABLE IF EXISTS `detalle_denuncia_serializables`;
CREATE TABLE IF NOT EXISTS `detalle_denuncia_serializables` (
  `den_id` int(4) NOT NULL COMMENT 'Detalle de denuncia de serializables',
  `ser_mac` varchar(12) CHARACTER SET latin1 NOT NULL COMMENT 'MAC de serializables',
  KEY `den_id` (`den_id`,`ser_mac`),
  KEY `ser_mac` (`ser_mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dupla_movil`
--

DROP TABLE IF EXISTS `dupla_movil`;
CREATE TABLE IF NOT EXISTS `dupla_movil` (
  `dup_mov_id` int(2) NOT NULL COMMENT 'ID de la dupla del movil',
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  PRIMARY KEY (`dup_mov_id`),
  KEY `usu_legajo` (`emp_legajo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `emp_legajo` int(4) NOT NULL COMMENT 'Número de legajo de los empleados',
  `emp_documento` int(8) NOT NULL COMMENT 'Número de DNI de los empleados',
  `emp_nombre` varchar(50) NOT NULL COMMENT 'Nombre del empleado',
  `emp_apellido` varchar(50) NOT NULL COMMENT 'Apellido de los empleados',
  PRIMARY KEY (`emp_legajo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

DROP TABLE IF EXISTS `historial`;
CREATE TABLE IF NOT EXISTS `historial` (
  `his_id` int(4) NOT NULL COMMENT 'ID del historial',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables',
  `ser_estado` varchar(10) NOT NULL COMMENT 'Estado del serializable',
  `ser_fecha_entrega` date NOT NULL COMMENT 'Fecha de entrega del serializable',
  `ser_fecha_ultimo_estado` date NOT NULL COMMENT 'Fecha del ultimo estado',
  PRIMARY KEY (`his_id`),
  KEY `ser_mac` (`ser_mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movil`
--

DROP TABLE IF EXISTS `movil`;
CREATE TABLE IF NOT EXISTS `movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `dup_mov_id` int(2) NOT NULL COMMENT 'ID de la dupla del movil',
  `mov_patente` varchar(7) NOT NULL COMMENT 'Número de patente del móvil',
  `mov_seguro` int(8) NOT NULL COMMENT 'Número de póliza de seguro',
  `mov_vtv` date NOT NULL COMMENT 'Fecha de vencimiento de la VTV',
  `mov_tarjeta_verde` int(8) NOT NULL COMMENT 'Número de tarjeta verde',
  `mov_licencia` date NOT NULL COMMENT 'Fecha de vencimiento de la Licencia de conducir',
  PRIMARY KEY (`mov_id`),
  KEY `dup_mov_id` (`dup_mov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serializable`
--

DROP TABLE IF EXISTS `serializable`;
CREATE TABLE IF NOT EXISTS `serializable` (
  `ser_mac` varchar(12) NOT NULL COMMENT 'Número MAC de serializable',
  `ser_nombre` varchar(30) NOT NULL COMMENT 'Nombre del serializable',
  `ser_fecha_ultimo_ingreso` date NOT NULL COMMENT 'Fecha último ingreso del serializable',
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  PRIMARY KEY (`ser_mac`),
  KEY `tip_id` (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serializable_movil`
--

DROP TABLE IF EXISTS `serializable_movil`;
CREATE TABLE IF NOT EXISTS `serializable_movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables',
  KEY `mov_id` (`mov_id`,`ser_mac`),
  KEY `ser_mac` (`ser_mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo`
--

DROP TABLE IF EXISTS `tipo`;
CREATE TABLE IF NOT EXISTS `tipo` (
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `tip_descripcion` text NOT NULL COMMENT 'Descripcion del tipo',
  PRIMARY KEY (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usu_legajo` int(4) NOT NULL COMMENT 'Número de legajo del usuario',
  `usu_password` int(128) NOT NULL COMMENT 'Contraseña de usuario',
  `activo` tinyint(1) NOT NULL COMMENT 'Usuario activo o inactivo',
  KEY `usu_legajo` (`usu_legajo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD CONSTRAINT `articulo_ibfk_1` FOREIGN KEY (`tip_id`) REFERENCES `tipo` (`tip_id`);

--
-- Filtros para la tabla `articulo_movil`
--
ALTER TABLE `articulo_movil`
  ADD CONSTRAINT `articulo_movil_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`),
  ADD CONSTRAINT `articulo_movil_ibfk_2` FOREIGN KEY (`art_id`) REFERENCES `articulo` (`art_id`);

--
-- Filtros para la tabla `articulo_tecnico`
--
ALTER TABLE `articulo_tecnico`
  ADD CONSTRAINT `articulo_tecnico_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`),
  ADD CONSTRAINT `articulo_tecnico_ibfk_2` FOREIGN KEY (`art_id`) REFERENCES `articulo` (`art_id`);

--
-- Filtros para la tabla `denuncias`
--
ALTER TABLE `denuncias`
  ADD CONSTRAINT `denuncias_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `detalle_denuncia_materiales`
--
ALTER TABLE `detalle_denuncia_materiales`
  ADD CONSTRAINT `detalle_denuncia_materiales_ibfk_1` FOREIGN KEY (`den_id`) REFERENCES `denuncias` (`den_id`),
  ADD CONSTRAINT `detalle_denuncia_materiales_ibfk_2` FOREIGN KEY (`art_id`) REFERENCES `articulo` (`art_id`);

--
-- Filtros para la tabla `detalle_denuncia_serializables`
--
ALTER TABLE `detalle_denuncia_serializables`
  ADD CONSTRAINT `detalle_denuncia_serializables_ibfk_1` FOREIGN KEY (`den_id`) REFERENCES `denuncias` (`den_id`),
  ADD CONSTRAINT `detalle_denuncia_serializables_ibfk_2` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`);

--
-- Filtros para la tabla `dupla_movil`
--
ALTER TABLE `dupla_movil`
  ADD CONSTRAINT `dupla_movil_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `historial`
--
ALTER TABLE `historial`
  ADD CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`);

--
-- Filtros para la tabla `movil`
--
ALTER TABLE `movil`
  ADD CONSTRAINT `movil_ibfk_1` FOREIGN KEY (`dup_mov_id`) REFERENCES `dupla_movil` (`dup_mov_id`);

--
-- Filtros para la tabla `serializable`
--
ALTER TABLE `serializable`
  ADD CONSTRAINT `serializable_ibfk_1` FOREIGN KEY (`tip_id`) REFERENCES `tipo` (`tip_id`);

--
-- Filtros para la tabla `serializable_movil`
--
ALTER TABLE `serializable_movil`
  ADD CONSTRAINT `serializable_movil_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`),
  ADD CONSTRAINT `serializable_movil_ibfk_2` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`usu_legajo`) REFERENCES `empleados` (`emp_legajo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
