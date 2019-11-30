# face-detector
Python exercise - detect total faces in image url, wrapped by flask


## docker version
pull it from docker hub
```
docker run -p 5000:5000 itamarco/face-detector
```

## run it locally
```
git pull https://github.com/itamarco/face-detector.git
cd face-detector
pip install -r requirements.txt
python -m flaskr
```
## face detection request
```
curl -X POST \
  http://localhost:5000/detect-faces \
  -F 'url=<img url>'
```
