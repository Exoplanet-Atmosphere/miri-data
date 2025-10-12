from astroquery.mast import Observations

#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Advanced instrument: MIRI/SLIT target_classification: Exoplanets, select planet

#Use MIRI/SLIT data
#Downloading _x1d.fits data: 
#Target Exoplanets

#contains one entry
obs_table = Observations.query_criteria(
    instrument_name="MIRI/SLIT",
    target_name="GU-PSC-B",
)

product_list = Observations.get_product_list(obs_table)

manifest = Observations.download_products(product_list,
                                          extension="_x1d.fits",
                                          download_dir='./planetdata/GU-PSC-B'
                                          )

