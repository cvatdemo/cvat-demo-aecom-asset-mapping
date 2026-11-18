# Walkthrough: AECOM demo on open-source CVAT

A self-guided tour of the same flow you saw in the demo, on your own machine. Open `clickthrough.html` next to this file to see each screen as it looked in CVAT Online.

Each step is marked **Free** (works in open-source CVAT) or **CVAT Online** (a paid feature, shown in the click-through only). Run `bash start.sh` first (or `bash scripts/setup.sh` and `bash scripts/restore.sh`); the links below are printed by `restore.sh` and saved in `demo/local-urls.txt`.

## c. Automatic annotation

1. **A batch of 92 aerial tiles** (Free). This is a batch of 92 aerial tiles, the kind of imagery a client hands you when a facility has no asset plans. It is split into jobs so several reviewers can work at once. The whole point is to digitize the tiny things fast, so you can bid the smaller utilities that manual digitization makes not worth it.
2. **Task actions** (Free). Before a reviewer draws anything, a model takes the first pass over the whole batch. Your people then correct it, instead of digitizing every tile from a blank image.
3. **Choose a model** (CVAT Online). First we pick which model takes the first pass over the batch.
   - On open source: not available. See this screen in `clickthrough.html`.
4. **Any model plugs in** (CVAT Online). Any model connected to the account shows here. Your own asset detector, one from Hugging Face, or one from Roboflow. The model does not have to be ours, and it never trains on your data here.
   - On open source: not available. See this screen in `clickthrough.html`.
5. **Pre-label the whole batch** (CVAT Online). You map what the model knows to your labels, here a generic aerial tank detector onto your tank label, and run it across every tile in one click. This is the fast first pass that turns imagery into asset boxes without anyone drawing from scratch. Your own model would plug in exactly the same way.
   - On open source: this dialog needs models deployed with Nuclio, a separate setup. The simpler route is `scripts/auto_annotate.sh`, which runs a model on your machine and uploads its boxes.
6. **The job the model labeled** (Free). Here is the job the model has already pre-labeled. Let's open it and see what it caught, and what it missed.
7. **Model pre-labels on the tiles** (Free). The model has already placed its tank boxes across the batch. It is a generic detector, so on your domain-specific water and sewer assets it catches some tanks and misses others. That gap is exactly what a reviewer fills in, and exactly what the answer key measures next.
   - Try it: open the `model_job` link. Press F and D to move between tiles.

## d. Human in the loop

8. **AI tools on the canvas** (CVAT Online). With Segment Anything 3 your reviewer types what they are looking for in plain words. Here, tank. This is the live refinement step that tightens a footprint without drawing it by hand.
   - On open source: Segment Anything 3 text prompts are not included. See this screen in `clickthrough.html`.
9. **Every tank outlined** (CVAT Online). One word, and the tank footprints in the tile are outlined. No training and no setup. Your reviewer still checks it and keeps what is right, so the speed comes without giving up the final say.
   - On open source: not included. See this screen in `clickthrough.html`.
10. **Who made each label** (Free). Your reviewer fixes what the model missed and draws the main lines, because the model finds tank footprints, not linear features. Every label records who made it, model or person, so you can filter to just the model's boxes or just a person's and correct from there. Your team has the final say.
   - Try it: in the job, click Filters, Add rule, pick Source.
11. **Back to the batch** (Free). The next question is who does the correcting, since you do not staff a labeling team for this.
12. **Add annotators** (CVAT Online). If you need more hands, Outsource Labeling sends the batch to CVAT's vetted annotators. They work to the same tank and main-line labels and the same quality rules, and your people can work in the same project alongside them, with AECOM keeping the final say.
   - On open source: not included. CVAT's annotators are a CVAT Online service.

## e. Quality you can measure

13. **The answer key** (Free). This is a small set of tiles, 20 here, with the tanks labeled carefully once. Every job is scored against it automatically, whoever drew the labels, the model, our annotators or your team. Quality is measured, not assumed. On a pilot your own experts would set this key on your facility.
   - Try it: open the `gt_job` link.
14. **Back to the batch** (Free). We go back to a batch to catch a bad one before it reaches you.
15. **A batch an annotator calls done** (Free). This batch still has only the model's boxes in it, and it missed one of the tanks. Let's pretend an annotator calls it done and tries to hand it over.
16. **Finish the job** (Free). The annotator clicks Finish the job to hand the batch over as finished work.
17. **Confirm finishing** (Free). because finishing hands the batch over as completed work.
18. **The job bounces** (CVAT Online). It checked the batch against the answer key before accepting it, and it names what is missing. The work goes back to the annotator, not on to you. A missed asset is the costly error here, and it never becomes a bad asset inventory or training data.
   - On open source: the job completes without the check. Run `scripts/quality_report.sh` afterwards to get the same scores.
19. **Back to the batch** (Free). Every job carries a score against the answer key, not just the one that bounced.
20. **Quality control** (CVAT Online). This is where you, or we, check quality on the batch at any time.
   - On open source: not available. See this screen in `clickthrough.html`.
21. **A score for every job** (CVAT Online). Every job gets a score against the answer key. The model's first pass scores low, and that is the point, it shows exactly how far a generic model is from your standard on domain-specific assets before you rely on it. On your own tiles, with your own model, this is the number a pilot measures.
   - On open source: run `scripts/quality_report.sh` for the same per-job scores in the terminal. The score screens in the browser are CVAT Online.
22. **Your quality rules** (CVAT Online). These are the rules. A tank box must be 80 percent accurate to drop into your GIS. A missed tank must be caught 95 percent of the time, because a missed asset is the costly error, the whole value is catching the asset nobody had on a plan. Main lines are held to 80 percent accuracy too. You set these, and every job is held to them.
   - On open source: the rules are loaded from `demo/quality.json` by `scripts/restore.sh` and used by the report. The requirements screen itself is CVAT Online.
23. **Export for Esri and Python** (Free). Once a batch passes, the checked tank boxes and main lines export in a standard format your Esri stack and custom Python tools already read, with no conversion step. CVAT stops at export on purpose. Whether you train an asset detector on these labels or just digitize to GIS stays your call, in your pipeline or a partner's. The answer key keeps checking every batch whichever model drew it.
   - Try it: on the task page: Actions, Export task dataset.

---

The photos are a public dataset, not your data: Oil Tanks dataset by Liangyu Wu, Roboflow Universe (https://universe.roboflow.com/liangyu-wu/oil-tanks), licensed CC BY 4.0.. Details in `LICENSES.md`.

