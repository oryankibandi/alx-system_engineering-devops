# Outage Report

## Issue Summary

The outage ran from **25th Oct, 2022 10:00pm EAT** to **26th Oct, 2022 1:00pm EAT**.

This outage denied customers access to the website features including authentication, generation of reports and adding new information.

The root cause was expired SSL Certificates.

## Timeline

- **10:30pm** - Issue detected by a customer who could not access his account.
- **11:00pm** - frontend engineering team noticed they could not access the website with the testing tools set in place. The datadog dashboard also showed no activity on the servers.
- **11:30pm** - Nginx server was checked on al the servers hosting the application, HAProxy load balancer was checked and the ssl certificates were checked
- **12:00am** - The incident was escalated to the Devops Engineer in the team.
- **01:00am** - Incident was resolved by renewing SSL certificates with certbot.

## Root cause

The root cause was expired SSL certificates on the load balancer. The SSL certificates issued during deployment were only valid for one month hence needed to be renewed.
SSL certificates were renewed and the application was accessible again. To prevent future incidences, a cron job was set up to automatically renew the certificates at 12:00am everyday in order to not require manual action.

## Corrective Measures

All SSL certificates issued to a new domain must be renewed automatically via setting up a cronjob to renew them at 12:00am every day.

Alerts on low activity on the servers should be set up to inform the relevant personnel.

### steps

    1. Type `crontab -e`
    2. Select an editor
    3. Add a new cron job to renew the SSL certificates automatically
