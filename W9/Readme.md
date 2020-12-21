# Praca z obrazami - OpenCV + Python

Ładowanie i wyświetlanie obrazu
```
image = cv2.imread("images/car1.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

#Wyświetlanie obrazu
cv2_imshow(image)
```
![car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car1.jpg?raw=true)

Otrzymywanie danych na temat poszczególnego piksela
```
(B, G, R) = image[150, 150]
print("R={}, G={}, B={}".format(R, G, B))
```
Odpowiedź: R=142, G=131, B=101

Przycinanie obrazu
```
crop = image[600:1600, 1000:2600]
cv2.imwrite("images/crop-car1.jpg", crop)
cv2_imshow(crop)
```
![crop-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/crop-car1.jpg?raw=true)

Prosta zmiana rozmiaru obrazu
```
resized = cv2.resize(image, (300, 300))
cv2.imwrite("images/resized-car1.jpg", resized)
cv2_imshow(resized)
```
![resized-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/resized-car1.jpg?raw=true)


Poprawiona zmiana rozmiaru obrazu
```
r = 300.0 / w
dim = (300, int(h * r))
fixed_resized = cv2.resize(image, dim)
cv2.imwrite("images/fixed-resized-car1.jpg",fixed_resized)
cv2_imshow(fixed_resized)
```
![fixed-resized-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/fixed-resized-car1.jpg?raw=true)

Zmiana roziaru obrazu z wykorzystaniem imutils
```
imutils_fixed_resized = imutils.resize(image, width=300)
cv2.imwrite("images/imutils-resized-car1.jpg", imutils_fixed_resized)
cv2_imshow(imutils_fixed_resized)
```
![imutils-resized-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/imutils-resized-car1.jpg?raw=true)

Obracanie obrazu
```
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("images/rotated-car1.jpg", rotated)
cv2_imshow(rotated)
```
![rotated-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/rotated-car1.jpg?raw=true)

Obracanie obrazu z użyciem imutils
```
imutils_rotated = imutils.rotate(image, -45)
cv2.imwrite("images/imutils-rotated-car1.jpg", imutils_rotated)
cv2_imshow(imutils_rotated)
```
![imutils-rotated-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/imutils-rotated-car1.jpg?raw=true)

Obracanie obrazu z użyciem imutils.rotate_bound. Obracanie uwzględnia skalowanie obrazu
```
rotated_bound = imutils.rotate_bound(image, 45)
cv2.imwrite("images/rotated-bound-car1.jpg", rotated_bound)
cv2_imshow(rotated_bound)
```
![rotated-bound-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/rotated-bound-car1.jpg?raw=true)

Rozmycie obrazu
```
blurred = cv2.GaussianBlur(image, (77, 77), 0)
cv2.imwrite("images/blurred-car1.jpg", blurred)
cv2_imshow(blurred)
```
![blurred-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/blurred-car1.jpg?raw=true)


Rysowanie na obrazie - kwadrat
```
output = image.copy()
cv2.rectangle(output, (500, 960),(880, 1160), (0, 0, 255), 2)
cv2.imwrite("images/drawing-car1.jpg", output)
cv2_imshow(output)
```
![drawing-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/drawing-car1.jpg?raw=true)

Rysowanie na obrazie - orkąg
```
output_2 = image.copy()
cv2.circle(output_2, (1500, 1160), 200, (255, 0, 255), 2)
cv2.imwrite("images/drawing-circle-car1.jpg", output_2)
cv2_imshow(output_2)
```
![drawing-circle-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/drawing-circle-car1.jpg?raw=true)

Rysowanie na obrazie - linia
```
output_3 = image.copy()
cv2.line(output_3, (120, 660), (1200, 660), (255, 0, 255), 10)
cv2.imwrite("image/drawing-line-car1.jpg", output_3)
cv2_imshow(output_3)
```
![drawing-line-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/drawing-line-car1.jpg?raw=true)

Dodanie napisu do obrazu
```
output_4 = image.copy()
cv2.putText(output_4, "OpenCV + Old car", (100, 250), 
	cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 2)
cv2.imwrite("image/text-car1.jpg", output_4)
cv2_imshow(output_4)
```

![text-car1.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/text-car1.jpg?raw=true)

Zmiana skali kolorów oraz wczytanie nowego obrazu
```
image2 = cv2.imread("images/car2.jpg")
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
cv2_imshow(image2)
cv2.imwrite("images/car2-gray.jpg", image2)
cv2_imshow(gray)
```
![car2.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2.jpg?raw=true)<br>
![car2-gray.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2-gray.jpg?raw=true)

Wykrywanie krawędzi

```
edged = cv2.Canny(gray, 150, 150)
cv2.imwrite("images/car2-edged.jpg", edged)
cv2_imshow(edged)
```
![car2-edged.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2-edged.jpg?raw=true)

Progowanie - wyznaczanie poziomu jasności dla zdjęcia
```
thresholding = cv2.threshold(gray, 60, 1000, cv2.THRESH_BINARY_INV)[1]
cv2.imwrite("images/threshold-car2.jpg", thresholding)
cv2_imshow(thresholding)
```
![threshold-car2.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/threshold-car2.jpg?raw=true)

Znajdowanie oraz oznaczanie kontur
```
cnts = cv2.findContours(thresholding.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output_5 = image2.copy()

for c in cnts:
  cv2.drawContours(output_5, [c], -1, (240, 0, 159), 10)
  
cv2.imwrite("images/car2-drawContours.jpg", output_5)
cv2_imshow(output_5)
```
![car2-drawContours.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2-drawContours.jpg?raw=true)

Erozje i dylatacje
```
mask = thresholding.copy()
mask_2 = thresholding.copy()
mask = cv2.erode(mask, None, iterations=2)
mask_2 = cv2.dilate(mask_2, None, iterations=5)
cv2.imwrite("images/car2-eroded.jpg", mask)
cv2.imwrite("images/car2-eroded.jpg", mask_2)
cv2_imshow(mask)
cv2_imshow(mask_2)
```
![car2-eroded.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2-eroded.jpg?raw=true)<br>
![car2-dilated.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2-dilated.jpg?raw=true)

Operacje maskujące i bitowe
```
mask_3 = thresholding.copy()
output_6 = cv2.bitwise_and(image2, image2, mask=mask)
cv2.imwrite("images/car2-mask.jpg", output_6)
cv2_imshow(output_6)
```
![car2-mask.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W9/images/car2-mask.jpg?raw=true)
