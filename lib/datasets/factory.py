# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

from datasets.pascal_voc import pascal_voc
from datasets.coco import coco
from datasets.rpn_uboone import rpn_uboone
from datasets.image import image

from fast_rcnn.config import cfg

import numpy as np

# Setup rpn_uboone
for split in ['train_'    + str(cfg.UB_N_CLASSES),\
              'val_'      + str(cfg.UB_N_CLASSES),\
              'trainval_' + str(cfg.UB_N_CLASSES),\
              'test_'     + str(cfg.UB_N_CLASSES)] :
    
    print split
    name = 'rpn_uboone_{}'.format(split)
    __sets[name] = (lambda split=split :  rpn_uboone(split))

# Set up imags
for split in ['train','val','trainval']:
    name = 'image_{}'.format(split)
    __sets[name] = (lambda split=split :  image(split))

# Set up voc_<year>_<split> using selective search "fast" mode
for year in ['2007', '2012']:
    for split in ['train', 'val', 'trainval', 'test']:
        name = 'voc_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))

# Set up coco_2014_<split>
for year in ['2014']:
    for split in ['train', 'val', 'minival', 'valminusminival']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2015_<split>
for year in ['2015']:
    for split in ['test', 'test-dev']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

def get_imdb(name):
    """Get an imdb (image database) by name."""
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
