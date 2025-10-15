from astroquery.mast import Observations
from astropy.io import fits
import os
import shutil
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Advanced instrument: MIRI/SLIT target_classification: Exoplanets, select planet

#Use MIRI/SLIT data
#Downloading _x1d.fits data: 
#Target Exoplanets

projectroot = os.path.abspath(__file__+"/../..")
planetfolder = projectroot+"/planetdata"

def download_exoplanet_x1d_by_instrument(planetname, instrument):
    planetname_folder = planetfolder+"/"+planetname
    obs_table = Observations.query_criteria(
        instrument_name=instrument+"/SLIT",
        target_name=planetname,
        #product_type="spectrum",
    )

    if(len(obs_table) == 0):
        print(planetname+": No Results")
        return False

    obs_products = Observations.get_product_list(obs_table)
    obs_filtered = Observations.filter_products(obs_products, extension="_x1d.fits")
    
    if(len(obs_filtered) == 0):
        print(planetname+": No Matches for "+instrument)
        return True
    
    obs_manifest = Observations.download_products(obs_filtered, download_dir=planetfolder)

    if os.path.exists(planetfolder+"/mastDownload/JWST"):
        
        os.makedirs(planetname_folder+"/"+instrument)

        for file in Path(planetfolder+"/mastDownload/JWST").glob('*'):
            file.rename(planetname_folder+"/"+instrument+"/"+file.name)

        shutil.rmtree(planetfolder+"/mastDownload")
        

    for path, folders, files in os.walk(planetname_folder+"/"+instrument):
        for folder_name in folders:
            for subpath, subfolders, subfiles in os.walk(planetname_folder+"/"+instrument+"/"+folder_name):
                for file_name in subfiles:
                    shutil.move(planetname_folder+"/"+instrument+"/"+folder_name+"/"+file_name, planetname_folder+"/"+instrument+"/"+file_name)
            shutil.rmtree(planetname_folder+"/"+instrument+"/"+folder_name)

    return True

def download_exoplanet_x1d(planetname):
    if not os.path.exists(planetfolder+"/"+planetname):
        results = download_exoplanet_x1d_by_instrument(planetname, "MIRI")
        
        if not results:
            return False
        
        download_exoplanet_x1d_by_instrument(planetname, "NIRSPEC")
    
    return True

def visualize_spectrum(fits_file):
        #open fits file
    with fits.open(fits_file) as hdul:
        hdul.info()
        data = hdul[1].data

        wavelength = data['Wavelength'][0]  # microns
        flux = data['Flux'][0]  # Jy or similar units

        # plotting
        plt.figure(figsize=(10,5))
        plt.plot(wavelength, flux, color='blue')
        plt.title(f"Spectrum from {os.path.basename(fits_file)}")
        plt.xlabel("Wavelength (microns)")
        plt.ylabel("Flux")
        plt.grid(True)
        plt.show()

        # Histogram of flux values
        plt.figure(figsize=(6,4))
        plt.hist(flux, bins=50, color='purple', alpha=0.7)
        plt.title("Flux Distribution")
        plt.xlabel("Flux")
        plt.ylabel("Count")
        plt.show()

#MAIN

if os.path.exists(planetfolder):
    shutil.rmtree(planetfolder)

download_exoplanet_x1d("GU-PSC-B")

download_exoplanet_x1d("CHA1110-7633")

download_exoplanet_x1d("CHA1107-7626")

download_exoplanet_x1d("CHA1110-7721")

download_exoplanet_x1d("UHWJ247.95-24.78")

download_exoplanet_x1d("51-ERI-SPECKLES")

download_exoplanet_x1d("WASP-39")

'''
if os.path.exists(gupscb+"/jw01188-o011_t003_miri_p750l/jw01188-o011_t003_miri_p750l_x1d.fits"):
    with fits.open(gupscb+"/jw01188-o011_t003_miri_p750l/jw01188-o011_t003_miri_p750l_x1d.fits") as hdul:
        hdul.info()
        #print(hdul[0].data)
        #print(hdul[1].data)
        #print(hdul[2].data)
'''
for path, subdirs, files in os.walk(planetfolder):
    for name in files:
        if name.endswith("_x1d.fits"):
            fits_path = os.path.join(path, name)
            print(f"Visualizing {fits_path}")
            visualize_spectrum(fits_path)
            break
