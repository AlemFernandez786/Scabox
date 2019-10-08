-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 08-10-2019 a las 00:23:37
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
  `art_cant_min` int(8) NOT NULL COMMENT 'Cantidad minima aceptada',
  `art_cant_max` int(8) NOT NULL COMMENT 'Cantidad maxima aceptada',
  PRIMARY KEY (`art_id`),
  KEY `tip_id` (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`art_id`, `art_nombre`, `art_fecha_ultimo_ingreso`, `tip_id`, `art_cantidad`, `art_cant_min`, `art_cant_max`) VALUES
(1, 'Tornillo', '2019-09-26', 2, 2000, 1200, 5000),
(2, 'Cable', '2019-09-26', 2, 1500, 1000, 4000),
(3, 'Destornillador', '2019-09-26', 1, 120, 70, 150),
(4, 'Martillo', '2019-09-26', 1, 120, 70, 150),
(5, 'Clavo', '2019-08-03', 2, 1000, 2000, 5000);

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

--
-- Volcado de datos para la tabla `articulo_movil`
--

INSERT INTO `articulo_movil` (`mov_id`, `art_id`, `art_mov_cantidad`) VALUES
(1, 1, 50),
(1, 2, 50),
(2, 1, 50),
(2, 2, 50);

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

--
-- Volcado de datos para la tabla `articulo_tecnico`
--

INSERT INTO `articulo_tecnico` (`emp_legajo`, `art_id`, `art_tec_cantidad`) VALUES
(123, 1, 50),
(124, 1, 50),
(124, 2, 50);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `codigo_finalizacion`
--

DROP TABLE IF EXISTS `codigo_finalizacion`;
CREATE TABLE IF NOT EXISTS `codigo_finalizacion` (
  `cod_finalizacion` int(10) NOT NULL AUTO_INCREMENT COMMENT 'Codigo de finalizacion de un trabajo',
  `descripcion` varchar(150) NOT NULL COMMENT 'Nombre de la finalizacion',
  PRIMARY KEY (`cod_finalizacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consumo_serializable`
--

DROP TABLE IF EXISTS `consumo_serializable`;
CREATE TABLE IF NOT EXISTS `consumo_serializable` (
  `ser_id` int(2) NOT NULL COMMENT 'Id del tipo de serializable',
  `ser_cant` int(10) NOT NULL COMMENT 'Cantidad utilizada',
  `ser_fecha_consumo` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha en que se realizo el consumo',
  PRIMARY KEY (`ser_fecha_consumo`),
  KEY `ser_id` (`ser_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `consumo_serializable`
--

INSERT INTO `consumo_serializable` (`ser_id`, `ser_cant`, `ser_fecha_consumo`) VALUES
(3, 5, '2019-08-15 00:00:30'),
(3, 15, '2019-09-30 00:42:00'),
(4, 10, '2019-09-30 00:53:25'),
(3, 15, '2019-10-04 05:09:42');

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
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `mov_id` int(5) NOT NULL COMMENT 'Id del movil',
  UNIQUE KEY `emp_legajo` (`emp_legajo`),
  KEY `mov_id` (`mov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dupla_movil`
--

INSERT INTO `dupla_movil` (`emp_legajo`, `mov_id`) VALUES
(123, 1),
(124, 1),
(125, 2),
(126, 2);

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
  `fecha_ingreso` date DEFAULT NULL COMMENT 'Fecha de ingreso del empleado',
  PRIMARY KEY (`emp_legajo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`emp_legajo`, `emp_documento`, `emp_nombre`, `emp_apellido`, `fecha_ingreso`) VALUES
(123, 1234123, 'asdqwe', 'zxcsd', NULL),
(124, 37102639, 'Nicolas', 'Campos', '2019-09-25'),
(125, 37103556, 'adolfo', 'h', '2019-10-02'),
(126, 31789556, 'rodrigo', 'b', '2019-10-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados_serializables`
--

DROP TABLE IF EXISTS `estados_serializables`;
CREATE TABLE IF NOT EXISTS `estados_serializables` (
  `id_estado_ser` int(2) NOT NULL AUTO_INCREMENT,
  `des_estado` varchar(50) NOT NULL,
  PRIMARY KEY (`id_estado_ser`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estados_serializables`
--

INSERT INTO `estados_serializables` (`id_estado_ser`, `des_estado`) VALUES
(1, 'Listo para entregar'),
(2, 'Entregado'),
(3, 'Instalado'),
(4, 'Devolucion'),
(5, 'Extraviado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `finalizacion_trabajo`
--

DROP TABLE IF EXISTS `finalizacion_trabajo`;
CREATE TABLE IF NOT EXISTS `finalizacion_trabajo` (
  `cod_finalizacion` int(10) NOT NULL COMMENT 'Codigo de finalizacion de un trabajo',
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden del trabajo',
  KEY `cod_finalizacion` (`cod_finalizacion`),
  KEY `nro_orden` (`nro_orden`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_dupla`
--

DROP TABLE IF EXISTS `historial_dupla`;
CREATE TABLE IF NOT EXISTS `historial_dupla` (
  `his_dup_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Id del historial',
  `emp_legajo` int(4) NOT NULL,
  `mov_id` int(5) NOT NULL,
  `his_dup_fecha` datetime NOT NULL COMMENT 'Fecha en la que estuvo en dicho movil',
  PRIMARY KEY (`his_dup_id`),
  KEY `emp_legajo` (`emp_legajo`,`mov_id`),
  KEY `mov_id` (`mov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_materiales`
--

DROP TABLE IF EXISTS `historial_materiales`;
CREATE TABLE IF NOT EXISTS `historial_materiales` (
  `art_id` int(8) NOT NULL,
  `his_mat_cant` int(4) NOT NULL,
  `his_mat_fecha` datetime NOT NULL,
  PRIMARY KEY (`his_mat_fecha`),
  KEY `art_id` (`art_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `historial_materiales`
--

INSERT INTO `historial_materiales` (`art_id`, `his_mat_cant`, `his_mat_fecha`) VALUES
(2, 10, '2019-09-20 00:00:00'),
(1, 15, '2019-09-30 00:00:00'),
(5, 15, '2019-09-30 20:08:02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_sectores`
--

DROP TABLE IF EXISTS `historial_sectores`;
CREATE TABLE IF NOT EXISTS `historial_sectores` (
  `fecha_cambio_sector` datetime NOT NULL COMMENT 'Fecha del cambio',
  `emp_legajo` int(8) NOT NULL COMMENT 'Legajo del empleado',
  `emp_sector` int(2) NOT NULL COMMENT 'Sector en el que se encuentra el empleado',
  `motivo_cambio` varchar(255) NOT NULL COMMENT 'Motivo del cambio de sector',
  PRIMARY KEY (`fecha_cambio_sector`),
  KEY `emp_legajo` (`emp_legajo`),
  KEY `emp_sector` (`emp_sector`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_serializables`
--

DROP TABLE IF EXISTS `historial_serializables`;
CREATE TABLE IF NOT EXISTS `historial_serializables` (
  `his_id` int(4) NOT NULL AUTO_INCREMENT COMMENT 'ID del historial',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables',
  `ser_estado` int(2) NOT NULL COMMENT 'Estado del serializable',
  `ser_fecha_entrega` date DEFAULT NULL COMMENT 'Fecha de entrega del serializable',
  `ser_fecha_ultimo_estado` date NOT NULL COMMENT 'Fecha del ultimo estado',
  PRIMARY KEY (`his_id`),
  KEY `ser_mac` (`ser_mac`),
  KEY `ser_estado` (`ser_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `historial_serializables`
--

INSERT INTO `historial_serializables` (`his_id`, `ser_mac`, `ser_estado`, `ser_fecha_entrega`, `ser_fecha_ultimo_estado`) VALUES
(3, '1122AABB3333', 1, NULL, '2019-10-04'),
(6, '112233445566', 2, NULL, '2019-10-07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movil`
--

DROP TABLE IF EXISTS `movil`;
CREATE TABLE IF NOT EXISTS `movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `mov_patente` varchar(7) NOT NULL COMMENT 'Número de patente del móvil',
  `mov_seguro` int(8) NOT NULL COMMENT 'Número de póliza de seguro',
  `mov_vtv` date NOT NULL COMMENT 'Fecha de vencimiento de la VTV',
  `mov_tarjeta_verde` int(8) NOT NULL COMMENT 'Número de tarjeta verde',
  `mov_licencia` date NOT NULL COMMENT 'Fecha de vencimiento de la Licencia de conducir',
  PRIMARY KEY (`mov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `movil`
--

INSERT INTO `movil` (`mov_id`, `mov_patente`, `mov_seguro`, `mov_vtv`, `mov_tarjeta_verde`, `mov_licencia`) VALUES
(1, 'abc123', 12345678, '2019-09-26', 11112222, '2019-09-26'),
(2, 'abc124', 11223344, '2019-09-26', 22221111, '2019-09-26');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sectores`
--

DROP TABLE IF EXISTS `sectores`;
CREATE TABLE IF NOT EXISTS `sectores` (
  `emp_sector` int(2) NOT NULL COMMENT 'Id del sector',
  `desc_sector` varchar(50) NOT NULL COMMENT 'Nombre del sector',
  PRIMARY KEY (`emp_sector`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sectores`
--

INSERT INTO `sectores` (`emp_sector`, `desc_sector`) VALUES
(1, 'Herramientas'),
(2, 'Serializables'),
(3, 'Materiales'),
(4, 'Supervisor'),
(5, 'Control de calidad'),
(6, 'Tecnicos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serializable`
--

DROP TABLE IF EXISTS `serializable`;
CREATE TABLE IF NOT EXISTS `serializable` (
  `ser_mac` varchar(12) NOT NULL COMMENT 'Número MAC de serializable',
  `ser_fecha_ultimo_ingreso` date NOT NULL COMMENT 'Fecha último ingreso del serializable',
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  PRIMARY KEY (`ser_mac`),
  KEY `tip_id` (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `serializable`
--

INSERT INTO `serializable` (`ser_mac`, `ser_fecha_ultimo_ingreso`, `tip_id`) VALUES
('112233445566', '2019-09-30', 4),
('1122AABB3333', '2019-10-04', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serializable_movil`
--

DROP TABLE IF EXISTS `serializable_movil`;
CREATE TABLE IF NOT EXISTS `serializable_movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables',
  UNIQUE KEY `ser_mac_2` (`ser_mac`),
  KEY `mov_id` (`mov_id`,`ser_mac`),
  KEY `ser_mac` (`ser_mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_material`
--

DROP TABLE IF EXISTS `tipo_material`;
CREATE TABLE IF NOT EXISTS `tipo_material` (
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `tip_descripcion` text NOT NULL COMMENT 'Descripcion del tipo',
  PRIMARY KEY (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_material`
--

INSERT INTO `tipo_material` (`tip_id`, `tip_descripcion`) VALUES
(1, 'Herramientas'),
(2, 'Materiales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_serializable`
--

DROP TABLE IF EXISTS `tipo_serializable`;
CREATE TABLE IF NOT EXISTS `tipo_serializable` (
  `tipo_serializable` int(2) NOT NULL COMMENT 'Id de tipo de serializable',
  `desc_serializable` varchar(50) NOT NULL COMMENT 'Nombre del tipo de serializable',
  `cant_serializable` int(7) NOT NULL DEFAULT '0' COMMENT 'Cantidad actual en stock',
  `cant_min_ser` int(7) NOT NULL COMMENT 'Stock minimo',
  `cant_max_ser` int(7) NOT NULL COMMENT 'Stock maximo',
  PRIMARY KEY (`tipo_serializable`),
  UNIQUE KEY `desc_serializable` (`desc_serializable`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_serializable`
--

INSERT INTO `tipo_serializable` (`tipo_serializable`, `desc_serializable`, `cant_serializable`, `cant_min_ser`, `cant_max_ser`) VALUES
(3, 'Modem WiFi', 5, 25, 125),
(4, 'Decodificador', 6, 140, 500),
(5, 'Decodificador HD', 1, 250, 800);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajos_realizados`
--

DROP TABLE IF EXISTS `trabajos_realizados`;
CREATE TABLE IF NOT EXISTS `trabajos_realizados` (
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden',
  `domicilio` varchar(100) NOT NULL COMMENT 'Domicilio en que se realizo el trabajo',
  `mov_id` int(5) NOT NULL COMMENT 'Id del movil que realizo el trabajo',
  `observaciones` varchar(255) DEFAULT NULL COMMENT 'Observaciones',
  `fecha_trabajo` date NOT NULL COMMENT 'Fecha en que se realizo',
  `nom_cliente` varchar(50) NOT NULL COMMENT 'Nombre del abonado',
  `dni_cliente` int(8) NOT NULL COMMENT 'DNI del abonado',
  `nro_cliente` int(11) NOT NULL COMMENT 'Numero de cliente',
  PRIMARY KEY (`nro_orden`),
  KEY `mov_id` (`mov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajo_serializable`
--

DROP TABLE IF EXISTS `trabajo_serializable`;
CREATE TABLE IF NOT EXISTS `trabajo_serializable` (
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden del trabajo',
  `ser_mac` varchar(12) NOT NULL,
  KEY `nro_orden` (`nro_orden`),
  KEY `ser_mac` (`ser_mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usu_legajo` int(4) NOT NULL COMMENT 'Número de legajo del usuario',
  `usu_password` varchar(128) NOT NULL COMMENT 'Contraseña de usuario',
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
  ADD CONSTRAINT `articulo_ibfk_1` FOREIGN KEY (`tip_id`) REFERENCES `tipo_material` (`tip_id`);

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
-- Filtros para la tabla `consumo_serializable`
--
ALTER TABLE `consumo_serializable`
  ADD CONSTRAINT `consumo_serializable_ibfk_1` FOREIGN KEY (`ser_id`) REFERENCES `tipo_serializable` (`tipo_serializable`);

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
  ADD CONSTRAINT `dupla_movil_ibfk_2` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`),
  ADD CONSTRAINT `dupla_movil_ibfk_3` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `finalizacion_trabajo`
--
ALTER TABLE `finalizacion_trabajo`
  ADD CONSTRAINT `finalizacion_trabajo_ibfk_1` FOREIGN KEY (`nro_orden`) REFERENCES `trabajos_realizados` (`nro_orden`) ON UPDATE CASCADE,
  ADD CONSTRAINT `finalizacion_trabajo_ibfk_2` FOREIGN KEY (`cod_finalizacion`) REFERENCES `codigo_finalizacion` (`cod_finalizacion`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `historial_dupla`
--
ALTER TABLE `historial_dupla`
  ADD CONSTRAINT `historial_dupla_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `historial_dupla_ibfk_2` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`) ON UPDATE CASCADE;

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
  ADD CONSTRAINT `historial_serializables_ibfk_1` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`),
  ADD CONSTRAINT `historial_serializables_ibfk_2` FOREIGN KEY (`ser_estado`) REFERENCES `estados_serializables` (`id_estado_ser`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `serializable`
--
ALTER TABLE `serializable`
  ADD CONSTRAINT `serializable_ibfk_1` FOREIGN KEY (`tip_id`) REFERENCES `tipo_serializable` (`tipo_serializable`);

--
-- Filtros para la tabla `serializable_movil`
--
ALTER TABLE `serializable_movil`
  ADD CONSTRAINT `serializable_movil_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`),
  ADD CONSTRAINT `serializable_movil_ibfk_2` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`);

--
-- Filtros para la tabla `trabajos_realizados`
--
ALTER TABLE `trabajos_realizados`
  ADD CONSTRAINT `trabajos_realizados_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`);

--
-- Filtros para la tabla `trabajo_serializable`
--
ALTER TABLE `trabajo_serializable`
  ADD CONSTRAINT `trabajo_serializable_ibfk_1` FOREIGN KEY (`nro_orden`) REFERENCES `trabajos_realizados` (`nro_orden`) ON UPDATE CASCADE,
  ADD CONSTRAINT `trabajo_serializable_ibfk_2` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`usu_legajo`) REFERENCES `empleados` (`emp_legajo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
