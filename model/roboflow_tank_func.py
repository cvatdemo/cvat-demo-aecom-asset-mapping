# CVAT auto-annotation function: the same hosted model the demo used for the first pass, the
# Aerial Tanks model on Roboflow (CC BY 4.0). Its weights are trained and hosted by Roboflow and
# are not included here; the model cannot be redistributed as a file. This function calls the
# Roboflow serverless API with YOUR OWN Roboflow key and uploads the tank boxes it returns, the
# same way your own model would plug in.
#
# This is only needed if you want to run the model again yourself. The first-pass tank boxes from
# this model are already in the backup (demo/backup.zip), so you can see them without running
# anything. In open-source CVAT the hosted-model integration you saw in the browser is a CVAT
# Online feature; this script is the open-source way to run the same model.
#
# Set up a free Roboflow key (https://docs.roboflow.com/api-reference/authentication) and export it:
#     export ROBOFLOW_API_KEY=your_key_here
# Then: bash scripts/auto_annotate.sh
#
# To use your own tank detector instead: replace the request below with your model's call and
# return cvataa.rectangle(0, [x1, y1, x2, y2]) for each box, in pixels. The same command uploads
# them to CVAT. Nothing else needs to change.
import io
import os

import PIL.Image
import requests

import cvat_sdk.auto_annotation as cvataa

# The Roboflow model and version the demo used for the first pass. Aerial Tanks, CC BY 4.0.
# https://universe.roboflow.com/yamen-gm7rm/aerial-tanks/model/2
_MODEL = "aerial-tanks/2"
_ENDPOINT = "https://serverless.roboflow.com"

# The Roboflow API returns the detection class as "0" (not "tank"); it maps to the project's
# tank rectangle label, which is label index 0 in the spec below.
_API_CLASS = "0"

# The label name must match a label in the CVAT project.
spec = cvataa.DetectionFunctionSpec(labels=[cvataa.label_spec("tank", 0)])


def _key():
    key = os.environ.get("ROBOFLOW_API_KEY")
    if not key:
        raise SystemExit(
            "ROBOFLOW_API_KEY is not set. This function runs the hosted Aerial Tanks model, which "
            "needs your own Roboflow key (the weights are not shipped and cannot be redistributed). "
            "Get a free key at https://docs.roboflow.com/api-reference/authentication then run:  "
            "export ROBOFLOW_API_KEY=your_key_here  and try again. The model's first-pass tank "
            "boxes are already in demo/backup.zip if you only want to look at them."
        )
    return key


def detect(context: cvataa.DetectionFunctionContext, image: PIL.Image.Image):
    # The demo used a deliberately low threshold (0.1): this is a weak generic first pass on hard
    # aerial tiles, so a low threshold puts a few visible boxes on the canvas for a reviewer to
    # correct. A high threshold returns nothing.
    threshold = 0.1 if context.conf_threshold is None else context.conf_threshold
    buf = io.BytesIO()
    image.convert("RGB").save(buf, format="JPEG")
    buf.seek(0)
    r = requests.post(
        f"{_ENDPOINT}/{_MODEL}",
        params={"api_key": _key(), "confidence": threshold},
        data=buf.getvalue(),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=300,
    )
    if not r.ok:
        raise SystemExit(f"Roboflow answered {r.status_code}: {r.text[:300]}")
    shapes = []
    for p in r.json().get("predictions", []):
        if str(p.get("class")) != _API_CLASS:
            continue
        x, y, w, h = p["x"], p["y"], p["width"], p["height"]
        shapes.append(cvataa.rectangle(0, [float(x - w / 2), float(y - h / 2), float(x + w / 2), float(y + h / 2)]))
    return shapes
