# OlympusVSI to SVS or OMETiff

> To transform OlympusVSI slides to other formates in batch

We have a VS200 scanner and an online platform Cytomine to process slides. These scripts are for converting OlympusVSI to OME-TIFF (QuPath converter.py) or SVS (Slideio converter.py), two formats Cytomine can process.

It turns out uploaded SVS files can be directly indexed by Cytomine, while OME-TIFF requires a lot of time and resources to process first. So I recommend SVS for Cytomine.


```
│  QuPath converter.py
│  Slideio converter.py
│
├─in
│  │  HE_M3396.vsi
│  │  HE_M3405.vsi
│  │  HE_M3433.vsi
│  │
│  ├─_HE_M3396_
│  │  ├─stack1
│  │  │      frame_t.ets
│  │  │
│  │  ├─stack10000
│  │  │      blob_21_f.meta
│  │  │      blob_21_f_Frame#0.ets
│  │  │      frame_t.ets
│  │  │
│  │  └─stack10002
│  │          frame_t.ets
│  │
│  ├─_HE_M3405_
│  │  ├─stack1
│  │  │      frame_t.ets
│  │  │
│  │  ├─stack10000
│  │  │      blob_21_f.meta
│  │  │      blob_21_f_Frame#0.ets
│  │  │      frame_t.ets
│  │  │
│  │  └─stack10002
│  │          frame_t.ets
│  │
│  └─_HE_M3433_
│      ├─stack1
│      │      frame_t.ets
│      │
│      ├─stack10000
│      │      blob_21_f.meta
│      │      blob_21_f_Frame#0.ets
│      │      frame_t.ets
│      │
│      └─stack10002
│              frame_t.ets
│
└─out
        HE_M3396.ome.tif
        HE_M3405.ome.tif
        HE_M3433.ome.tif
```
