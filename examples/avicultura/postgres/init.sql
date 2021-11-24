-- create base schema
/* DROP SCHEMA iot; */
CREATE SCHEMA IF NOT EXISTS iotdb;

-- create dim and ft tables
/* DROP TABLE iotdb.dm_device */
CREATE TABLE IF NOT EXISTS iotdb.dm_device (
    device_guid char(6) NOT NULL PRIMARY KEY,
    working_station char(1) NOT NULL,
    context char(30) NOT NULL,
    name char(40) NOT NULL
);

-- DROP TABLE iotdb.ft_temperature
CREATE TABLE IF NOT EXISTS iotdb.ft_temperature (
    guid char(40) NOT NULL PRIMARY KEY,
    device_guid char(6) NOT NULL,
    context char(30) NULL,
    value double precision NULL,
    timestamp integer NOT NULL,
    constraint fk_device_guid foreign key (device_guid) REFERENCES iotdb.dm_device (device_guid)
);

-- DROP TABLE iotdb.ft_ammonia
CREATE TABLE IF NOT EXISTS iotdb.ft_ammonia (
    guid char(40) NOT NULL PRIMARY KEY,
    device_guid char(6) NOT NULL,
    context char(30) NULL,
    value double precision NULL,
    timestamp integer NOT NULL,
    constraint fk_device_guid foreign key (device_guid) REFERENCES iotdb.dm_device (device_guid)
);

-- DROP TABLE iotdb.ft_luminosity
CREATE TABLE IF NOT EXISTS iotdb.ft_luminosity (
    guid char(40) NOT NULL PRIMARY KEY,
    device_guid char(6) NOT NULL,
    context char(30) NULL,
    value double precision NULL,
    timestamp integer NOT NULL,
    constraint fk_device_guid foreign key (device_guid) REFERENCES iotdb.dm_device (device_guid)
);

-- DROP TABLE iotdb.ft_humidity
CREATE TABLE IF NOT EXISTS iotdb.ft_humidity (
    guid char(40) NOT NULL PRIMARY KEY,
    device_guid char(6) NOT NULL,
    context char(30) NULL,
    value double precision NULL,
    timestamp integer NOT NULL,
    constraint fk_device_guid foreign key (device_guid) REFERENCES iotdb.dm_device (device_guid)
);

INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'893003','A','ammonia','ammonia-sensor-1A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'030863','A','ammonia','ammonia-sensor-2A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'015980','A','ammonia','ammonia-sensor-3A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'067476','A','ammonia','ammonia-sensor-4A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'375945','A','temperature','temperature-sensor-1A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'189287','A','temperature','temperature-sensor-2A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'416612','A','temperature','temperature-sensor-3A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'179818','A','luminosity','lum-sensor-1A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'429204','A','luminosity','lum-sensor-2A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'424296','A','humidity','humidity-sensor-1A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'848473','A','humidity','humidity-sensor-2A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'727584','A','humidity','humidity-sensor-3A');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'312065','B','ammonia','ammonia-sensor-1B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'318073','B','ammonia','ammonia-sensor-2B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'706892','B','ammonia','ammonia-sensor-3B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'477431','B','ammonia','ammonia-sensor-4B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'575775','B','ammonia','ammonia-sensor-5B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'603146','B','temperature','temp-sensor-4B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'173630','B','temperature','temp-sensor-3B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'970671','B','temperature','temp-sensor-2B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'354611','B','temperature','temp-sensor-5B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'591386','B','temperature','temp-sensor-1B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'454539','B','luminosity','lum-sensor-1B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'711524','B','luminosity','lum-sensor-2B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'669191','B','luminosity','lum-sensor-3B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'291819','B','humidity','humidity-sensor-3B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'339561','B','humidity','humidity-sensor-1B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'849195','B','humidity','humidity-sensor-2B');
INSERT INTO iotdb.dm_device(device_guid,working_station,context,name) VALUES (N'804086','B','humidity','humidity-sensor-4B');