import requests, json, pandas as pd


#### Query

query_name = "test"

url = "https://api.fda.gov/drug/event.json"

querystring = {"search":"patient.reaction.reactionmeddrapt:\"fatigue\"","limit":"3"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)
data = json.loads(response.text)
data = data['results']
data[0]


#### Count number of reports

number_of_reports = len(data)


#### Unnest JSON file into dictionaries

## Dictionaries
safetyreportversion = {}
safetyreportid = {}
primarysourcecountry = {}
occurcountry = {}
transmissiondateformat = {}
transmissiondate = {}
reporttype = {}
serious = {}
receivedateformat = {}
receivedate = {}
receiptdateformat = {}
receiptdate = {}
fulfillexpeditecriteria = {}
companynumb = {}
duplicate = {}


## Unnest loops for each column

x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['safetyreportversion']
        safetyreportversion[z] = w
        z += 1
        y += 1
    x += 1
safetyreportversion


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['safetyreportid']
        safetyreportid[z] = w
        z += 1
        y += 1
    x += 1
safetyreportid


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['primarysourcecountry']
        primarysourcecountry[z] = w
        z += 1
        y += 1
    x += 1
primarysourcecountry


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['occurcountry']
        occurcountry[z] = w
        z += 1
        y += 1
    x += 1
occurcountry


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['transmissiondateformat']
        transmissiondateformat[z] = w
        z += 1
        y += 1
    x += 1
transmissiondateformat


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['transmissiondate']
        transmissiondate[z] = w
        z += 1
        y += 1
    x += 1
transmissiondate


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['reporttype']
        reporttype[z] = w
        z += 1
        y += 1
    x += 1
reporttype


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['serious']
        serious[z] = w
        z += 1
        y += 1
    x += 1
serious


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['receivedateformat']
        receivedateformat[z] = w
        z += 1
        y += 1
    x += 1
receivedateformat


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['receivedate']
        receivedate[z] = w
        z += 1
        y += 1
    x += 1
receivedate


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['receiptdateformat']
        receiptdateformat[z] = w
        z += 1
        y += 1
    x += 1
receiptdateformat


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['receiptdate']
        receiptdate[z] = w
        z += 1
        y += 1
    x += 1
receiptdate


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['fulfillexpeditecriteria']
        fulfillexpeditecriteria[z] = w
        z += 1
        y += 1
    x += 1
fulfillexpeditecriteria


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['companynumb']
        companynumb[z] = w
        z += 1
        y += 1
    x += 1
companynumb


x = 0
z = 1
while x < number_of_reports:
    number_of_reactions = len(data[x]['patient']['reaction'])
    y = 0
    while y <number_of_reactions:
        w = data[x]['duplicate']
        duplicate[z] = w
        z += 1
        y += 1
    x += 1
duplicate


#### Create a SQL tabular object

list_a=[]
a={}
export={}

for n in safetyreportversion:
    a = {'safetyreportversion':safetyreportversion[n],'safetyreportid':safetyreportid[n],'primarysourcecountry':primarysourcecountry[n],'occurcountry':occurcountry[n],'transmissiondateformat':transmissiondateformat[n],'transmissiondate':transmissiondate[n],'reporttype':reporttype[n],'serious':serious[n],'receivedateformat':receivedateformat[n],'receivedate':receivedate[n],'receiptdateformat':receiptdateformat[n],'receiptdate':receiptdate[n],'fulfillexpeditecriteria':fulfillexpeditecriteria[n],'companynumb':companynumb[n],'duplicate':duplicate[n]}
    list_a.append(a)


### Create A DataFrame From the JSON Data

df = pd.DataFrame(list_a)
df

