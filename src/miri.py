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
    obs_table = Observations.query_criteria(
        instrument_name="MIRI/SLIT",
        target_name="GU-PSC-B",
    )

    product_list = Observations.get_product_list(obs_table)

    filtered_products = Observations.filter_products(product_list, extension="_x1d.fits")

    manifest = Observations.download_products(filtered_products, download_dir=planetfolder)

    os.rename(planetfolder+"/mastDownload/JWST/", gupscb)

    os.removedirs(planetfolder+"/mastDownload")

if os.path.exists(gupscb+"/jw01188-o011_t003_miri_p750l/jw01188-o011_t003_miri_p750l_x1d.fits"):
    with fits.open(gupscb+"/jw01188-o011_t003_miri_p750l/jw01188-o011_t003_miri_p750l_x1d.fits") as hdul:
        hdul.info()
        print(hdul[0].data)
        print(hdul[1].data)
        print(hdul[2].data)
