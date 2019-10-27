-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-10-2019 a las 20:09:00
-- Versión del servidor: 10.1.32-MariaDB
-- Versión de PHP: 7.2.5

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
(1, 'Tornillo', '2019-10-26', 2, 1899, 1200, 5000),
(2, 'Cable', '2019-09-26', 2, 1500, 1000, 4000),
(3, 'Destornillador', '2019-09-26', 1, 120, 70, 150),
(4, 'Martillo', '2019-09-26', 1, 120, 70, 150),
(5, 'Clavo', '2019-08-03', 2, 1000, 2000, 5000);

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
(1, 1, 1101),
(1, 2, 10),
(1, 5, 50),
(2, 1, 151),
(2, 2, 10),
(2, 5, 50),
(3, 1, 0),
(3, 2, 10),
(3, 5, 50),
(4, 1, 0),
(4, 2, 10),
(4, 5, 50);

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
(123, 3, 2),
(123, 4, 5),
(124, 3, 4),
(124, 4, 2);

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
(125, 'Instalacion Modem WIfi');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consumo_serializable`
--

CREATE TABLE `consumo_serializable` (
  `ser_id` int(2) NOT NULL COMMENT 'Id del tipo de serializable',
  `ser_cant` int(10) NOT NULL COMMENT 'Cantidad utilizada',
  `ser_fecha_consumo` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha en que se realizo el consumo'
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

CREATE TABLE `denuncias` (
  `den_id` int(4) NOT NULL COMMENT 'ID de la denuncia',
  `den_numero_folio` int(30) NOT NULL COMMENT 'Numero de folio de la denuncia',
  `den_numero_acta` int(30) NOT NULL COMMENT 'Numero de acta de la denuncia',
  `den_numero_legajo` int(10) NOT NULL,
  `den_comisaria` varchar(20) COLLATE latin1_spanish_ci NOT NULL COMMENT 'Nombre de la comisaria',
  `den_fecha_siniestro` date NOT NULL COMMENT 'Fecha del siniestro',
  `den_fecha_ingreso` date NOT NULL COMMENT 'Fecha de ingreso de denuncia',
  `mov_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

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
(123, 1),
(124, 1),
(125, 2),
(126, 2),
(127, 3),
(131, 3),
(129, 4),
(130, 4);

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
(123, 1234123, 'asdqwe', 'zxcsd', NULL),
(124, 37102639, 'Nicolas', 'Campos', '2019-09-25'),
(125, 37103556, 'adolfo', 'h', '2019-10-02'),
(126, 31789556, 'rodrigo', 'b', '2019-10-02'),
(127, 11111, 'pri', 'pri', '2019-10-09'),
(128, 22222, 'sec', 'seg', '2019-10-09'),
(129, 3333, 'tre', 'ter', '2019-10-09'),
(130, 444, 'cuarrr', 'cua', '2019-10-09'),
(131, 8528, 'cuchu', 'cambiasso', '2019-10-09');

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

--
-- Volcado de datos para la tabla `finalizacion_trabajo`
--

INSERT INTO `finalizacion_trabajo` (`cod_finalizacion`, `nro_orden`) VALUES
('120, 121', 11111111),
('122', 22222222),
('123, 125', 33333333),
('121, 122, 121', 44444444),
('123,123', 32132121),
('120, 121', 11111111),
('122', 22222222),
('123, 125', 33333333),
('121, 122, 121', 44444444),
('123,123', 32132121);

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

--
-- Volcado de datos para la tabla `historial_dupla`
--

INSERT INTO `historial_dupla` (`his_dup_id`, `emp_legajo`, `mov_id`, `his_dup_fecha`) VALUES
(1, 128, 3, '2019-10-09 22:24:16'),
(2, 130, 4, '2019-10-09 22:25:04'),
(3, 129, 4, '2019-10-15 22:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_materiales`
--

CREATE TABLE `historial_materiales` (
  `art_id` int(8) NOT NULL,
  `his_mat_cant` int(4) NOT NULL,
  `his_mat_fecha` datetime NOT NULL
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
('2019-10-09 14:49:40', 127, 6, 'Alta'),
('2019-10-09 14:49:52', 128, 6, 'Alta'),
('2019-10-09 14:50:01', 129, 6, 'Alta'),
('2019-10-09 14:50:08', 130, 6, 'Alta'),
('2019-10-09 14:50:57', 131, 1, 'Cambio');

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
(3, '1122AABB3333', 1, NULL, '2019-10-04'),
(6, '112233445566', 2, NULL, '2019-10-07');

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
(1, 'abc123', 12345678, '2019-09-26', 11112222, '2019-09-26', 123),
(2, 'abc124', 11223344, '2019-11-26', 22221111, '2019-11-26', 124),
(3, 'w23e4r', 2344321, '2020-07-11', 2345, '2025-07-16', 125),
(4, 'w2e3r4', 444, '2020-03-14', 2345555, '2020-03-14', 131),
(5, 'qwe123', 123321, '2019-10-21', 213321, '2019-10-21', 128);

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
(1, '2019-10-11', 124, '2'),
(2, '2019-10-14', 123, '4'),
(5, '2019-10-16', 129, '3'),
(6, '2019-10-16', 131, '3'),
(9, '2019-10-16', 124, 'Vacaciones'),
(18, '2019-10-16', 130, 'Enfermedad'),
(19, '2019-10-17', 130, 'En Base'),
(43, '2019-10-17', 129, '3'),
(44, '2019-10-17', 131, '3'),
(45, '2019-10-17', 124, 'Vacaciones'),
(146, '2019-10-17', 129, '3'),
(147, '2019-10-17', 131, '3'),
(148, '2019-10-17', 124, 'Vacaciones'),
(149, '2019-10-17', 130, 'Enfermedad'),
(150, '2019-10-15', 125, '1'),
(151, '2019-10-10', 123, '2'),
(152, '2019-10-22', 123, '1'),
(153, '2019-10-22', 124, '1'),
(154, '2019-10-22', 125, '2'),
(155, '2019-10-22', 126, '2'),
(156, '2019-10-22', 129, '4'),
(157, '2019-10-22', 130, '4'),
(160, '2019-10-22', 131, '3');

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
('112233445566', '2019-09-30', 4),
('1122AABB3333', '2019-10-04', 4);

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
(3, 'Modem WiFi', 5, 25, 125),
(4, 'Decodificador', 6, 140, 500),
(5, 'Decodificador HD', 1, 250, 800);

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
(11111111, 'calle uno 111', 1, 'poste roto', '2019-10-15', 'Primerisimo', 11111111, 1111111),
(22222222, 'calle dos 222', 2, '	', '2019-10-10', 'Segundisimo', 222222222, 22222222),
(32132121, 'nose 234', 3, NULL, '2019-10-16', 'elpibito', 32659814, 3216548),
(33333333, 'calle 3', 3, '', '2019-10-14', 'Terceri', 0, 0),
(44444444, 'Calle 4 444', 4, 'El sandaime', '2019-10-14', 'El Cuaro Hokage', 4444444, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajo_serializable`
--

CREATE TABLE `trabajo_serializable` (
  `nro_orden` int(10) NOT NULL COMMENT 'Numero de orden del trabajo',
  `ser_mac` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
(131, '565656', 1);

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
-- Indices de la tabla `detalle_denuncia_empleados`
--
ALTER TABLE `detalle_denuncia_empleados`
  ADD KEY `den_id` (`den_id`),
  ADD KEY `emp_legajo` (`emp_legajo`);

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
  ADD UNIQUE KEY `emp_legajo` (`emp_legajo`),
  ADD KEY `mov_id` (`mov_id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`emp_legajo`);

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
-- Indices de la tabla `trabajos_realizados`
--
ALTER TABLE `trabajos_realizados`
  ADD PRIMARY KEY (`nro_orden`),
  ADD KEY `mov_id` (`mov_id`);

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
-- AUTO_INCREMENT de la tabla `codigo_finalizacion`
--
ALTER TABLE `codigo_finalizacion`
  MODIFY `cod_finalizacion` int(10) NOT NULL AUTO_INCREMENT COMMENT 'Codigo de finalizacion de un trabajo', AUTO_INCREMENT=126;

--
-- AUTO_INCREMENT de la tabla `estados_serializables`
--
ALTER TABLE `estados_serializables`
  MODIFY `id_estado_ser` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `historial_dupla`
--
ALTER TABLE `historial_dupla`
  MODIFY `his_dup_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Id del historial', AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `historial_serializables`
--
ALTER TABLE `historial_serializables`
  MODIFY `his_id` int(4) NOT NULL AUTO_INCREMENT COMMENT 'ID del historial', AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `salidas_diarias`
--
ALTER TABLE `salidas_diarias`
  MODIFY `saldias_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=166;

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
  ADD CONSTRAINT `denuncias_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `movil` (`mov_id`);

--
-- Filtros para la tabla `detalle_denuncia_empleados`
--
ALTER TABLE `detalle_denuncia_empleados`
  ADD CONSTRAINT `detalle_denuncia_empleados_ibfk_1` FOREIGN KEY (`den_id`) REFERENCES `denuncias` (`den_id`),
  ADD CONSTRAINT `detalle_denuncia_empleados_ibfk_2` FOREIGN KEY (`emp_legajo`) REFERENCES `empleados` (`emp_legajo`);

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
