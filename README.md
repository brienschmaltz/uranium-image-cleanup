# Uranium Image Cleanup
--------
To run this program, see the first use case below. 

 This package was designed to take in user input (a directory where images of uranium are stored), ask for an output folder and then proceed to process images in specified directory to remove text/noise. 

Below is an example of how our ideal user should use install and use this package (AFIT = ideal user).

***Note:*** This package was designed to run our driver.py, or main(), code, much like an executable. We have provided use cases where the functionality of our package outside of running as a program that requires user input, ect... is useful. 

Remember to run these in a python shell.

## To install:

```
    >>> python3 -m pip install --index-url https://pypi.org/project/uranium_image_cleanup==version-number
```
## To run the program:

```
    >>> import uranium_image_cleanup_package as uic
    >>> 
    >>> uic.main()
    >>>
    >>> *** Uranium Image Cleanup  ***
    >>> Enter Image/s Retrieval Directory:
```

## This package is capable of:

- Removing text/noise on a single image of uranium.
- Detecting white pixels from a image.

Below are examples on how to implement these.

###### Use case to work on a single image:

``` 
    >>> import uranium_image_cleanup_package as uic
    >>> import opencv as cv2
    >>>
    >>> image uranium_nucleus_10593520                  
    >>> result_image = uic.removeLabel(uranium_nucleus_10593520)

```
###### Detect white pixels from an image:
``` 
    >>> import uranium_image_cleanup_package as uic
    >>> import opencv as cv2
    >>>
    >>> image uranium_nucleus_10593520                  
    >>> white_pixel_image = uic.detectWhite(img)
```

For more info and access to all the methods available, consult the remove_label.py script.

----------------------------



