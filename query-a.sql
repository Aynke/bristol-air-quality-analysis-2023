--
-- Database: `pollutions-db2`
--
-- --------------------------------------------------------
--
-- Table: `readings`, `stations
--
-- --------------------------------------------------------
--
-- Query to return the date/time, station name and the highest recorded value of nitrogen oxide (NOx) for the year 2019.
--

SELECT `location` AS 'Station Name', MAX(`nox`) AS 'nox',`datetime`FROM `readings`

JOIN `stations`
on `stationId-fk` = `stationID`

WHERE `datetime`>= '2019-01-01 00:00:00' 
AND `datetime` < '2020-01-01 00:00:00'