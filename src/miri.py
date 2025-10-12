from astroquery.mast import Observations

#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Advanced instrument: MIRI/SLIT target_classification: Exoplanets, select planet

#Use MIRI/SLIT data
#Downloading _x1d.fits data: 
#Target Exoplanets

obs_table = Observations.query_criteria(
    instrument_name="MIRI/SLIT",
    target_name="GU-PSC-B",
    #target_classification="planets"
)

#1 Entry
product_list = Observations.get_product_list(obs_table)

filtered_products = Observations.filter_products(product_list, productSubGroupDescription='x1d')

manifest = Observations.download_products(product_list,
                                          extension="_x1d.fits",
                                          download_dir='./planetdata/GU-PSC-B'
                                          )