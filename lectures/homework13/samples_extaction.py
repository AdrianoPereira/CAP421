import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from PIL import Image as pimage
import rasterio as rio
from sklearn.preprocessing import MinMaxScaler
import geopandas as gpd
from shapely.geometry import Point
import os


PATH = "/home/adriano/CAP421/lectures/homework13"
TIF_IMG_PATH = os.path.join(PATH, f"data/PREPROCESSED/raw/PAR_AMAZONIA1_WFI_CROPPED.tif")
PNG_IMG_PATH = TIF_IMG_PATH.replace('.tif', '.png')
RESULT_PATH = os.path.join(PATH, f"results")

WIDTH, HEIGHT = 128, 128
N_SAMPLES = 2000
CROP_IMG_PATHS = os.path.join(PATH, f"data/PREPROCESSED/CROPPED/{WIDTH}X{HEIGHT}")
if not os.path.exists(CROP_IMG_PATHS):
    os.makedirs(CROP_IMG_PATHS)


# In[3]:


with rio.open(TIF_IMG_PATH) as handle:
    nrows, ncols = handle.shape
    res = handle.res
    left, bottom, right, top = handle.bounds
mlon = np.linspace(left, right, ncols)
mlat = np.linspace(bottom, top, nrows)
mlons, mlats = np.meshgrid(mlon, mlat)


np.random.seed(42)
with pimage.open(PNG_IMG_PATH) as handle:
    img_arr = np.asarray(handle)
    fig, ax = plt.subplots(1, 2, figsize=(20, 15), sharex=True, sharey=True)
    ax[0].set_title("AREA WITHOUT A LOT OF CLOUD COVERAGE", fontdict={'size': 18 ,'weight': 'bold'})
    ax[0].imshow(img_arr)
    ax[0].set_yticks(range(nrows), [f'{i:.3f}' for i in mlat[::-1]])
    ax[1].set_title("SAMPLE EXTRACTION POINTS", fontdict={'size': 18 ,'weight': 'bold'})
    ax[1].imshow(img_arr)
    
    idxs = np.random.choice(range(0, (nrows*ncols)), N_SAMPLES, replace=False)
    scols = idxs%ncols
    srows = idxs//ncols
    ax[1].scatter(scols, srows, color='red', lw=0.75, ec='k', s=30)
    plt.savefig(
        f"{RESULT_PATH}/area_cropped_for_extraction.png", transparent=False, bbox_inches='tight', 
        pad_inches=0.1
    )
    plt.show()


mw, mh = WIDTH//2, HEIGHT//2
for i, (scol, srow) in enumerate(zip(scols, srows)):
    filename = f"PAR-AMAZONIA1-WFI-{str(i).zfill(4)}-{WIDTH}X{HEIGHT}.png"
    filename = os.path.join(CROP_IMG_PATHS, filename)
    
    print(f"Working in {filename}...")
    srow = srow if srow-mh >= mh else mh
    srow = srow if srow+mh < nrows-mh else nrows-mh
    srow = [srow-mh, srow+mh]
    
    scol = scol if scol-mw >= mw else mw
    scol = scol if scol+mw < ncols-mw else ncols-mw
    scol = [scol-mw, scol+mw]
    
    img = img_arr[srow[0]:srow[1], scol[0]:scol[1], :].copy()
    pimage.fromarray(img).save(filename, 'png', quality=100)


img_filepaths = sorted([os.path.join(CROP_IMG_PATHS, filename) for filename in os.listdir(CROP_IMG_PATHS)])

fig, ax = plt.subplots(3, 4, figsize=(20, 10), sharex=True, sharey=True)

for i in range(12):
    row = i//4
    col = i%4
    with pimage.open(img_filepaths[i]) as handle:
        ax[row][col].set_title(img_filepaths[i].split(os.sep)[-1][:-4], fontdict={'size': 9, 'weight': 'bold'})
        ax[row][col].imshow(handle)
        
fig.subplots_adjust(wspace=0.01)
plt.savefig(
    f"{RESULT_PATH}/grid_samples.png", transparent=False, bbox_inches='tight', 
    pad_inches=0.1
)
plt.show()
