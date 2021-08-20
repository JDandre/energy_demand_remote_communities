# Analyzing Energy Demand in Remote Communities
## AI Launch Lab - Summer 2021 Cohort 

#### Contributors
[Audrey Jameson](https://github.com/audreeclaire), Cristina Ortuño Mojica, [Farinaz Kouhrangiha](https://github.com/Farinaaaaaaaz), [Jaret André](https://github.com/JDandre) and [Meilin Lyu](https://github.com/Meilin-Lyu)

## Overview
This was a three-month team project to analyze energy demands in Canadian remote communities. 
The goal of the project was to establish long-term foundations for calculating heating consumption
in these communities by classifying building classifications (Commercial, Residential, Industrial)
and building arch-types (single/mulit-unit housings, garages, factories, etc).


More in-depth report on the project can be found in `/reports` 
### Video Demo

[High level Project Demo](https://drive.google.com/file/d/12MUdNlHbzhRw8fW4SeyzYx2B37lxG03j/view?usp=sharing)
- Team won the “AI choice award” for the best demo (which had to be directed to all audience levels)

## Datasets
1. osm files can be found from [Open Street Map.](https://www.openstreetmap.org/#map=2/71.3/-96.8)
2. Guide building classes (Commerical, Industrial, Residential) for communities in [Nunavut.](http://www.buildingnunavut.com/en/communityprofiles/communityprofiles.asp) 
3. 3D Raster Layers for communities in Canada can be found [here.](https://open.canada.ca/data/en/fgpv_vpgf/957782bf-847c-4644-a757-e383c0057995)
## File Structure
```
├── README.md          <- The top-level README for developers using this project.
├── pipeline
│      ├── data
│         ├── processed      <- The final, canonical data sets for modeling.
│         └── raw            <- The original, immutable data dump.
│
├── qgis models             <- QGIS models and scripts for dealing with GIS data
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── remote_communities_pipeline.ipynb      <- Jupyter notebooks. 
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── images         <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`(Coming Soon)
```


