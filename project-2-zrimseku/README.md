# Project 2: Initial exploration and data visualization

This repository contains the code and report of data analysis of Celtra company's platform usage.

## Instructions

To reproduce the work described in the [report](https://github.com/DS-ULFRI/project-2-zrimseku/blob/main/report/report.pdf) 
you need to create the environment exported in `environment.yml` file and run the notebook `data_exploration.ipynb`. 

## Data

Celtra company provided an anonymized and sampled dataset on their platform usage data.

The two datasets are contained in the file [*Celtra example datasets (shared externally).zip*](https://drive.google.com/file/d/18rVfAmCZ5TmGLXSqlSzEvIGDFrTa44VC/view?usp=sharing). Below we overview the attributes provided in the datasets.


### Celtra platform usage data.csv

Platform user activity:

| Attribute | Description |
| --- | ----------- |
| `Account` | Unique ID for each user (company) |
| `User`    | Unique ID for each user on the platform (company employee) |
| `Session` | Unique ID of (web) session using the platform |
| `ActivityLocation` | Which part of the platform is used by the `User` |
| `Activity` | Coarse grouping of ActivityLocation |
| `Timestamp` |  |


### Celtra sessions data.csv

Advertisement traffic on Celtra servers, data on ads shown on internet users' devices:

| Attribute | Description |
| --- | ----------- |
| `Date` |  |
| `AccountID` |  Unique ID for each user (company) |
| `CampaignID` | Unique ID for campaign produced by a `User` (company employee) |
| `CreativeID` | Unique ID for each creative (group of ads - creative) |
| `Platform` | Platform where ads shown |
| `SDK` |  Software environment on device where ads shown |
| `Requested sessions` |  Number of requests to the server from the (internet) users' devices |
| `Creative load attempts` |  Number of ads that were attempted to be loaded on the devices |
| `Loaded sessions` | Number of ads that were successfully loaded on the devices |
| `Rendered sessions` | Number of ads that were successfully shown on the devices |
| `Sessions with interaction` | Number of ads that the internet users interacted with |
| `Viewable time` | Number of seconds the ads were visible to users |

Detailed description of attributes can be [found here](https://support.celtra.com/trafficking-and-analytics/analytics-glossary).
