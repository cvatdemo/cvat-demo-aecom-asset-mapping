# Licenses and credit

## Photos and labels

Oil Tanks dataset by Liangyu Wu, Roboflow Universe (https://universe.roboflow.com/liangyu-wu/oil-tanks), licensed CC BY 4.0..

- Source: Oil Tanks (Roboflow Universe, by Liangyu Wu) (https://universe.roboflow.com/liangyu-wu/oil-tanks/dataset/4)
- License: CC BY 4.0
- Changes made for this demo: a subset of 92 images; bounding-box labels converted to CVAT rectangles; the main-line polyline label kept for the reviewer to draw by hand (the model only boxes tanks).

- Illustrative aerial and satellite imagery of above-ground storage tanks (oil and water tanks at industrial and treatment-plant sites). These oil storage tanks stand in for the water and sewer facility tanks you would map; they are not your data.
- The tank label is a bounding box, matching the box answer key, so the quality score compares like with like.
- The main-line polyline label has no answer-key examples on purpose: labeled pipes and major lines are rare in aerial imagery, so a reviewer draws the main lines by hand. The polyline requirement therefore has nothing to score against and reads as not applicable.
- The answer key is not exhaustive per image: some images have visible unlabeled tanks, so recall against it is a soft number. It still supports the point that a missed asset is the costly error.
- Some images carry a map-viewer banner or watermark along the top or bottom edge from the source capture; the tanks themselves are clean overhead views.

## Model

- The model is Aerial Tanks on Roboflow Universe
  (https://universe.roboflow.com/yamen-gm7rm/aerial-tanks/model/2), licensed CC BY 4.0. Its
  weights are not included (hosted by Roboflow, not redistributable).
  model/roboflow_tank_func.py calls it through the Roboflow API with your own key.
- The first-pass tank boxes in the backup were made in CVAT Online by a Roboflow-hosted model, Aerial Tanks (https://universe.roboflow.com/yamen-gm7rm/aerial-tanks/model/2), licensed CC BY 4.0. Its weights are trained and hosted by Roboflow; they are not included here and cannot be redistributed. Roboflow integration is a CVAT Online feature. The open-source way to run the same model is model/roboflow_tank_func.py, which calls the Roboflow API with your own Roboflow key. You do not have to run it: the model's first pass is already in the backup.

## CVAT

CVAT is open source under the MIT License: https://github.com/cvat-ai/cvat. `scripts/setup.sh`
downloads it at tag `v2.82.0`. CVAT Online features shown in `clickthrough.html` are not part
of the open-source release.
