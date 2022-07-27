# AdverseDrugEventPipeline

> Drug Side Effect Checker - The Pharmacovigilance Dashboard Prototype
> 
> Developed for MSc thesis "Improving Understandability of Drug Safety Data. Design Principles for Drug Safety Dashboards" available at [link_to_thesis]




## Table of contents
* [General info](#general-info)
* [Illustrations](#illustrations)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)

## General info

<h3> Background info </h3>
Every year, FDA receives over one million adverse event and medication error reports associated with the use of drugs. FDA uses these reports to monitor safety of the drugs. Although these reports are a valuable source of information, this system has limitations, including submission of incomplete, inaccurate, untimely and unverified information. Importantly, the information in the FDA database does not confirm a causal relationship between the drug and the side effect. 
<br> </br>
To address that issue, our prototype uses data mining techniques that rely on statistical analysis to evaluate whether there may be a causal relationship between a side effect and a drug (i.e., whether an event is potentially related or unrelated to a drug). However, the interpretation of data mining analysis should be done with caution, as it doesn’t represent certainty that a drug caused a side effect. So, just because the side effect was evaluated as unrelated, does not mean you will certainly not experience it. 
<br> </br>

More info on data source: [FAERS Database](https://www.fda.gov/drugs/surveillance/questions-and-answers-fdas-adverse-event-reporting-system-faers)

<h3> How is the data analysed? </h3>
Disproportionality Analysis (DPA) with calculation of Proportionality Reporting Ratio (PRR) are be used as data mining techniques to process the data. Retrieved DPA indicators are used to identify safety signals. They can be interpreted as “unexpectedly high reporting associations” and can “signal that there may be a causal association between the particular adverse event and the product”. Source: 

[FDA White Paper](https://www.fda.gov/science-research/data-mining/data-mining-fda-white-paper)

In essence, in DPA an "expected" count is compared with a "observed" count for a product-event combination. PRR can be defined as “the degree of disproportionate reporting of an adverse event for a product of interest compared to this same event for all other products in the database” (Duggirala et al. 2016; Duggirala et al. 2018). The main assumptions here are 1) that the whole database serves as an “expected background” and 2) that there is no association between events reported and their products. If there is a disproportionately high number of events reported per drug, assumption no. 2 is questionable and the event may be (statistically) associated with a drug. Contingency table is a means of visualisation of this concept (below).
<br> </br>
Table 1. PRR Contingency Table. Source: 

[FDA White Paper](https://www.fda.gov/science-research/data-mining/data-mining-fda-white-paper)

|                    | Event Y | All other events | Sums  |
|--------------------|---------|------------------|-------|
| Product X          | a       | b                | a + b |
| All other products | c       | d                | c + d |
| Sums               | a + c   | b + d            | Total |

<br> </br>
In this work, VigilApp is used to calculate DPA indicators, see more here: [VigilApp](https://openvigil.pharmacology.uni-kiel.de/openvigilfda.php#)

For more information (eg., exact formulas used for calculations), refer to [VigilApp Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0157753) and [Evaluation Criteria](https://onlinelibrary.wiley.com/doi/10.1002/pds.677)

<h3> What can I find in the prototype? </h3>

This is an academic prototype of an interactive dashboard that visualises information on drugs and their possible side effects. The dashboard has two sections. Up the page you will find general analysis for a selected drug and its most common side effects. Down the page you can explore in-depth analysis for a selected drug and one selected side effect.
<br> </br>
Events are pre-evaluated as either <b>potentially</b> Related or Unrelated to a drug by DPA algorithm. 
<br> </br>
Link to the final prototype developed in this project using Tableau: [Prototype](https://public.tableau.com/app/profile/cl.udio.pires4914/viz/DrugSideEffectChecker/DrugSideEffectChecker)

<h3> What does this code do? </h3>
See "Setup" section.

## Illustrations
Below you can find example visualisations of drug safety data in the dashboard prototype.

<h4> General Overview of Drug Safety Profile </h4>

![Dashboard1](img/dashboard1.png)

<h4> Selected in-depth analysis for a selected drug and one selected side effect </h4>

![Dashboard2](img/dashboard2.png)

## Technologies
* Python 3.8.12
* Pandas 1.3.4
* Selenium 4.0
* BeautifulSoup4 4.7.1

## Setup
<h3> General info </h3>
There are two scripts in this project: API_Drug_Data_Extract.ipynb & DPA_Scraper.ipynb. Run DPA_Scraper.ipynb first.

<h3> DPA Scraper </h3>

DPA_Scraper.ipynb retrieves DPA analysis (drug safety signal as either related or unrelated) from [VigilApp](https://openvigil.pharmacology.uni-kiel.de/openvigilfda.php#) for drugs + side effects.
<br> </br>
All necessary dirs will be created by the script. File 'events.xlsx' [in here](required_excel_files/events.xlsx) must be placed in script directory. It contains drugs + their most common side effects (obtained from VigilApp by querying for drug name in basic data extraction or counting). File 'references.xlsx' must be placed in script directory [in here](required_excel_files/references.xlsx). 
<br> </br>

Script outputs:
- .xlsx file with DPA analysis per drug+side effect in DA directory
- file 'events_signals.xlsx' in script directory. It contains drug safety signal information (related/unrelated). <b>This file is required for API_Drug_Data_Extract.ipynb run </b>

<h3> API Drug Data Extractor </h3>
API_Drug_Data_Extract.ipynb queries API to get all demographic data (per drug + secondary effect) visualised in the dashboard. 
<br> </br>
All necessary dirs will be created by the script. File 'events_signals.xlsx' [in here](required_excel_files/events_signals.xlsx) must be placed in script directory. <b> This file is created with DPA_Scraper.ipynb run. </b> Exemplary 'events_signals.xlsx' file can be found in dir /required_excel_files
<br> </br>

Other mandatory files (in script dir):
- country_codes.xlsx
- demo.xlsx
- df_empty_template.xlsx
- references.xlsx
- reporter_type.xlsx
- serious.xlsx
- signal_df.xlsx
- years.xlsx
<br> </br>
These files can be found in dir /required_excel_files. They are either providing interpretation for FDA database codes or serve as DataFrame templates.
<br> </br>

Script outputs:
- demographic data on drugs + side effects (as in events_signals.xlsx) in demo directory

## Status
Project is _in progress_. TODO: 
- [x] Rewrite Readme
- [x] Add .xlsx files

## Contact
Created by Malwina Kotowicz (m_kotowicz@hotmail.com) and Cláudio Pires (claudiofmpires@gmail.com ) - feel free to contact us!
