# OlympusVSI_to_OMETiff
> Transform OlympusVSI slides to OME-TIFF in batch using QuPath

We have a VS200 scanner and a online platform cytomine to process slides. This script is for converting OlympusVSI to OME-TIFF, a formate cytomine can process.


```
│  QuPath converter.py
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
