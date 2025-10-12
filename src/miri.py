from astroquery.mast import Observations

#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Advanced instrument: MIRI/SLIT target_classification: Exoplanets, select planet

#Use MIRI/SLIT data
#Target Exoplanets

obs_table = Observations.query_criteria(
    instrument_name="MIRI/SLIT",
    target_name="GU-PSC-B",
    #target_classification="planets"
)

#1 Entry
product_list = Observations.get_product_list(filtered_obs)

manifest = Observations.download_products(product_list, download_dir='./planetdata/GU-PSC-B')
