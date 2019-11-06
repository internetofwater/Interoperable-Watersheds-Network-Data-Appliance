# Internet of Water Semi-Automatic Sensor Observation Service

The Internet of Water Semi-Automatic Sensor Observation Service is a collection of open source software components to manage the ingestion of manually-collected environmental data from field sites where there may not be internet access into an OGC Sensor Observation Service (SOS) specification-compliant server. 

## 1. KoBoToolbox

The service owner interacts with a browser-based, online/offline data collection form (Enketo) that supplies attributes on one or more "sensors" (field observation points, e.g. groundwater wells, stream gages, benthic observation posts, etc.). This form caches results in the browser until the mobile device has internet access, at which point it automatically uploads the data to a PostgreSQL database on a KoBoToolbox server.


The system periodically polls this server, downloading the data using the KoBo API and parsing it into a separate .csv file for each "sensor". 

## 2. Sensor Observation Service (EPA Interoperable Watersheds Network Data Appliance)

See github




