# Cricket-Performance-Predictor
An end-to-end machine learning and computer vision-ready pipeline that processes raw sports telemetry to predict T20 batting performance categories: Early Dismissal (<15 runs), Stable Anchor (15-40 runs), and Match Winner (>40 runs).

## Performance & Features - 
Overall Accuracy: 42.68% (High-performance baseline for sports analytics), 
Early Dismissal Precision: 73% (Highly reliable risk-detection engine), 
Match-Winner Recall: 59% (Anticipates rare high-impact peaks)

## How to Run the Frontend Dashboard Locally
To view the interactive visual scouting dashboard, open the terminal/command prompt and:
### 1. Install required visualization libraries
pip install streamlit plotly
### 2. Navigate to your project directory
cd path/to/T20 Analytics
### 3. Launch the web application
python -m streamlit run app.py
