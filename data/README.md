This directory holds:
- Precomputed object proposals
- Caffe models pretrained on ImageNet
- Fast R-CNN models
- Symlinks to datasets

To download precomputed selective search proposals, run:

```
./tools/scripts/fetch_selective_search_data.sh
```

This script will populate `data/selective_search_data`.

To download Caffe models pretrained on ImageNet, run:

```
./tools/scripts/fetch_imagenet_models.sh
```

This script will populate `data/imagenet_models`.

To download Fast R-CNN models, run:

```
./tools/scripts/fetch_fast_rcnn_models.sh
```

This script will populate `data/fast_rcnn_models`.

In order to train and test with PASCAL VOC, you will need to establish symlinks.
From the `data` directory (`cd data`):

```
# For VOC 2007
ln -s /your/path/to/VOC2007/VOCdevkit VOCdevkit2007

# For VOC 2012
ln -s /your/path/to/VOC2012/VOCdevkit VOCdevkit2012
```

Since you'll likely be experimenting with multiple installs of Fast R-CNN in
parallel, you'll probably want to keep all of this data in a shared place and
use symlinks. On my system I create the following symlinks inside `data`:

```
# data/cache holds various outputs created by the datasets package
ln -s /data/fast_rcnn_shared/cache

# move the imagenet_models to shared location and symlink to them
ln -s /data/fast_rcnn_shared/imagenet_models

# move the selective search data to a shared location and symlink to them
ln -s /data/fast_rcnn_shared/selective_search_data

ln -s /data/VOC2007/VOCdevkit VOCdevkit2007
ln -s /data/VOC2012/VOCdevkit VOCdevkit2012
```