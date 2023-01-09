# License Plate number detection and notification system
For ethos 2022 IIT Guwahati

## How to run on local system? 
<p>1. Clone the repo</p>

```git
git clone https://github.com/Roshaen/detection-notification-sns-processing.git
```
<p>2. Create virtual enviroment</p>

```bash
python -m venv env
```
```bash
source env/bin/activate
```

<p>3. Install required dependencies </p>

```bash
pip install -r requirements.txt
```
<p> 4. Clone yolov5 repo and install dependencies</p>

```bash
git clone https://github.com/ultralytics/yolov5.git  
cd yolov5
pip install -r requirements.txt
cd ..
```

<p> 5. Add pytesseract to the system path </p>
<p> Refer this link - https://pypi.org/project/pytesseract for pytesseract installation</p>

<p> 6. Run main.py </p>

```bash 
python3 main.py
```

