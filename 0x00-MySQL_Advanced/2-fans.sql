-- Rank the countries based on the non-unique fans country

CREATE TEMPORARY TABLE temp_fans_table AS
SELECT
    origin,
    COUNT(fan_id) AS nb_fans
FROM
    bands
GROUP BY
    origin;

SELECT
    origin,
    nb_fans,
    RANK() OVER (ORDER BY nb_fans DESC) AS rank
FROM
    temp_fans_table
ORDER BY
    rank;

DROP TEMPORARY TABLE IF EXISTS temp_fans_table;
