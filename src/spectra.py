from astroquery.mast import Observations
from astropy.io import fits
import os

#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Advanced instrument: MIRI/SLIT target_classification: Exoplanets, select planet

#Use MIRI/SLIT data
#Downloading _x1d.fits data: 
#Target Exoplanets

projectroot = os.path.abspath(__file__+"/../..")
planetfolder = projectroot+"/planetdata"
gupscb = planetfolder+"/GU-PSC-B"

if not os.path.exists(gupscb):

    #table contains one entry
    miri_table = Observations.query_criteria(
        instrument_name="MIRI/SLIT",
        target_name="GU-PSC-B",
    )

    miri_products = Observations.get_product_list(miri_table)
    miri_filtered = Observations.filter_products(miri_products, extension="_x1d.fits")
    miri_manifest = Observations.download_products(miri_filtered, download_dir=planetfolder)

    if os.path.exists(planetfolder+"/mastDownload/JWST/"):
        os.rename(planetfolder+"/mastDownload/JWST/", gupscb)
        os.removedirs(planetfolder+"/mastDownload")

    nirspec_table = Observations.query_criteria(
        instrument_name="NIRSPEC/SLIT",
        target_name="GU-PSC-B",
    )

    nirspec_products = Observations.get_product_list(nirspec_table)
    nirspec_filtered = Observations.filter_products(nirspec_products, extension="_x1d.fits")
    nirspec_manifest = Observations.download_products(nirspec_filtered, download_dir=planetfolder)

    if os.path.exists(planetfolder+"/mastDownload/JWST/"):
        os.rename(planetfolder+"/mastDownload/JWST/", gupscb)
        os.removedirs(planetfolder+"/mastDownload")

if os.path.exists(gupscb+"/jw01188-o011_t003_miri_p750l/jw01188-o011_t003_miri_p750l_x1d.fits"):
    with fits.open(gupscb+"/jw01188-o011_t003_miri_p750l/jw01188-o011_t003_miri_p750l_x1d.fits") as hdul:
        hdul.info()
        #print(hdul[0].data)
        #print(hdul[1].data)
        #print(hdul[2].data)
