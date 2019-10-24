1. The US National Oceanic & Atmospheric Administration (NOAA) collects and stores historic atmospheric measurements from across the world at https://www.esrl.noaa.gov/gmd/dv/data/
(and on their ftp server at ftp://ftp.cmdl.noaa.gov/). Using either site, try to find the files
that hold measurements of atmospheric CO2, specifically:
    * the discrete measurements from tasks collected by the German Weather Service at Mount
Hohenpeissenberg in Southern Bavaria, Germany (the world’s oldest mountain-top weather
station)
    * the discrete measurements from ƽasks collected by the German Weather Service at Mount
Ochsenkopf in Germany in Northern Bavaria, Germany
    * daily averages collected by NOAA on the Mauna Loa volcano on the Island of Haiwaii since
1969

2. take a look at each Ƽle. If you could not Ƽnd them in the Ƽrst part of this exercise, they are available
on Ilias. But Ƽnding them online is a key part of this exercise!

3. write a python script to load each ASCII text Ƽle into a pandas table

4. make a plot of the raw data (CO2 contentration vs. time) for Hohenpeissenberg. Do you notice any
problems with the data? Check the Ƽnal reading on 2018/12/27/11:55:00

5. How would you correct this Ƽnal reading? Check the data from Ochsenkopf. Can you think of a way
to use it to Ƽx the reading at Hohenpeissenberg?

6. You can also download raw readings from the same station at https://www.icos-cp.eu/data
(stored by the European Carbon Portal). Do the data stored there match the record in the NOAA
database?

7. make a plot of the data from Mauna Loa (since 1969).
