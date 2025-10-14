from astroquery.mast import Observations
from astropy.io import fits
import os
import shutil
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Advanced instrument: MIRI/SLIT target_classification: Exoplanets, select planet

#Use MIRI/SLIT data
#Downloading _x1d.fits data: 
#Target Exoplanets

#assign variables for project directories
projectroot = os.path.abspath(__file__+"/../..") #root of the project
planetfolder = projectroot+"/planetdata" #folder containing data for exoplanets

#donwload 1d extracted spectra data from the MAST database by exoplanet name, and instrument (generally MIRI or NIRSpec)
def download_exoplanet_x1d_by_instrument(planetname, instrument):
    planetname_folder = planetfolder+"/"+planetname #directory where specific planet data will be stored
    
    #The search criteria to retrieve the data from MAST
    obs_table = Observations.query_criteria(
        instrument_name=instrument+"/SLIT",
        target_name=planetname,
    )

    #if the search returns no results, return False, letting other functions know to stop searching
    #note: this is different from the planet having no results for a specific type of instrument
    if(len(obs_table) == 0):
        print(planetname+": No Results")
        return False

    #get a list of downloadable products from the query results
    obs_products = Observations.get_product_list(obs_table)

    #filter through the downloads for _1xd.fits files <- Extracted 1D Spectra data
    obs_filtered = Observations.filter_products(obs_products, extension="_x1d.fits")
    
    #if the filtered results have no matches, return true, letting other functions know that there still might be data for other instruments
    if(len(obs_filtered) == 0):
        print(planetname+": No Matches for "+instrument)
        return True
    
    #download the _1xd.fits files into the exoplanet's data folder
    obs_manifest = Observations.download_products(obs_filtered, download_dir=planetfolder)

    #if the download succeeded this mastDownload/JWST folder will have been created
    if os.path.exists(planetfolder+"/mastDownload/JWST"):
        
        #create a folder to organize the data found by the type of instrument used to collect it (MIRI or NIRSpec)
        os.makedirs(planetname_folder+"/"+instrument)

        #move the data from a download folder to the appropriate exoplanet folder
        for file in Path(planetfolder+"/mastDownload/JWST").glob('*'):
            file.rename(planetname_folder+"/"+instrument+"/"+file.name)

        #remove emptied download folder
        shutil.rmtree(planetfolder+"/mastDownload")
        
    #Organizing the data, removing the redundant directories downloaded /a/ for a.fits or /b/ for b.fits etc.
    for path, folders, files in os.walk(planetname_folder+"/"+instrument):
        for folder_name in folders:
            for subpath, subfolders, subfiles in os.walk(planetname_folder+"/"+instrument+"/"+folder_name):
                for file_name in subfiles:
                    shutil.move(planetname_folder+"/"+instrument+"/"+folder_name+"/"+file_name, planetname_folder+"/"+instrument+"/"+file_name)
            shutil.rmtree(planetname_folder+"/"+instrument+"/"+folder_name)

    return True

#Download all _x1d files for a planet, from MIRI and NIRSpec
def download_exoplanet_x1d(planetname):
    if not os.path.exists(planetfolder+"/"+planetname):
        results = download_exoplanet_x1d_by_instrument(planetname, "MIRI")
        
        #if the planet name is invalid for a query, no need to search again
        if not results:
            return False
        
        download_exoplanet_x1d_by_instrument(planetname, "NIRSPEC")
    
    return True

#execute if the script is called directly, but not if it is imported
if __name__ == "__main__":

    #if os.path.exists(planetfolder):
    #    shutil.rmtree(planetfolder)

    download_exoplanet_x1d("GU-PSC-B")

    with fits.open(planetfolder+"/GU-PSC-B/MIRI/jw01188-o011_t003_miri_p750l_x1d.fits") as hdul:
        
        data = hdul[1].data

        #includes Nan at end and start, hence the slice
        wavelength = data['WAVELENGTH'][1:387]
        flux = data['FLUX'][1:387]

        #quick plot of data
        plt.plot(wavelength, flux)
        plt.xlabel("Wavelength μm")
        plt.ylabel("Flux erg/s/cm²/Å")
        plt.title("Normalized 1D Extracted Spectra Data")
        plt.show()
        
        '''
        #normalize data with average of 0 and standard dev of 1
        wavemean = np.mean(wavelength)
        wavedev = np.std(wavelength)
        for x in range(len(wavelength)):
            wavelength[x] = (wavelength[x]-wavemean)/wavedev
        
        fluxmean = np.mean(flux)
        fluxdev = np.std(flux)
        for x in range(len(flux)):
            flux[x] = (flux[x]-fluxmean)/fluxdev
        '''

        '''
        #normalize data between 1 and 0
        wavemin = min(wavelength)
        waverange = max(wavelength)-wavemin
        for x in range(len(wavelength)):
            wavelength[x] = (wavelength[x]-wavemin)/waverange
        
        fluxmin = min(flux)
        fluxrange = max(flux)-fluxmin
        for x in range(len(flux)):
            flux[x] = (flux[x]-fluxmin)/fluxrange
        '''

        '''
        molecule = keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
        ])
        '''
