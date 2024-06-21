Cherry Mold Detection
## How to use this repo

1. Fork this repo and copy the https URL of your forked Walkthrough01 repo

1. Log into the cloud IDE with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open the jupyter_notebooks directory in the explorer sidebar, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

1. Choose the kernel that says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code cell.

Your workspace is now ready to use. When you want to return to this project, you can find it in your Cloud IDE Dashboard</a>. You should only create one workspace per project.

## Dataset Content

The dataset contains x images taken from x workflow. The leaves are either mold infected or uninfected.

## Business Requirements

As a Data Analyst, you are requested by the company to provide actionable insights and data-driven recommendations to a Cherry Plantage. The client is currently facing challenges in mold detection, especially with cherry leaves.

- 1 - The client is interested in having a study that visually differentiates a infected from an uninfected leave.
- 2 - The client is interested in telling whether a given leave contains mold or not.

## Hypothesis and how to validate?

- We suspect mold on these leaves and they have clear marks/signs, typically for mold on the leave, differentiating them from uninfected leaves.
  - An average image study can help to investigate it

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Data Visualization

  - We will display the "mean" and "standard deviation" images for infected and uninfected leave.
  - We will display the difference between average infected and uninfected leave.
  - We will display an image montage for either infected or uninfected leave.

- **Business Requirement 2**: Classification
  - We want to predict if a given leave is infected or not with mold.
  - We want to build a binary classifier and generate reports.

## ML Business Case

### MoldClf

- We want an ML model to predict if a leave is infected with mold or not based on historical image data. It is a supervised model, a 2-class, single-label classification model.
- Our ideal outcome is to provide the medical team with a faster and more reliable diagnostic for mold detection.
- The model success metrics are
  - Accuracy of x% or above on the test set.
- The model output is defined as a flag, indicating if the leave has mold or not and the associated probability of being infected or not. As usual, the staff would take a picture of the leave and upload the picture to the App. The prediction is made on the fly (not in batches).
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and non-infected leaves. A leave is photographed and uploaded to the app. Visual criteria are used to detect mold on cherry leaves. It leaves room to produce inaccurate diagnostics due to human error. On top of that, specially trained staff and expertise could be conducted.
- The training data to fit the model come from the X [x](https://x/). This dataset contains about x+ thousand images. We have extracted a subset of x images from this dataset and saved it to [Kaggle dataset directory](https://www.kaggle.com/codeinstitute/x/) for quicker model training.
  - Train data - target: infected or not; features: all images

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary

- Quick project summary
  - General Information
    - Facts about mold on Cherry Leaves
  - Project Dataset
    - The available dataset contains x out of +x thousand images taken from cherry leaves that are infected or uninfected with mold.
  - Link to additional information
  - Business requirements
    - The client is interested in having a study to differentiate between a parasite-contained and uninfected leave visually.
    - The client is interested in whether a given cherry leave contains mold or not.

### Page 2: Cells Visualizer

- It will answer business requirement 1
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between average infected and average uninfected leave
  - Checkbox 3 - Image Montage

### Page 3: Malaria Detector

- Business requirement 2 information - "The client is interested in telling whether a given cherry leave contains mold or not."
- Link to download a set of mold-contained and uninfected leave images for live prediction.
- User Interface with a file uploader widget. The user should upload multiple cherry leave images. It will display the image and a prediction statement, indicating if the leave is infected or not with mold and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

- Block for each project hypothesis, describe the conclusion and how you validated it.

### Page 5: ML Performance Metrics

- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result
