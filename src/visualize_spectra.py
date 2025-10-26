import matplotlib.pyplot as plt
from astropy.io import fits
import os

def visualize_spectrum(fits_file, type=["None"]):
        #open fits file
    with fits.open(fits_file) as hdul:
        hdul.info()
        data = hdul[1].data

        wavelength = data['WAVELENGTH'][1:len(data)-1]  # microns
        flux = data['Flux'][1:len(data['FLUX'])-1]  # Jy or similar units

        # Flux vs Wavelength
        if "None" in type or "flux-len" in type:
            plt.figure(figsize=(10,5))
            plt.plot(wavelength, flux, color='blue')
            plt.title(f"Spectrum from {os.path.basename(fits_file)}")
            plt.xlabel("Wavelength (microns)")
            plt.ylabel("Flux")
            plt.grid(True)
            plt.show()

        # Histogram of flux values
        if "flux-hist" in type:
            plt.figure(figsize=(6,4))
            plt.hist(flux, bins=50, color='purple', alpha=0.7)
            plt.title("Flux Distribution")
            plt.xlabel("Flux")
            plt.ylabel("Count")
            plt.show()

if __name__ == "__main__":
    import get_spectra_data as gsd

    print("Running Visualization Script...")

    gsd.download_exoplanet_x1d("GU-PSC-B")
    test_file = gsd.planetfolder+"/GU-PSC-B/MIRI/jw01188-o011_t003_miri_p750l_x1d.fits"
    
    visualize_spectrum(test_file, ["flux-hist", "flux-len"])