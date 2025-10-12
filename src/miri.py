from astroquery.mast import MastMissions
from astroquery.mast import Observations
from astropy.coordinates import SkyCoord


#Earth 2.0 TRAPPIST-1e, in TRAPPIST-1 star system
#https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
#Go to MAST Observations by Object Name... and enter TRAPPIST-1e

#Use MIRI/SLIT data
#Target Exoplanets

obs_table = Observations.query_criteria(
    instrument_name="MIRI/SLIT",
    target_name="GU-PSC-B",
    #target_classification="planets"
)

#1 Entry
filtered_obs = obs_table[(obs_table['instrument_name'] == 'MIRI/SLIT') & (obs_table['target_name'] == 'GU-PSC-B')]

product_list = Observations.get_product_list(filtered_obs)

manifest = Observations.download_products(product_list, download_dir='./planetdata/GU-PSC-B')
