SELECT issue_type, COUNT(*) AS volume
FROM contact_data
GROUP BY issue_type
ORDER BY volume DESC;

SELECT issue_type, AVG(escalated) AS escalation_rate
FROM contact_data
GROUP BY issue_type;

SELECT region, AVG(resolution_time_min) AS avg_resolution_time_min
FROM contact_data
GROUP BY region;
