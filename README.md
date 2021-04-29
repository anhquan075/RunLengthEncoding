# RunLengthEncoding

## Package Requirements
```
pip install pillow==2.4.0
```
## Run images folder
Chay file ```test_image.py``` để nhận kết quả encoding và decoding của tất cả các ảnh trong thư mục ```images``` bao gồm các ảnh ở dạng ```4bit```, ```8bit``` và ```black&white```
```python
python test_image.py
```
Kết quả được lưu trong file ```results.json```
## Run with a image
### Encoding
```python
python main.py -e path-to-image-to-encoding
```
### Decoding
```python
python main.py -d path-to-image-to-decoding 
```
