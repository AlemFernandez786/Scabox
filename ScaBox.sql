-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 24-09-2019 a las 23:49:17
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.1.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ScaBox`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo`
--

CREATE TABLE `articulo` (
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_nombre` varchar(30) COLLATE latin1_spanish_ci NOT NULL COMMENT 'Nombre del artículo',
  `art_fecha_ultimo_ingreso` date NOT NULL COMMENT 'Fecha último ingreso del artículo',
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `art_cantidad` int(4) NOT NULL COMMENT 'Cantidad del articulo',
  `art_cant_min` int(8) NOT NULL COMMENT 'Cantidad minima aceptada',
  `art_cant_max` int(8) NOT NULL COMMENT 'Cantidad maxima aceptada'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`art_id`, `art_nombre`, `art_fecha_ultimo_ingreso`, `tip_id`, `art_cantidad`, `art_cant_min`, `art_cant_max`) VALUES
(123456, 'asd', '2019-09-18', 3, 110004565, 7, 60),
(456789, 'fds', '2019-09-18', 3, 74665, 1, 10),
(456790, 'Divisorx3', '2019-09-16', 3, 49, 50, 200),
(456791, 'Descripcion', '2019-09-16', 3, 2, 13, 78),
(456792, 'poi', '2019-09-18', 3, 12, 1, 99);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo_movil`
--

CREATE TABLE `articulo_movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_mov_cantidad` int(3) NOT NULL COMMENT 'Cantidad de articulos en el movil'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `articulo_movil`
--

INSERT INTO `articulo_movil` (`mov_id`, `art_id`, `art_mov_cantidad`) VALUES
(4564, 123456, 12),
(4564, 456791, 123);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo_tecnico`
--

CREATE TABLE `articulo_tecnico` (
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_tec_cantidad` int(3) NOT NULL COMMENT 'Cantidad de articulos del tecnico'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denuncias`
--

CREATE TABLE `denuncias` (
  `den_id` int(4) NOT NULL COMMENT 'ID de la denuncia',
  `den_numero_folio` int(30) NOT NULL COMMENT 'Numero de folio de la denuncia',
  `den_numero_acta` int(30) NOT NULL COMMENT 'Numero de acta de la denuncia',
  `den_comisaria` varchar(20) COLLATE latin1_spanish_ci NOT NULL COMMENT 'Nombre de la comisaria',
  `den_fecha_siniestro` date NOT NULL COMMENT 'Fecha del siniestro',
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `den_fecha_ingreso` date NOT NULL COMMENT 'Fecha de ingreso de denuncia'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_denuncia_materiales`
--

CREATE TABLE `detalle_denuncia_materiales` (
  `den_id` int(4) NOT NULL COMMENT 'ID de la denuncia',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `det_den_mat_cantidad` int(3) NOT NULL COMMENT 'Cantidad de materiales denunciados'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_denuncia_serializables`
--

CREATE TABLE `detalle_denuncia_serializables` (
  `den_id` int(4) NOT NULL COMMENT 'Detalle de denuncia de serializables',
  `ser_mac` varchar(12) CHARACTER SET latin1 NOT NULL COMMENT 'MAC de serializables'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dupla_movil`
--

CREATE TABLE `dupla_movil` (
  `dup_mov_id` int(2) NOT NULL COMMENT 'ID de la dupla del movil',
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dupla_movil`
--

INSERT INTO `dupla_movil` (`dup_mov_id`, `emp_legajo`) VALUES
(1, 1),
(2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `emp_legajo` int(4) NOT NULL COMMENT 'Número de legajo de los empleados',
  `emp_documento` int(8) NOT NULL COMMENT 'Número de DNI de los empleados',
  `emp_nombre` varchar(50) NOT NULL COMMENT 'Nombre del empleado',
  `emp_apellido` varchar(50) NOT NULL COMMENT 'Apellido de los empleados'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`emp_legajo`, `emp_documento`, `emp_nombre`, `emp_apellido`) VALUES
(1, 123456, 'gusti', 'canob'),
(2, 123789, 'fran', 'larosa'),
(123, 1234123, 'asdqwe', 'zxcsd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_materiales`
--

CREATE TABLE `historial_materiales` (
  `art_id` int(8) NOT NULL,
  `his_mat_cantidad` int(4) NOT NULL,
  `his_mat_fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `historial_materiales`
--

INSERT INTO `historial_materiales` (`art_id`, `his_mat_cantidad`, `his_mat_fecha`) VALUES
(456790, 25, '2019-09-18'),
(456790, 26, '2019-09-11'),
(456789, 10, '2019-08-01'),
(456791, 10, '2019-08-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_sectores`
--

CREATE TABLE `historial_sectores` (
  `fecha_cambio_sector` datetime NOT NULL COMMENT 'Fecha del cambio',
  `emp_legajo` int(8) NOT NULL COMMENT 'Legajo del empleado',
  `emp_sector` int(2) NOT NULL COMMENT 'Sector en el que se encuentra el empleado',
  `motivo_cambio` varchar(255) NOT NULL COMMENT 'Motivo del cambio de sector'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_serializables`
--

CREATE TABLE `historial_serializables` (
  `his_id` int(4) NOT NULL COMMENT 'ID del historial',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables',
  `ser_estado` varchar(10) NOT NULL COMMENT 'Estado del serializable',
  `ser_fecha_entrega` date NOT NULL COMMENT 'Fecha de entrega del serializable',
  `ser_fecha_ultimo_estado` date NOT NULL COMMENT 'Fecha del ultimo estado'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movil`
--

CREATE TABLE `movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `dup_mov_id` int(2) NOT NULL COMMENT 'ID de la dupla del movil',
  `mov_patente` varchar(7) NOT NULL COMMENT 'Número de patente del móvil',
  `mov_seguro` int(8) NOT NULL COMMENT 'Número de póliza de seguro',
  `mov_vtv` date NOT NULL COMMENT 'Fecha de vencimiento de la VTV',
  `mov_tarjeta_verde` int(8) NOT NULL COMMENT 'Número de tarjeta verde',
  `mov_licencia` date NOT NULL COMMENT 'Fecha de vencimiento de la Licencia de conducir'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `movil`
--

INSERT INTO `movil` (`mov_id`, `dup_mov_id`, `mov_patente`, `mov_seguro`, `mov_vtv`, `mov_tarjeta_verde`, `mov_licencia`) VALUES
(4564, 1, '123asd', 1321564, '2019-09-18', 12313, '2019-09-03'),
(7676, 2, 'rwerte3', 34545456, '2019-09-03', 234323423, '2019-09-20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sectores`
--

CREATE TABLE `sectores` (
  `emp_sector` int(2) NOT NULL COMMENT 'Id del sector',
  `desc_sector` varchar(50) NOT NULL COMMENT 'Nombre del sector'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sectores`
--

INSERT INTO `sectores` (`emp_sector`, `desc_sector`) VALUES
(1, 'supervisor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serializable`
--

CREATE TABLE `serializable` (
  `ser_mac` varchar(12) NOT NULL COMMENT 'Número MAC de serializable',
  `ser_nombre` varchar(30) NOT NULL COMMENT 'Nombre del serializable',
  `ser_fecha_ultimo_ingreso` date NOT NULL COMMENT 'Fecha último ingreso del serializable',
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `ser_cant_minima` int(8) NOT NULL COMMENT 'Cantidad minima aceptada',
  `ser_cant_maxima` int(8) NOT NULL COMMENT 'Cantidad maxima aceptada'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serializable_movil`
--

CREATE TABLE `serializable_movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo`
--

CREATE TABLE `tipo` (
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `tip_descripcion` text NOT NULL COMMENT 'Descripcion del tipo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo`
--

INSERT INTO `tipo` (`tip_id`, `tip_descripcion`) VALUES
(1, 'Herramientas'),
(2, 'Serializables'),
(3, 'Materiales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usu_legajo` int(4) NOT NULL COMMENT 'Número de legajo del usuario',
  `usu_password` int(128) NOT NULL COMMENT 'Contraseña de usuario',
  `activo` tinyint(1) NOT NULL COMMENT 'Usuario activo o inactivo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD PRIMARY KEY (`art_id`),
  ADD KEY `tip_id` (`tip_id`);

--
-- Indices de la tabla `articulo_movil`
--
ALTER TABLE `articulo_movil`
  ADD KEY `mov_id` (`mov_id`,`art_id`),
  ADD KEY `art_id` (`art_id`);

--
-- Indices de la tabla `articulo_tecnico`
--
ALTER TABLE `articulo_tecnico`
  ADD KEY `usu_legajo` (`emp_legajo`),
  ADD KEY `usu_legajo_2` (`emp_legajo`,`art_id`),
  ADD KEY `art_id` (`art_id`);

--
-- Indices de la tabla `denuncias`
--
ALTER TABLE `denuncias`
  ADD PRIMARY KEY (`den_id`),
  ADD KEY `usu_legajo` (`emp_legajo`);

--
-- Indices de la tabla `detalle_denuncia_materiales`
--
ALTER TABLE `detalle_denuncia_materiales`
  ADD PRIMARY KEY (`den_id`),
  ADD KEY `art_id` (`art_id`);

--
-- Indices de la tabla `detalle_denuncia_serializables`
--
ALTER TABLE `detalle_denuncia_serializables`
  ADD KEY `den_id` (`den_id`,`ser_mac`),
  ADD KEY `ser_mac` (`ser_mac`);

--
-- Indices de la tabla `dupla_movil`
--
ALTER TABLE `dupla_movil`
  ADD PRIMARY KEY (`dup_mov_id`),
  ADD KEY `usu_legajo` (`emp_legajo`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`emp_legajo`);

--
-- Indices de la tabla `historial_materiales`
--
ALTER TABLE `historial_materiales`
  ADD KEY `art_id` (`art_id`);

--
-- Indices de la tabla `historial_sectores`
--
ALTER TABLE `historial_sectores`
  ADD PRIMARY KEY (`fecha_cambio_sector`),
  ADD KEY `emp_legajo` (`emp_legajo`),
  ADD KEY `emp_sector` (`emp_sector`);

--
-- Indices de la tabla `historial_serializables`
--
ALTER TABLE `historial_serializables`
  ADD PRIMARY KEY (`his_id`),
  ADD KEY `ser_mac` (`ser_mac`);

--
-- Indices de la tabla `movil`
--
ALTER TABLE `movil`
  ADD PRIMARY KEY (`mov_id`),
  ADD KEY `dup_mov_id` (`dup_mov_id`);

--
-- Indices de la tabla `sectores`
--
ALTER TABLE `sectores`
  ADD PRIMARY KEY (`emp_sector`);

--
-- Indices de la tabla `serializable`
--
ALTER TABLE `serializable`
  ADD PRIMARY KEY (`ser_mac`),
  ADD KEY `tip_id` (`tip_id`);

--
-- Indices de la tabla `serializable_movil`
--
ALTER TABLE `serializable_movil`
  ADD KEY `mov_id` (`mov_id`,`ser_mac`),
  ADD KEY `ser_mac` (`ser_mac`);

--
-- Indices de la tabla `tipo`
--
ALTER TABLE `tipo`
  ADD PRIMARY KEY (`tip_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD KEY `usu_legajo` (`usu_legajo`);

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
-- Filtros para la tabla `historial_materiales`
--
ALTER TABLE `historial_materiales`
  ADD CONSTRAINT `historial_materiales_ibfk_1` FOREIGN KEY (`art_id`) REFERENCES `articulo` (`art_id`);

--
-- Filtros para la tabla `historial_sectores`
--
ALTER TABLE `historial_sectores`
  ADD CONSTRAINT `historial_sectores_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`),
  ADD CONSTRAINT `historial_sectores_ibfk_2` FOREIGN KEY (`emp_sector`) REFERENCES `sectores` (`emp_sector`);

--
-- Filtros para la tabla `historial_serializables`
--
ALTER TABLE `historial_serializables`
  ADD CONSTRAINT `historial_serializables_ibfk_1` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`);

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
