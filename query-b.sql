-- Database: `pollutions-db2`
--
-- --------------------------------------------------------
--
-- Table: `readings`, `stations`
--
-- --------------------------------------------------------
--
-- Query to return Return the mean values of PM2.5 & VPM2.5 by each station for the year 2019 
--for readings taken on or near 08:00 hours (peak traffic intensity).--

SELECT 
`stationId-fk`,
`location`, 
AVG(`vpm2.5`), 
AVG(`pm2.5`)

FROM `readings`

JOIN `stations`
on `stationId-fk` = `stationID`

WHERE YEAR(`datetime`) = '2019' AND (TIME(`datetime`) BETWEEN '730' AND '830')

GROUP BY `stationId-fk`, `location`