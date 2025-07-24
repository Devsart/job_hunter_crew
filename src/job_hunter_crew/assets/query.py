import os
from datetime import datetime, timedelta

job_roles = ["AI Engineer", "Data Scientist", "Machine Learning Engineer", "AI Researcher", "AI Developer"]
sites_to_search = ["jobs.google.com", "linkedin.com/jobs", "weworkremotely.com", "remotive.io", "angel.co"]
today_date = datetime.now().strftime("%Y-%m-%d")
days_to_search = 3
end_date = (datetime.now() - timedelta(days=days_to_search)).strftime("%Y-%m-%d")
job_roles_query = ' OR '.join([f'"{job_role}"' for job_role in job_roles])
sites_query = ' OR '.join([f'site:{site}' for site in sites_to_search])
job_opportunities_query = f'"Remote" AND "contractor" AND ({job_roles_query}) {sites_query} after:{end_date}'