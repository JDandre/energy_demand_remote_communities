# Analyzing Energy Demand in Remote Communities
## AI Launch Lab - Summer 2021 Cohort 

#### Contributors
[Audrey Jameson](https://github.com/audreeclaire), Cristina Ortuño Mojica, [Farinaz Kouhrangiha](https://github.com/Farinaaaaaaaz), [Jaret André](https://github.com/JDandre) and [Meilin Lyu](https://github.com/Meilin-Lyu)

## Overview
This was a three-month team project to analyze energy demands in Canadian remote communities. 
The goal of the project was to establish long-term foundations for calculating heating consumption
in these communities by classifying building classifications (Commercial, Residential, Industrial)
and building arch-types (single/mulit-unit housings, garages, factories, etc).


More in-depth report on the project can be found in `/reports/Report.pdf` 
### Video Demo

[High level Project Demo](https://drive.google.com/file/d/12MUdNlHbzhRw8fW4SeyzYx2B37lxG03j/view?usp=sharing)
- Team won the “AI choice award” for the best demo (which had to be directed to all audience levels)

## File Structure
```
├── README.md                               <- The top-level README for guideance using this project.
├── pipeline
│      ├── data
│         ├── processed                     <- The final, canonical data sets for modeling.
│         └── raw                           <- The original, immutable data dump.
│
├── qgis models                            <- QGIS models, scripts and JSON files for dealing with GIS data
├── models                                 <- Trained and serialized models, model predictions, or model summaries
│
├── remote_communities_pipeline.ipynb      <- Jupyter notebooks. 
│
├── reports                                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── images                             <- Generated graphics and figures to be used in reporting
│
├── requirements.txt                       <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`(Coming Soon)
```

## Datasets
1. `.osm` files can be found from [Open Street Map.](https://www.openstreetmap.org/#map=2/71.3/-96.8)
2. Guide building classes (Commerical, Industrial, Residential) for communities in [Nunavut.](http://www.buildingnunavut.com/en/communityprofiles/communityprofiles.asp) 
3. The 3D Raster Layers for communities in Canada can be found [here.](https://open.canada.ca/data/en/fgpv_vpgf/957782bf-847c-4644-a757-e383c0057995)


## QGIS Models
This will be a step-by-step process to how to use the QGIS Graphical Model for this project.

1. [Download QGIS](https://qgis.org/en/site/forusers/download.html)
2. Go to the 3rd reference in the `Datasets` Section and find the community you are looking for. (ie Cambridge Bay)
3. You will see a dark symbol of stacked squares called the `Layers` button, press that and uncheck all foot prints.
   ![Raster Layer Guide Camabridge Bay](reports/images/Raster_layer_guide_cbay.png)
4.  Zoom into Community and show `HRDEM Project Footprints`.
    ![Raster Layer Guide 2 Camabridge Bay](reports/images/Raster_layer_guide_cbay_2.png)

    Canada is split into 50 km x 50 km since these are very large files. Within each section you will see a tile id (ie `29_21`) for each tile it will be broken into four quaters.
    ![Raster Layer Guide 3 Camabridge Bay](reports/images/Raster_layer_guide_cbay_3.png)

    If you toggle the `HRDEM Project Footprints` you should see which corner the community lies in.
5. Press anywhere in the tile and it should bring up more information on the right hand side. 
6. Scroll down until you see `Download link for DSM` and press the link below it.
7. It will bring you to a new page will a bunch of files, scroll down until you see `dsm_2m_polarstereo_<tile_id>...`. When you hover your mouse over them you will see the four quarters number as specified in the last in step 4 (last image). Download the file that the community lies in. (ie `dsm_2m_polarstereo_29_21_2_1.tif`)






