# SparseDespike
An implementation of the Despiking/Data cleaning algorithm for spectral trajectories as described in [Kennedy et al. 2015](http://osu-wams-blogs-uploads.s3.amazonaws.com/blogs.dir/2108/files/2015/05/Kennedy_etal2010.pdf)

This version is adapted to work with sparse data (ie irregular spacing) by computing the linear interpolation between neighbouring points.

The process is iteratively applied, despiking the largest deviation from interpolation on each pass, until no points on the timeseries exceed the tolerance threshold.

More info can be found in my [write-up on my website](https://levikeay.github.io/Project_Site/blog/Spectral_despike).

![image](https://user-images.githubusercontent.com/63168148/186097612-0c4c06d0-09df-4e83-b4fe-889eccd94588.gif)
