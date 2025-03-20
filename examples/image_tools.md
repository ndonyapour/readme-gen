# Image Tools Repository

Welcome to the Image Tools repository, a comprehensive collection of tools designed for image processing and analysis. This repository includes a variety of plugins for filtering, segmentation, transformation, and visualization of images. Each tool is tailored to perform specific tasks, making it easier to handle complex image data efficiently.

## Tools Overview

### Filtering Tools
- **ImageJ Filter Partial Derivative Tool**: Applies partial derivative filter to input collection using ImageJ.
- **ImageJ Filter Gauss Tool**: Applies Gaussian Convolutional filter to input collection using ImageJ.
- **ImageJ Filter Tubeness Tool**: Filters a collection to score tube-like structures using ImageJ.
- **ImageJ Filter Add Poisson Noise Tool**: Adds Poisson distribution noise to input images using ImageJ.
- **ImageJ Filter Derivative Gauss Tool**: Applies nth derivative of Gaussian to input collection using ImageJ.
- **ImageJ Filter Sobel Tool**: Applies Sobel operator to input collection using ImageJ.
- **ImageJ Filter Frangi Vesselness Tool**: Applies Frangi Vesselness filter to highlight vessel-like structures using ImageJ.
- **ImageJ Filter DoG Tool**: Applies Difference of Gaussians algorithm to input collection using ImageJ.
- **ImageJ Filter Correlate Tool**: Applies correlation operation with user-specified kernel using ImageJ.
- **ImageJ Filter Convolve Tool**: Performs convolution operation with user-specified kernel using ImageJ.

### Segmentation Tools
- **ImageJ Threshold Rosin Tool**: Implements Rosin's thresholding method for unimodal distributions.
- **ImageJ Threshold Minimum Tool**: Applies minimum thresholding method for bimodal histograms.
- **ImageJ Threshold Apply Tool**: Applies constant manual threshold value to images.
- **ImageJ Threshold MinError Tool**: Implements Minimum Error thresholding method.
- **ImageJ Threshold Huang Tool**: Implements Huang's threshold method to minimize fuzziness measure.
- **ImageJ Threshold Otsu Tool**: Implements Otsu's threshold clustering algorithm.
- **ImageJ Threshold Li Tool**: Implements Li's Minimum Cross Entropy thresholding method.
- **ImageJ Threshold Percentile Tool**: Applies percentile thresholding method assuming foreground pixel fraction.
- **ImageJ Threshold Isodata Tool**: Implements isodata thresholding method using iterative selection.
- **ImageJ Threshold Triangle Tool**: Implements triangle threshold method using geometric approach.
- **ImageJ Threshold Yen Tool**: Applies Yen's threshold method for automatic multilevel thresholding.
- **ImageJ Threshold Moments Tool**: Implements Tsai's moment-preserving thresholding method.
- **ImageJ Threshold Intermodes Tool**: Applies intermodes thresholding method for bimodal histograms.
- **ImageJ Threshold Mean Tool**: Uses mean of grey levels as threshold value.
- **ImageJ Threshold RenyiEntropy Tool**: Uses Renyi entropy method for thresholding.
- **ImageJ Threshold Shanbhag Tool**: Implements Shanbhag's extension of Renyi Entropy method.
- **ImageJ Threshold IJ1 Tool**: Implements default thresholding method from ImageJ 1.x.
- **ImageJ Threshold MaxEntropy Tool**: Implements Kapur-Sahoo-Wong Maximum Entropy thresholding method.
- **ImageJ Threshold MaxLikelihood Tool**: Implements maximum likelihood threshold method using EM algorithm.

### Transformation Tools
- **Image Assembler Tool**: Assembles images into a stitched image using stitching vector.
- **Polus Recycle Vector Plugin**: Applies existing stitching vector to image collection using WIPP.
- **Polus Image Registration Plugin**: Registers image collection using projective transformation.
- **Binary Operations Tool**: Performs morphological image processing on binary images.
- **Polus Stack Z-Slice Plugin**: Stacks z-slices into a single volume using Bioformats tiled tiff format.
- **Polus Autocropping Plugin**: Automatically crops images to remove outer edges using entropy tracking.
- **LUMoS Bleedthrough Correction Tool**: Uses LUMoS algorithm to separate fluorophore signals in images.
- **Polus Intensity Projection Plugin**: Calculates volumetric intensity projection of 3D images.
- **Image Calculator Tool**: Performs pixel-wise operations between two image collections.
- **Montage Tool**: Generates stitching vector to montage images together.
- **ROI Relabel Tool**: Relabels and consolidates Regions of Interest in images.

### Visualization Tools
- **Tabular to Microjson Tool**: Generates JSON from tabular data for visualization.
- **Microjson to OME Tool**: Reconstructs binary image from polygon coordinates in microjson format.
- **Polus Feature Heatmap Pyramid Plugin**: Generates heatmap pyramids from image features.
- **OME to Microjson Tool**: Generates microjson of polygon coordinates from binary segmentations.
- **Polus Image Cluster Annotation Plugin**: Converts images to cluster annotations with border cluster IDs.
- **Polus Precompute Volume Plugin**: Converts images to Neuroglancer precomputed format.
- **Precompute Slide Tool**: Generates image pyramids in multiple viewing formats.
- **Polus Color Pyramid Builder Plugin**: Builds DeepZoom color image pyramids for WDZT.

### Regression Tools
- **Basic Flatfield Estimation Tool**: Estimates flatfield correction using BaSiC algorithm.
- **Theia Bleedthrough Estimation Tool**: Estimates bleed-through in images using Theia algorithm.

### Clustering Tools
- **HDBSCAN Clustering Tool**: Clusters data using HDBSCAN clustering library.

### Format Conversion Tools
- **Polus TiledTiff Converter Plugin**: Converts images to OME tiled tiff format using Bioformats.
- **Polus Imaris Parser Plugin**: Extracts tracking statistics from Imaris .ims files.
- **Vector to Label Tool**: Converts vector fields to labeled images.
- **Polus Multichannel Tiff Plugin**: Assigns images to multi-channel ome tiff using filename pattern.
- **Image Dimension Stacking Tool**: Stacks images into multi-dimensional images using filepattern.
- **Label to Vector Tool**: Converts labeled images to vector fields.
- **File Renaming Tool**: Renames files in image collection using supplied patterns.
- **Polus CZI Extract Plugin**: Imports fields of view from CZI file as tiled tiffs.
- **OME Converter Tool**: Converts BioFormats supported data types to OME Zarr or TIF format.

### Utility Tools
- **Rxiv Download Tool**: Downloads data from open access archives like arxiv.
- **Polus Python Template**: Template for creating Python-based WIPP plugins.
- **IDR Download Tool**: Downloads data from IDR using web API.
- **Polus Subset Data Plugin**: Selects subset of data from image collection using filename pattern.
- **Polus ImageJ Util**: Generates WIPP plugins from ImageJ ops.
- **Polus Stitching Vector Merger Plugin**: Merges stitching vector collections together.
- **Filepattern Generator Plugin**: Creates filepatterns to subset image data.
- **Polus Generic to Image Collection Plugin**: Copies contents of Generic Data collection to Image Collection.
- **MIDRC Download Tool**: Downloads images and annotations from MIDRC Commons.
- **Polus Notebook Plugin**: Executes Jupyter notebooks as WIPP plugins.
- **Polus ImageJ Macro Plugin**: Runs ImageJ macros on images.

## Installation and Usage

Each tool in this repository can be installed and used individually. Most tools require Docker for building and running. Installation instructions and usage examples are provided in the README files of each tool.

For more information on how to use these tools, visit the [official WIPP page](https://isg.nist.gov/deepzoomweb/software/wipp).

## Contribution

We welcome contributions to the Image Tools repository. If you have a new tool or improvement to an existing tool, please submit a pull request. Ensure that your code follows the repository guidelines and includes proper documentation.

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.

---

This README provides a high-level overview of the Image Tools repository and its various tools. Each tool has its own detailed documentation for specific installation and usage instructions.