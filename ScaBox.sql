-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-10-2019 a las 06:56:21
-- Versión del servidor: 10.1.35-MariaDB
-- Versión de PHP: 7.2.9

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
(1, 'Conector Rg6', '2019-10-28', 2, 1200, 1000, 2000);

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
(1, 1, 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo_tecnico`
--

CREATE TABLE `articulo_tecnico` (
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `art_id` int(8) NOT NULL COMMENT 'ID del artículo',
  `art_tec_cantidad` int(3) NOT NULL COMMENT 'Cantidad de articulos del tecnico'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `articulo_tecnico`
--

INSERT INTO `articulo_tecnico` (`emp_legajo`, `art_id`, `art_tec_cantidad`) VALUES
(100, 1, 0),
(101, 1, 0),
(102, 1, 0),
(103, 1, 0),
(104, 1, 0),
(105, 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ausentes`
--

CREATE TABLE `ausentes` (
  `aus_id` int(11) NOT NULL COMMENT 'id de la ausencia',
  `emp_legajo` int(5) NOT NULL COMMENT 'legajo de empleado',
  `aus_fecha` date NOT NULL COMMENT 'fecha de la ausencia',
  `aus_justificacion` tinytext COMMENT 'presento justificativo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `codigo_finalizacion`
--

CREATE TABLE `codigo_finalizacion` (
  `cod_finalizacion` int(10) NOT NULL COMMENT 'Codigo de finalizacion de un trabajo',
  `descripcion` varchar(150) NOT NULL COMMENT 'Nombre de la finalizacion'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `codigo_finalizacion`
--

INSERT INTO `codigo_finalizacion` (`cod_finalizacion`, `descripcion`) VALUES
(120, 'Instalación acometida'),
(121, 'Instalacion boca modem'),
(122, 'Instalacion boca catv'),
(123, 'instalacion acometida + boca modem'),
(124, 'Instalacion acometida + boca catv'),
(125, 'Instalacion Modem WIfi'),
(400, 'Ausente'),
(403, 'No lo quiere'),
(410, 'Impedimento Técnico'),
(412, 'Zona peligrosa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consumo_serializable`
--

CREATE TABLE `consumo_serializable` (
  `ser_id` int(2) NOT NULL COMMENT 'Id del tipo de serializable',
  `ser_cant` int(10) NOT NULL COMMENT 'Cantidad utilizada',
  `ser_fecha_consumo` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha en que se realizo el consumo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denuncias`
--

CREATE TABLE `denuncias` (
  `den_id` int(4) NOT NULL COMMENT 'ID de la denuncia',
  `den_numero_folio` int(30) NOT NULL COMMENT 'Numero de folio de la denuncia',
  `den_numero_acta` int(30) NOT NULL COMMENT 'Numero de acta de la denuncia',
  `den_numero_legajo` int(10) NOT NULL COMMENT 'Número de legajo de denuncia',
  `den_comisaria` varchar(20) COLLATE latin1_spanish_ci NOT NULL COMMENT 'Nombre de la comisaria',
  `den_fecha_siniestro` date NOT NULL COMMENT 'Fecha del siniestro',
  `den_fecha_ingreso` date NOT NULL COMMENT 'Fecha de ingreso de denuncia',
  `mov_id` int(5) NOT NULL COMMENT 'Movil del siniestro'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descuentos`
--

CREATE TABLE `descuentos` (
  `des_id` int(11) NOT NULL COMMENT 'id del descuento',
  `emp_legajo` int(4) NOT NULL COMMENT 'legajo de empleado',
  `des_importe` int(8) NOT NULL COMMENT 'importe a descontar',
  `des_fecha` date NOT NULL COMMENT 'fecha del descuento'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_denuncia_empleados`
--

CREATE TABLE `detalle_denuncia_empleados` (
  `den_id` int(4) NOT NULL,
  `emp_legajo` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `emp_legajo` int(4) NOT NULL COMMENT 'Legajo del empleado',
  `mov_id` int(5) NOT NULL COMMENT 'Id del movil'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dupla_movil`
--

INSERT INTO `dupla_movil` (`emp_legajo`, `mov_id`) VALUES
(101, 1),
(104, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `emp_legajo` int(4) NOT NULL COMMENT 'Número de legajo de los empleados',
  `emp_documento` int(8) NOT NULL COMMENT 'Número de DNI de los empleados',
  `emp_nombre` varchar(50) NOT NULL COMMENT 'Nombre del empleado',
  `emp_apellido` varchar(50) NOT NULL COMMENT 'Apellido de los empleados',
  `fecha_ingreso` date DEFAULT NULL COMMENT 'Fecha de ingreso del empleado'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`emp_legajo`, `emp_documento`, `emp_nombre`, `emp_apellido`, `fecha_ingreso`) VALUES
(100, 32987654, 'Juan', 'Supervisor', '2015-07-10'),
(101, 32654987, 'Luis', 'Tecnico', '2019-10-27'),
(102, 31326985, 'Alejandro ', 'Fernandez', '2019-10-27'),
(103, 38321654, 'Nicolas', 'Campos', '2019-10-27'),
(104, 12345678, 'Marcos', 'Perez', '2019-10-28'),
(105, 12345679, 'Marcos', 'Perez', '2019-10-28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entradas_salidas`
--

CREATE TABLE `entradas_salidas` (
  `eys_id` int(11) NOT NULL COMMENT 'id de entrada y salida',
  `emp_legajo` int(4) NOT NULL COMMENT 'legajo de empleado',
  `eys_fecha` date NOT NULL COMMENT 'Fecha',
  `eys_entrada` time NOT NULL COMMENT 'horario de entrada',
  `eys_salida` time NOT NULL COMMENT 'horario de salida'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `estados`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `estados` (
`ser_mac` varchar(12)
,`ultimo_estado` int(4)
,`primer_estado` date
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados_serializables`
--

CREATE TABLE `estados_serializables` (
  `id_estado_ser` int(2) NOT NULL,
  `des_estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

CREATE TABLE `finalizacion_trabajo` (
  `cod_finalizacion` varchar(20) NOT NULL COMMENT 'Codigo de finalizacion de un trabajo',
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden del trabajo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_dupla`
--

CREATE TABLE `historial_dupla` (
  `his_dup_id` int(11) NOT NULL COMMENT 'Id del historial',
  `emp_legajo` int(4) NOT NULL,
  `mov_id` int(5) NOT NULL,
  `his_dup_fecha` datetime NOT NULL COMMENT 'Fecha en la que estuvo en dicho movil'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_materiales`
--

CREATE TABLE `historial_materiales` (
  `art_id` int(8) NOT NULL,
  `his_mat_cant` int(4) NOT NULL,
  `his_mat_fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

--
-- Volcado de datos para la tabla `historial_sectores`
--

INSERT INTO `historial_sectores` (`fecha_cambio_sector`, `emp_legajo`, `emp_sector`, `motivo_cambio`) VALUES
('2019-10-27 00:00:00', 100, 4, 'ALTA'),
('2019-10-27 22:31:28', 101, 6, 'Alta'),
('2019-10-27 23:34:11', 102, 3, 'Cambio'),
('2019-10-27 23:34:24', 103, 2, 'Cambio'),
('2019-10-28 02:10:31', 104, 6, 'Alta'),
('2019-10-28 02:11:58', 105, 5, 'Cambio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_serializables`
--

CREATE TABLE `historial_serializables` (
  `his_id` int(4) NOT NULL COMMENT 'ID del historial',
  `ser_mac` varchar(12) NOT NULL COMMENT 'MAC de serializables',
  `ser_estado` int(2) NOT NULL COMMENT 'Estado del serializable',
  `ser_fecha_entrega` date DEFAULT NULL COMMENT 'Fecha de entrega del serializable',
  `ser_fecha_ultimo_estado` date NOT NULL COMMENT 'Fecha del ultimo estado'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `historial_serializables`
--

INSERT INTO `historial_serializables` (`his_id`, `ser_mac`, `ser_estado`, `ser_fecha_entrega`, `ser_fecha_ultimo_estado`) VALUES
(7, '1122334455AA', 1, NULL, '2019-10-28'),
(8, '1122334455AA', 3, NULL, '2019-10-28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movil`
--

CREATE TABLE `movil` (
  `mov_id` int(5) NOT NULL COMMENT 'ID del movil',
  `mov_patente` varchar(7) NOT NULL COMMENT 'Número de patente del móvil',
  `mov_seguro` int(8) NOT NULL COMMENT 'Número de póliza de seguro',
  `mov_vtv` date NOT NULL COMMENT 'Fecha de vencimiento de la VTV',
  `mov_tarjeta_verde` int(8) NOT NULL COMMENT 'Número de tarjeta verde',
  `mov_licencia` date NOT NULL COMMENT 'Fecha de vencimiento de la Licencia de conducir',
  `emp_legajo` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `movil`
--

INSERT INTO `movil` (`mov_id`, `mov_patente`, `mov_seguro`, `mov_vtv`, `mov_tarjeta_verde`, `mov_licencia`, `emp_legajo`) VALUES
(1, 'ABC123', 1234567, '2020-01-17', 123123123, '2021-04-16', 101);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salidas_diarias`
--

CREATE TABLE `salidas_diarias` (
  `saldias_id` int(10) NOT NULL,
  `Fecha` date NOT NULL COMMENT 'Fecha de salida',
  `emp_legajo` int(4) NOT NULL,
  `estado_tecnico` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `salidas_diarias`
--

INSERT INTO `salidas_diarias` (`saldias_id`, `Fecha`, `emp_legajo`, `estado_tecnico`) VALUES
(17, '2019-10-28', 100, 'Supervisor'),
(18, '2019-10-28', 101, '1'),
(19, '2019-10-28', 102, 'Materiales'),
(20, '2019-10-28', 103, 'Serializable'),
(22, '2019-10-28', 105, 'Calidad'),
(24, '2019-10-28', 104, '1');

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

CREATE TABLE `serializable` (
  `ser_mac` varchar(12) NOT NULL COMMENT 'Número MAC de serializable',
  `ser_fecha_ultimo_ingreso` date NOT NULL COMMENT 'Fecha último ingreso del serializable',
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `serializable`
--

INSERT INTO `serializable` (`ser_mac`, `ser_fecha_ultimo_ingreso`, `tip_id`) VALUES
('1122334455AA', '2019-10-28', 1);

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
-- Estructura de tabla para la tabla `tipo_material`
--

CREATE TABLE `tipo_material` (
  `tip_id` int(2) NOT NULL COMMENT 'ID del tipo',
  `tip_descripcion` text NOT NULL COMMENT 'Descripcion del tipo'
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

CREATE TABLE `tipo_serializable` (
  `tipo_serializable` int(2) NOT NULL COMMENT 'Id de tipo de serializable',
  `desc_serializable` varchar(50) NOT NULL COMMENT 'Nombre del tipo de serializable',
  `cant_serializable` int(7) NOT NULL DEFAULT '0' COMMENT 'Cantidad actual en stock',
  `cant_min_ser` int(7) NOT NULL COMMENT 'Stock minimo',
  `cant_max_ser` int(7) NOT NULL COMMENT 'Stock maximo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_serializable`
--

INSERT INTO `tipo_serializable` (`tipo_serializable`, `desc_serializable`, `cant_serializable`, `cant_min_ser`, `cant_max_ser`) VALUES
(1, 'Modem WiFi', 1, 20, 50),
(2, 'Decodificador FLOW', 0, 20, 50);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajos_controlados`
--

CREATE TABLE `trabajos_controlados` (
  `nro_orden` int(10) NOT NULL COMMENT 'nro de orden de trabajo',
  `con_fecha` date NOT NULL COMMENT 'fecha de control',
  `con_observaciones` varchar(255) DEFAULT NULL COMMENT 'observaciones dle trabajo realizado'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajos_realizados`
--

CREATE TABLE `trabajos_realizados` (
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden',
  `domicilio` varchar(100) NOT NULL COMMENT 'Domicilio en que se realizo el trabajo',
  `mov_id` int(5) NOT NULL COMMENT 'Id del movil que realizo el trabajo',
  `observaciones` varchar(255) DEFAULT NULL COMMENT 'Observaciones',
  `fecha_trabajo` date NOT NULL COMMENT 'Fecha en que se realizo',
  `nom_cliente` varchar(50) DEFAULT NULL COMMENT 'Nombre del abonado',
  `dni_cliente` int(8) DEFAULT NULL COMMENT 'DNI del abonado',
  `nro_cliente` int(11) DEFAULT NULL COMMENT 'Numero de cliente'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `trabajos_realizados`
--

INSERT INTO `trabajos_realizados` (`nro_orden`, `domicilio`, `mov_id`, `observaciones`, `fecha_trabajo`, `nom_cliente`, `dni_cliente`, `nro_cliente`) VALUES
(123456789, 'Paraguay 2233', 1, NULL, '2019-10-28', 'Ramiro Sanchez', 34483118, 34483118);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajo_materiales`
--

CREATE TABLE `trabajo_materiales` (
  `nro_orden` int(10) NOT NULL COMMENT 'numero de orden',
  `art_id` int(8) NOT NULL COMMENT 'id del articulo',
  `ot_art_cantidad` int(10) NOT NULL COMMENT 'cantidad consumida'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `trabajo_materiales`
--

INSERT INTO `trabajo_materiales` (`nro_orden`, `art_id`, `ot_art_cantidad`) VALUES
(123456789, 1, 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajo_serializable`
--

CREATE TABLE `trabajo_serializable` (
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden del trabajo',
  `ser_mac` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `trabajo_serializable`
--

INSERT INTO `trabajo_serializable` (`nro_orden`, `ser_mac`) VALUES
(123456789, '1122334455AA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usu_legajo` int(4) NOT NULL COMMENT 'Número de legajo del usuario',
  `usu_password` varchar(128) NOT NULL COMMENT 'Contraseña de usuario',
  `activo` tinyint(1) NOT NULL COMMENT 'Usuario activo o inactivo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usu_legajo`, `usu_password`, `activo`) VALUES
(100, '565656', 1),
(102, '565656', 1),
(103, '565656', 1),
(105, '565656', 1);

-- --------------------------------------------------------

--
-- Estructura para la vista `estados`
--
DROP TABLE IF EXISTS `estados`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `estados`  AS  (select `historial_serializables`.`ser_mac` AS `ser_mac`,max(`historial_serializables`.`his_id`) AS `ultimo_estado`,min(`historial_serializables`.`ser_fecha_ultimo_estado`) AS `primer_estado` from `historial_serializables` group by `historial_serializables`.`ser_mac`) ;

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
-- Indices de la tabla `ausentes`
--
ALTER TABLE `ausentes`
  ADD PRIMARY KEY (`aus_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

--
-- Indices de la tabla `codigo_finalizacion`
--
ALTER TABLE `codigo_finalizacion`
  ADD PRIMARY KEY (`cod_finalizacion`);

--
-- Indices de la tabla `consumo_serializable`
--
ALTER TABLE `consumo_serializable`
  ADD PRIMARY KEY (`ser_fecha_consumo`),
  ADD KEY `ser_id` (`ser_id`);

--
-- Indices de la tabla `denuncias`
--
ALTER TABLE `denuncias`
  ADD PRIMARY KEY (`den_id`),
  ADD KEY `mov_id` (`mov_id`);

--
-- Indices de la tabla `descuentos`
--
ALTER TABLE `descuentos`
  ADD PRIMARY KEY (`des_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

--
-- Indices de la tabla `detalle_denuncia_empleados`
--
ALTER TABLE `detalle_denuncia_empleados`
  ADD KEY `den_id` (`den_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

--
-- Indices de la tabla `detalle_denuncia_materiales`
--
ALTER TABLE `detalle_denuncia_materiales`
  ADD KEY `art_id` (`art_id`),
  ADD KEY `den_id` (`den_id`);

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
  ADD UNIQUE KEY `emp_legajo` (`emp_legajo`),
  ADD KEY `mov_id` (`mov_id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`emp_legajo`);

--
-- Indices de la tabla `entradas_salidas`
--
ALTER TABLE `entradas_salidas`
  ADD PRIMARY KEY (`eys_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

--
-- Indices de la tabla `estados_serializables`
--
ALTER TABLE `estados_serializables`
  ADD PRIMARY KEY (`id_estado_ser`);

--
-- Indices de la tabla `finalizacion_trabajo`
--
ALTER TABLE `finalizacion_trabajo`
  ADD KEY `nro_orden` (`nro_orden`);

--
-- Indices de la tabla `historial_dupla`
--
ALTER TABLE `historial_dupla`
  ADD PRIMARY KEY (`his_dup_id`),
  ADD KEY `emp_legajo` (`emp_legajo`,`mov_id`),
  ADD KEY `mov_id` (`mov_id`);

--
-- Indices de la tabla `historial_materiales`
--
ALTER TABLE `historial_materiales`
  ADD PRIMARY KEY (`his_mat_fecha`),
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
  ADD KEY `ser_mac` (`ser_mac`),
  ADD KEY `ser_estado` (`ser_estado`);

--
-- Indices de la tabla `movil`
--
ALTER TABLE `movil`
  ADD PRIMARY KEY (`mov_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

--
-- Indices de la tabla `salidas_diarias`
--
ALTER TABLE `salidas_diarias`
  ADD PRIMARY KEY (`saldias_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

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
  ADD UNIQUE KEY `ser_mac_2` (`ser_mac`),
  ADD KEY `mov_id` (`mov_id`,`ser_mac`),
  ADD KEY `ser_mac` (`ser_mac`);

--
-- Indices de la tabla `tipo_material`
--
ALTER TABLE `tipo_material`
  ADD PRIMARY KEY (`tip_id`);

--
-- Indices de la tabla `tipo_serializable`
--
ALTER TABLE `tipo_serializable`
  ADD PRIMARY KEY (`tipo_serializable`),
  ADD UNIQUE KEY `desc_serializable` (`desc_serializable`);

--
-- Indices de la tabla `trabajos_controlados`
--
ALTER TABLE `trabajos_controlados`
  ADD KEY `nro_orden` (`nro_orden`);

--
-- Indices de la tabla `trabajos_realizados`
--
ALTER TABLE `trabajos_realizados`
  ADD PRIMARY KEY (`nro_orden`),
  ADD KEY `mov_id` (`mov_id`);

--
-- Indices de la tabla `trabajo_materiales`
--
ALTER TABLE `trabajo_materiales`
  ADD KEY `nro_orden` (`nro_orden`),
  ADD KEY `art_id` (`art_id`);

--
-- Indices de la tabla `trabajo_serializable`
--
ALTER TABLE `trabajo_serializable`
  ADD KEY `nro_orden` (`nro_orden`),
  ADD KEY `ser_mac` (`ser_mac`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD KEY `usu_legajo` (`usu_legajo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ausentes`
--
ALTER TABLE `ausentes`
  MODIFY `aus_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id de la ausencia';

--
-- AUTO_INCREMENT de la tabla `codigo_finalizacion`
--
ALTER TABLE `codigo_finalizacion`
  MODIFY `cod_finalizacion` int(10) NOT NULL AUTO_INCREMENT COMMENT 'Codigo de finalizacion de un trabajo', AUTO_INCREMENT=413;

--
-- AUTO_INCREMENT de la tabla `denuncias`
--
ALTER TABLE `denuncias`
  MODIFY `den_id` int(4) NOT NULL AUTO_INCREMENT COMMENT 'ID de la denuncia';

--
-- AUTO_INCREMENT de la tabla `descuentos`
--
ALTER TABLE `descuentos`
  MODIFY `des_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id del descuento';

--
-- AUTO_INCREMENT de la tabla `entradas_salidas`
--
ALTER TABLE `entradas_salidas`
  MODIFY `eys_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id de entrada y salida', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `estados_serializables`
--
ALTER TABLE `estados_serializables`
  MODIFY `id_estado_ser` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `historial_dupla`
--
ALTER TABLE `historial_dupla`
  MODIFY `his_dup_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Id del historial';

--
-- AUTO_INCREMENT de la tabla `historial_serializables`
--
ALTER TABLE `historial_serializables`
  MODIFY `his_id` int(4) NOT NULL AUTO_INCREMENT COMMENT 'ID del historial', AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `salidas_diarias`
--
ALTER TABLE `salidas_diarias`
  MODIFY `saldias_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

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
-- Filtros para la tabla `ausentes`
--
ALTER TABLE `ausentes`
  ADD CONSTRAINT `ausentes_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `consumo_serializable`
--
ALTER TABLE `consumo_serializable`
  ADD CONSTRAINT `consumo_serializable_ibfk_1` FOREIGN KEY (`ser_id`) REFERENCES `tipo_serializable` (`tipo_serializable`);

--
-- Filtros para la tabla `denuncias`
--
ALTER TABLE `denuncias`
  ADD CONSTRAINT `denuncias_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`);

--
-- Filtros para la tabla `descuentos`
--
ALTER TABLE `descuentos`
  ADD CONSTRAINT `descuentos_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `detalle_denuncia_empleados`
--
ALTER TABLE `detalle_denuncia_empleados`
  ADD CONSTRAINT `detalle_denuncia_empleados_ibfk_2` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`),
  ADD CONSTRAINT `detalle_denuncia_empleados_ibfk_3` FOREIGN KEY (`den_id`) REFERENCES `denuncias` (`den_id`);

--
-- Filtros para la tabla `detalle_denuncia_materiales`
--
ALTER TABLE `detalle_denuncia_materiales`
  ADD CONSTRAINT `detalle_denuncia_materiales_ibfk_2` FOREIGN KEY (`art_id`) REFERENCES `articulo` (`art_id`),
  ADD CONSTRAINT `detalle_denuncia_materiales_ibfk_3` FOREIGN KEY (`den_id`) REFERENCES `denuncias` (`den_id`);

--
-- Filtros para la tabla `detalle_denuncia_serializables`
--
ALTER TABLE `detalle_denuncia_serializables`
  ADD CONSTRAINT `detalle_denuncia_serializables_ibfk_2` FOREIGN KEY (`ser_mac`) REFERENCES `serializable` (`ser_mac`),
  ADD CONSTRAINT `detalle_denuncia_serializables_ibfk_3` FOREIGN KEY (`den_id`) REFERENCES `denuncias` (`den_id`);

--
-- Filtros para la tabla `dupla_movil`
--
ALTER TABLE `dupla_movil`
  ADD CONSTRAINT `dupla_movil_ibfk_2` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`),
  ADD CONSTRAINT `dupla_movil_ibfk_3` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `entradas_salidas`
--
ALTER TABLE `entradas_salidas`
  ADD CONSTRAINT `entradas_salidas_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `finalizacion_trabajo`
--
ALTER TABLE `finalizacion_trabajo`
  ADD CONSTRAINT `finalizacion_trabajo_ibfk_1` FOREIGN KEY (`nro_orden`) REFERENCES `trabajos_realizados` (`nro_orden`) ON UPDATE CASCADE;

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
-- Filtros para la tabla `movil`
--
ALTER TABLE `movil`
  ADD CONSTRAINT `movil_ibfk_1` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

--
-- Filtros para la tabla `salidas_diarias`
--
ALTER TABLE `salidas_diarias`
  ADD CONSTRAINT `salidas_diarias_ibfk_2` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

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
-- Filtros para la tabla `trabajos_controlados`
--
ALTER TABLE `trabajos_controlados`
  ADD CONSTRAINT `trabajos_controlados_ibfk_1` FOREIGN KEY (`nro_orden`) REFERENCES `trabajos_realizados` (`nro_orden`);

--
-- Filtros para la tabla `trabajos_realizados`
--
ALTER TABLE `trabajos_realizados`
  ADD CONSTRAINT `trabajos_realizados_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`);

--
-- Filtros para la tabla `trabajo_materiales`
--
ALTER TABLE `trabajo_materiales`
  ADD CONSTRAINT `trabajo_materiales_ibfk_1` FOREIGN KEY (`nro_orden`) REFERENCES `trabajos_realizados` (`nro_orden`),
  ADD CONSTRAINT `trabajo_materiales_ibfk_2` FOREIGN KEY (`art_id`) REFERENCES `articulo` (`art_id`);

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
